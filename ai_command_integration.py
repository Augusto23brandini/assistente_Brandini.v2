"""
Integração do processador de comandos ao assistente principal
"""

from modules.command_processor import CommandProcessor

def process_ai_command(text, llm_manager=None):
    """
    Processa comandos relacionados a assistentes virtuais, LLMs e IAs
    usando o processador de comandos especializado ou o LLM padrão
    
    Args:
        text (str): Texto do comando
        llm_manager: Gerenciador de LLM para fallback (opcional)
        
    Returns:
        dict: Resposta processada com texto e metadados
    """
    # Inicializar processador de comandos
    processor = CommandProcessor()
    
    # Tentar processar com o processador especializado
    response = processor.process_command(text)
    
    # Se a resposta for genérica e tivermos um LLM disponível, usar como fallback
    if response.startswith("Não tenho") and llm_manager:
        # Adicionar contexto para o LLM
        context = """
        Você é o Assistente Brandini, especializado em informações sobre assistentes virtuais,
        modelos de linguagem grandes (LLMs), inteligências artificiais e chatbots.
        Responda à pergunta do usuário de forma concisa e informativa.
        """
        
        llm_response = llm_manager.generate_response(
            text, 
            system_prompt=context
        )
        
        return {
            "text": llm_response["text"],
            "source": llm_response["source"],
            "processed_by": "llm_fallback"
        }
    
    # Retornar resposta do processador especializado
    return {
        "text": response,
        "source": "knowledge_base",
        "processed_by": "command_processor"
    }
