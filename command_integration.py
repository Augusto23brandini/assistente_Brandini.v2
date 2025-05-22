"""
Integração dos processadores de comando ao assistente principal
"""

from modules.command_processor import CommandProcessor
from modules.general_command_processor import GeneralCommandProcessor

def process_command(text, llm_manager=None):
    """
    Processa comandos usando múltiplos processadores em cascata
    
    Args:
        text (str): Texto do comando
        llm_manager: Gerenciador de LLM para fallback (opcional)
        
    Returns:
        dict: Resposta processada com texto e metadados
    """
    # Inicializar processadores
    general_processor = GeneralCommandProcessor()
    ai_processor = CommandProcessor()
    
    # Primeiro, tentar com o processador de comandos gerais
    response = general_processor.process_command(text)
    
    # Se a resposta for genérica, tentar com o processador de IA
    if response.startswith("Não entendi") or response.startswith("Não tenho certeza") or response.startswith("Desculpe, não consegui"):
        ai_response = ai_processor.process_command(text)
        
        # Se o processador de IA também retornar resposta genérica e tivermos um LLM disponível, usar como fallback
        if ai_response.startswith("Não tenho") and llm_manager:
            # Adicionar contexto para o LLM
            context = """
            Você é o Assistente Brandini, especializado em responder a comandos de voz e texto.
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
        
        return {
            "text": ai_response,
            "source": "knowledge_base",
            "processed_by": "ai_command_processor"
        }
    
    # Retornar resposta do processador geral
    return {
        "text": response,
        "source": "general_commands",
        "processed_by": "general_command_processor"
    }
