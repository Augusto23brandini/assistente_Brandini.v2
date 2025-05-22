"""
Módulo de processamento de comandos para o Assistente Brandini
Integra a base de conhecimento com o processamento de linguagem natural
"""

import re
import random
from modules.knowledge_base import KnowledgeBase

class CommandProcessor:
    """Processador de comandos para o Assistente Brandini"""
    
    def __init__(self):
        """Inicializa o processador de comandos"""
        self.knowledge_base = KnowledgeBase()
        
        # Padrões de comando para diferentes categorias
        self.command_patterns = {
            # Padrões para assistentes virtuais
            "assistente_info": [
                r"(?:o que|quem) (?:é|foi)(?: a| o)? (siri|alexa|google assistente|cortana|bixby|alice)",
                r"fale sobre(?: a| o)? (siri|alexa|google assistente|cortana|bixby|alice)",
                r"(?:me)? conte sobre(?: a| o)? (siri|alexa|google assistente|cortana|bixby|alice)",
                r"explique(?: o que é)?(?: a| o)? (siri|alexa|google assistente|cortana|bixby|alice)"
            ],
            "assistente_funcionalidades": [
                r"(?:quais são|me diga|liste) as funcionalidades d[oa] (siri|alexa|google assistente|cortana|bixby|alice)",
                r"o que(?: a| o)? (siri|alexa|google assistente|cortana|bixby|alice) (?:pode fazer|faz)",
                r"para que serve(?: a| o)? (siri|alexa|google assistente|cortana|bixby|alice)",
                r"como (?:usar|utilizar)(?: a| o)? (siri|alexa|google assistente|cortana|bixby|alice|android auto|carplay)"
            ],
            
            # Padrões para LLMs
            "llm_info": [
                r"(?:o que|quem) é(?: o)? (gemini|chatgpt|deepseek|claude|llama|gpt-4|palm)",
                r"fale sobre(?: o)? (gemini|chatgpt|deepseek|claude|llama|gpt-4|palm)",
                r"(?:me)? conte sobre(?: o)? (gemini|chatgpt|deepseek|claude|llama|gpt-4|palm)",
                r"explique(?: o que é)?(?: o)? (gemini|chatgpt|deepseek|claude|llama|gpt-4|palm)"
            ],
            "llm_capacidades": [
                r"(?:quais são|me diga|liste) as capacidades d[oe] (gemini|chatgpt|deepseek|claude|llama|gpt-4|palm)",
                r"o que(?: o)? (gemini|chatgpt|deepseek|claude|llama|gpt-4|palm) (?:pode fazer|faz)",
                r"como (?:funciona|opera)(?: o)? (gemini|chatgpt|deepseek|claude|llama|gpt-4|palm)"
            ],
            
            # Padrões para outras IAs
            "ia_info": [
                r"(?:o que|quem) é(?: o)? (alphago|dall-e|midjourney)",
                r"fale sobre(?: o)? (alphago|dall-e|midjourney)",
                r"(?:me)? conte sobre(?: o)? (alphago|dall-e|midjourney)",
                r"explique(?: o que é)?(?: o)? (alphago|dall-e|midjourney)"
            ],
            "ia_aplicacoes": [
                r"(?:quais|que) (?:ias|inteligências artificiais) são usadas (?:em|para) (carros autônomos|diagnóstico médico|sistemas de recomendação)",
                r"como as (?:ias|inteligências artificiais) (?:ajudam|são usadas) (?:em|para|no) (diagnóstico médico|carros autônomos|sistemas de recomendação)",
                r"aplicações de ia (?:em|para) (medicina|veículos|recomendação)"
            ],
            
            # Padrões para chatbots
            "chatbot_info": [
                r"(?:o que|quem) é(?: o)? (perplexity|copilot)",
                r"fale sobre(?: o)? (perplexity|copilot)",
                r"(?:me)? conte sobre(?: o)? (perplexity|copilot)",
                r"explique(?: o que é)?(?: o)? (perplexity|copilot)"
            ],
            "chatbot_tipos": [
                r"(?:quais são|me diga|liste) os principais chatbots baseados em llms",
                r"(?:quais|que) chatbots são (?:bons|melhores) para atendimento ao cliente",
                r"como criar um chatbot para (whatsapp|telegram|messenger|site)"
            ],
            
            # Padrões para comparações
            "comparacao": [
                r"(?:compare|comparação entre) (siri|alexa|google assistente|cortana|bixby|gemini|chatgpt|claude|llama)",
                r"(?:qual|quais)(?: é| são)? a(?:s)? diferença(?:s)? entre (siri|alexa|google assistente|chatgpt|claude)",
                r"(assistentes virtuais|chatbots) (?:versus|vs|ou) (assistentes virtuais|chatbots)",
                r"(?:quais são|me diga) os melhores (llms|assistentes virtuais|chatbots) (de código aberto|em português)"
            ],
            
            # Padrões para guias práticos
            "guia_pratico": [
                r"como configurar um assistente virtual em casa",
                r"(?:quais são|me diga|liste) os comandos básicos da alexa",
                r"como usar llms para estudar",
                r"(?:quais|que) assistentes virtuais (?:respeitam mais|são melhores para) a privacidade",
                r"como integrar chatbots em um site"
            ]
        }
    
    def process_command(self, text):
        """
        Processa um comando de texto e retorna uma resposta apropriada
        
        Args:
            text (str): Texto do comando
            
        Returns:
            str: Resposta ao comando
        """
        # Normalizar texto (minúsculas, sem pontuação excessiva)
        text = text.lower().strip()
        text = re.sub(r'[!?.,;:]+', '', text)
        
        # Verificar cada categoria de padrão
        for category, patterns in self.command_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, text)
                if match:
                    # Extrair entidade mencionada (se houver)
                    entity = match.groups()[0] if match.groups() else None
                    return self._generate_response(category, entity, text)
        
        # Se nenhum padrão específico for encontrado, tentar busca geral
        return self._fallback_response(text)
    
    def _generate_response(self, category, entity, original_text):
        """
        Gera uma resposta com base na categoria e entidade identificadas
        
        Args:
            category (str): Categoria do comando
            entity (str): Entidade mencionada (se houver)
            original_text (str): Texto original do comando
            
        Returns:
            str: Resposta gerada
        """
        # Assistentes virtuais
        if category == "assistente_info" and entity:
            info = self.knowledge_base.obter_informacao('assistentes_virtuais', entity)
            return self.knowledge_base.formatar_resposta(info)
        
        elif category == "assistente_funcionalidades" and entity:
            info = self.knowledge_base.obter_informacao('assistentes_virtuais', entity, 'recursos')
            if isinstance(info, list):
                response = f"O {entity.title()} pode:\n"
                for recurso in info:
                    response += f"- {recurso}\n"
                return response
            return f"Não tenho informações detalhadas sobre as funcionalidades do {entity.title()}."
        
        # LLMs
        elif category == "llm_info" and entity:
            info = self.knowledge_base.obter_informacao('llms', entity)
            return self.knowledge_base.formatar_resposta(info)
        
        elif category == "llm_capacidades" and entity:
            info = self.knowledge_base.obter_informacao('llms', entity, 'capacidades')
            if isinstance(info, list):
                response = f"O {entity.title()} pode:\n"
                for capacidade in info:
                    response += f"- {capacidade}\n"
                return response
            return f"Não tenho informações detalhadas sobre as capacidades do {entity.title()}."
        
        # Outras IAs
        elif category == "ia_info" and entity:
            info = self.knowledge_base.obter_informacao('outras_ias', entity)
            return self.knowledge_base.formatar_resposta(info)
        
        elif category == "ia_aplicacoes" and entity:
            # Mapear termos de busca para chaves no dicionário
            entity_map = {
                "carros autônomos": "carros_autonomos",
                "diagnóstico médico": "ia_medicina",
                "sistemas de recomendação": "sistemas_recomendacao",
                "medicina": "ia_medicina",
                "veículos": "carros_autonomos",
                "recomendação": "sistemas_recomendacao"
            }
            
            key = entity_map.get(entity)
            if key:
                info = self.knowledge_base.obter_informacao('outras_ias', key)
                return self.knowledge_base.formatar_resposta(info)
            return f"Não tenho informações específicas sobre aplicações de IA em {entity}."
        
        # Chatbots
        elif category == "chatbot_info" and entity:
            info = self.knowledge_base.obter_informacao('chatbots', entity)
            return self.knowledge_base.formatar_resposta(info)
        
        elif category == "chatbot_tipos":
            if "baseados em llms" in original_text:
                info = self.knowledge_base.obter_informacao('chatbots', 'llm_chatbots')
                return self.knowledge_base.formatar_resposta(info)
            elif "atendimento ao cliente" in original_text:
                info = self.knowledge_base.obter_informacao('chatbots', 'atendimento_cliente')
                return self.knowledge_base.formatar_resposta(info)
            elif "whatsapp" in original_text:
                info = self.knowledge_base.obter_informacao('chatbots', 'whatsapp_chatbots')
                return self.knowledge_base.formatar_resposta(info)
            return "Não tenho informações específicas sobre esse tipo de chatbot."
        
        # Comparações
        elif category == "comparacao":
            if "siri" in original_text and "alexa" in original_text and "google" in original_text:
                info = self.knowledge_base.obter_informacao('comparacoes', 'assistentes_populares')
                return self.knowledge_base.formatar_resposta(info)
            elif "chatgpt" in original_text and "claude" in original_text:
                info = self.knowledge_base.obter_informacao('comparacoes', 'chatgpt_vs_claude')
                return self.knowledge_base.formatar_resposta(info)
            elif "assistentes virtuais" in original_text and "chatbots" in original_text:
                info = self.knowledge_base.obter_informacao('comparacoes', 'assistentes_vs_chatbots')
                return self.knowledge_base.formatar_resposta(info)
            elif "código aberto" in original_text:
                info = self.knowledge_base.obter_informacao('comparacoes', 'llms_codigo_aberto')
                return self.knowledge_base.formatar_resposta(info)
            elif "português" in original_text:
                info = self.knowledge_base.obter_informacao('comparacoes', 'assistentes_em_portugues')
                return self.knowledge_base.formatar_resposta(info)
            return "Não tenho uma comparação específica sobre esses itens."
        
        # Guias práticos
        elif category == "guia_pratico":
            if "configurar" in original_text and "assistente" in original_text and "casa" in original_text:
                info = self.knowledge_base.obter_informacao('guias_praticos', 'configurar_assistente_casa')
                return self.knowledge_base.formatar_resposta(info)
            elif "comandos" in original_text and "alexa" in original_text:
                info = self.knowledge_base.obter_informacao('guias_praticos', 'comandos_alexa')
                return self.knowledge_base.formatar_resposta(info)
            elif "llms" in original_text and "estudar" in original_text:
                info = self.knowledge_base.obter_informacao('guias_praticos', 'usar_llms_estudar')
                return self.knowledge_base.formatar_resposta(info)
            elif "privacidade" in original_text:
                info = self.knowledge_base.obter_informacao('guias_praticos', 'privacidade_assistentes')
                return self.knowledge_base.formatar_resposta(info)
            elif "integrar" in original_text and "chatbots" in original_text and "site" in original_text:
                info = self.knowledge_base.obter_informacao('guias_praticos', 'integrar_chatbots_site')
                return self.knowledge_base.formatar_resposta(info)
            return "Não tenho um guia específico sobre esse tópico."
        
        # Fallback para categorias sem correspondência exata
        return self._fallback_response(original_text)
    
    def _fallback_response(self, text):
        """
        Gera uma resposta para comandos que não correspondem a padrões específicos
        
        Args:
            text (str): Texto original do comando
            
        Returns:
            str: Resposta gerada
        """
        # Buscar termos-chave em todas as categorias
        words = text.split()
        for word in words:
            if len(word) < 3:  # Ignorar palavras muito curtas
                continue
                
            results = self.knowledge_base.buscar_em_todas_categorias(word)
            if results:
                # Encontrou algo relacionado
                categories = list(results.keys())
                if len(categories) == 1:
                    category = categories[0]
                    items = results[category]
                    if len(items) == 1:
                        # Encontrou um único item
                        item = items[0]
                        if category == 'assistentes_virtuais':
                            info = self.knowledge_base.obter_informacao('assistentes_virtuais', item)
                            return self.knowledge_base.formatar_resposta(info, 'resumido')
                        elif category == 'llms':
                            info = self.knowledge_base.obter_informacao('llms', item)
                            return self.knowledge_base.formatar_resposta(info, 'resumido')
                        elif category == 'outras_ias':
                            info = self.knowledge_base.obter_informacao('outras_ias', item)
                            return self.knowledge_base.formatar_resposta(info, 'resumido')
                        elif category == 'chatbots':
                            info = self.knowledge_base.obter_informacao('chatbots', item)
                            return self.knowledge_base.formatar_resposta(info, 'resumido')
                    else:
                        # Encontrou múltiplos itens na mesma categoria
                        response = f"Encontrei várias informações sobre {word} na categoria {category.replace('_', ' ')}:\n"
                        for item in items[:5]:
                            response += f"- {item.replace('_', ' ').title()}\n"
                        if len(items) > 5:
                            response += "E outros...\n"
                        response += "\nPode me perguntar especificamente sobre um deles?"
                        return response
                else:
                    # Encontrou em múltiplas categorias
                    response = f"Encontrei informações sobre {word} em várias categorias:\n"
                    for category in categories[:3]:
                        items_str = ", ".join([item.replace('_', ' ').title() for item in results[category][:3]])
                        if len(results[category]) > 3:
                            items_str += " e outros"
                        response += f"- {category.replace('_', ' ').title()}: {items_str}\n"
                    if len(categories) > 3:
                        response += "E outras categorias...\n"
                    response += "\nPode me perguntar mais especificamente sobre algum desses tópicos?"
                    return response
        
        # Respostas genéricas quando nada é encontrado
        generic_responses = [
            "Não tenho informações específicas sobre isso. Posso falar sobre assistentes virtuais como Siri e Alexa, modelos de linguagem como ChatGPT e Gemini, ou outros tipos de IA.",
            "Não encontrei informações sobre esse tópico na minha base de conhecimento. Posso ajudar com informações sobre assistentes virtuais, LLMs, chatbots e outras tecnologias de IA.",
            "Não tenho dados suficientes para responder a essa pergunta. Que tal me perguntar sobre assistentes virtuais populares, modelos de linguagem ou chatbots?",
            "Não consegui entender completamente sua pergunta. Posso fornecer informações sobre Siri, Alexa, Google Assistente, ChatGPT, Gemini e muitas outras tecnologias de IA."
        ]
        return random.choice(generic_responses)

# Exemplo de uso
if __name__ == "__main__":
    processor = CommandProcessor()
    
    # Testar alguns comandos
    commands = [
        "O que é a Alexa?",
        "Quais são as funcionalidades do Google Assistente?",
        "Fale sobre o ChatGPT",
        "Como o DALL-E funciona?",
        "Compare Siri, Alexa e Google Assistente",
        "Como usar LLMs para estudar?",
        "Quais são os melhores assistentes em português?"
    ]
    
    for cmd in commands:
        print(f"\nComando: {cmd}")
        response = processor.process_command(cmd)
        print(f"Resposta: {response[:100]}...")  # Mostrar apenas o início da resposta
