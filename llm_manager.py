"""
Módulo de gerenciamento de modelos de linguagem (LLM)
Implementa alternância entre OpenAI API e modelos locais
"""

import os
import time
import json

# Verificar se OpenAI está disponível
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("Aviso: OpenAI API não está disponível. Usando apenas modelo local.")

# Verificar se Transformers está disponível para modelo local
try:
    from transformers import pipeline
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    print("Aviso: Transformers não está disponível. Usando implementação simulada.")

class LLMManager:
    """Gerenciador de modelos de linguagem com alternância entre OpenAI e local"""
    
    def __init__(self, openai_api_key=None, local_model="gpt2", system_prompt=None):
        """
        Inicializa o gerenciador de modelos de linguagem
        
        Args:
            openai_api_key (str): Chave da API OpenAI
            local_model (str): Nome do modelo local para usar com Transformers
            system_prompt (str): Prompt de sistema para contextualizar o modelo
        """
        self.openai_api_key = openai_api_key
        self.local_model = local_model
        self.system_prompt = system_prompt or "Você é um assistente de voz útil, conciso e amigável."
        self.local_generator = None
        self.use_openai = OPENAI_AVAILABLE and openai_api_key is not None
        self.conversation_history = []
        self.conversation_id = f"conv_{int(time.time())}"
        
        # Configurar OpenAI se disponível
        if OPENAI_AVAILABLE and self.openai_api_key:
            openai.api_key = self.openai_api_key
            print("OpenAI API configurada com sucesso")
        
        # Inicializar histórico de conversa
        self.conversation_history.append({
            "id": self.conversation_id,
            "messages": [
                {"role": "system", "content": self.system_prompt}
            ]
        })
    
    def _initialize_local_model(self):
        """Inicializa o modelo local sob demanda"""
        if self.local_generator is None and TRANSFORMERS_AVAILABLE:
            try:
                print(f"Inicializando modelo local {self.local_model}...")
                self.local_generator = pipeline('text-generation', model=self.local_model)
                print("Modelo local inicializado com sucesso!")
            except Exception as e:
                print(f"Erro ao inicializar modelo local: {e}")
                self.local_generator = None
    
    def toggle_backend(self):
        """
        Alterna entre OpenAI e modelo local
        
        Returns:
            str: Nome do backend ativo após a alternância
        """
        if not OPENAI_AVAILABLE or self.openai_api_key is None:
            return "Local (OpenAI não disponível)"
        
        self.use_openai = not self.use_openai
        return "OpenAI" if self.use_openai else f"Local ({self.local_model})"
    
    def generate_response(self, prompt, conversation_id=None, system_prompt=None, max_tokens=150):
        """
        Gera resposta para o prompt fornecido
        
        Args:
            prompt (str): Texto de entrada
            conversation_id (str): ID da conversa para manter contexto
            system_prompt (str): Prompt de sistema personalizado
            max_tokens (int): Número máximo de tokens na resposta
            
        Returns:
            dict: Dicionário com texto da resposta e fonte (openai ou local)
        """
        # Usar ID de conversa fornecido ou o padrão
        conv_id = conversation_id or self.conversation_id
        
        # Encontrar ou criar histórico para esta conversa
        conv = None
        for c in self.conversation_history:
            if c["id"] == conv_id:
                conv = c
                break
        
        if conv is None:
            # Criar novo histórico se não existir
            sys_prompt = system_prompt or self.system_prompt
            conv = {
                "id": conv_id,
                "messages": [
                    {"role": "system", "content": sys_prompt}
                ]
            }
            self.conversation_history.append(conv)
        
        # Adicionar mensagem do usuário ao histórico
        conv["messages"].append({"role": "user", "content": prompt})
        
        # Tentar API OpenAI primeiro, se configurada e ativada
        if self.use_openai and OPENAI_AVAILABLE and self.openai_api_key:
            try:
                # Preparar mensagens para a API
                messages = conv["messages"].copy()
                
                # Chamar API OpenAI
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=0.7
                )
                
                # Extrair resposta
                response_text = response.choices[0].message.content
                
                # Adicionar resposta ao histórico
                conv["messages"].append({"role": "assistant", "content": response_text})
                
                return {
                    "text": response_text,
                    "source": "openai"
                }
            except Exception as e:
                print(f"Erro na API OpenAI: {e}")
                print("Alternando para modelo local...")
                self.use_openai = False
        
        # Usar modelo local ou simulação
        if TRANSFORMERS_AVAILABLE:
            # Inicializar modelo local se necessário
            self._initialize_local_model()
            
            if self.local_generator:
                # Preparar contexto com histórico recente
                context = ""
                for msg in conv["messages"][-3:]:  # Usar apenas as 3 mensagens mais recentes
                    role = msg["role"]
                    if role == "system":
                        continue
                    prefix = "Usuário: " if role == "user" else "Assistente: "
                    context += f"{prefix}{msg['content']}\n"
                
                context += "Assistente: "
                
                # Gerar resposta
                try:
                    result = self.local_generator(
                        context, 
                        max_length=len(context.split()) + max_tokens,
                        num_return_sequences=1
                    )
                    
                    # Extrair apenas a parte gerada
                    full_text = result[0]['generated_text']
                    response_text = full_text[len(context):].strip()
                    
                    # Se a resposta estiver vazia, usar texto alternativo
                    if not response_text:
                        response_text = "Desculpe, não consegui gerar uma resposta adequada."
                    
                    # Adicionar resposta ao histórico
                    conv["messages"].append({"role": "assistant", "content": response_text})
                    
                    return {
                        "text": response_text,
                        "source": "local"
                    }
                except Exception as e:
                    print(f"Erro ao gerar resposta com modelo local: {e}")
        
        # Fallback: simulação simples
        response_options = [
            "Entendi. Como posso ajudar com isso?",
            "Interessante. Pode me contar mais?",
            "Estou processando sua solicitação. Um momento, por favor.",
            "Desculpe, estou com dificuldade para processar isso agora.",
            f"Olá! Estou aqui para ajudar com suas perguntas sobre {prompt.split()[-1] if len(prompt.split()) > 0 else 'diversos assuntos'}."
        ]
        
        import random
        response_text = random.choice(response_options)
        
        # Adicionar resposta ao histórico
        conv["messages"].append({"role": "assistant", "content": response_text})
        
        return {
            "text": response_text,
            "source": "mock"
        }
    
    def get_conversation_history(self, conversation_id=None):
        """
        Obtém o histórico de uma conversa específica
        
        Args:
            conversation_id (str): ID da conversa
            
        Returns:
            list: Lista de mensagens da conversa
        """
        conv_id = conversation_id or self.conversation_id
        
        for conv in self.conversation_history:
            if conv["id"] == conv_id:
                return conv["messages"]
        
        return []
    
    def clear_conversation(self, conversation_id=None):
        """
        Limpa o histórico de uma conversa específica
        
        Args:
            conversation_id (str): ID da conversa
        """
        conv_id = conversation_id or self.conversation_id
        
        for i, conv in enumerate(self.conversation_history):
            if conv["id"] == conv_id:
                # Manter apenas a mensagem do sistema
                system_msg = next((msg for msg in conv["messages"] if msg["role"] == "system"), None)
                if system_msg:
                    self.conversation_history[i]["messages"] = [system_msg]
                else:
                    self.conversation_history[i]["messages"] = []
                return True
        
        return False


# Exemplo de uso
if __name__ == "__main__":
    # Obter chave da API do ambiente
    api_key = os.environ.get("OPENAI_API_KEY")
    
    # Criar gerenciador
    llm = LLMManager(openai_api_key=api_key, local_model="gpt2")
    
    # Testar geração de resposta
    prompt = "Olá, como você está hoje?"
    print(f"Prompt: {prompt}")
    
    # Gerar resposta
    response = llm.generate_response(prompt)
    print(f"Resposta ({response['source']}): {response['text']}")
    
    # Alternar backend
    backend = llm.toggle_backend()
    print(f"Backend alternado para: {backend}")
    
    # Gerar nova resposta
    response = llm.generate_response("E o que você pode fazer por mim?")
    print(f"Resposta ({response['source']}): {response['text']}")
