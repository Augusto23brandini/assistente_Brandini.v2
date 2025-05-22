"""
Módulo de processamento de comandos gerais para o Assistente Brandini
Implementa os comandos comuns e específicos mapeados do arquivo de comandos
"""

import re
import random
import datetime
import os
from modules.knowledge_base import KnowledgeBase

class GeneralCommandProcessor:
    """Processador de comandos gerais para o Assistente Brandini"""
    
    def __init__(self):
        """Inicializa o processador de comandos gerais"""
        self.knowledge_base = KnowledgeBase() if 'KnowledgeBase' in globals() else None
        
        # Padrões de comando para diferentes categorias
        self.command_patterns = {
            # Informações Gerais
            "tempo": [
                r"qual (?:a|é) (?:previsão do tempo|tempo) (?:para|em) (hoje|amanhã|[\w\s]+)",
                r"como está o tempo (?:em|para) (hoje|amanhã|[\w\s]+)"
            ],
            "hora": [
                r"que horas são",
                r"qual (?:a|é) hora",
                r"me diga (?:a|as) horas?"
            ],
            "data": [
                r"que dia é hoje",
                r"qual (?:a|é) data de hoje",
                r"em que dia estamos"
            ],
            "definicao": [
                r"defina ([\w\s]+)",
                r"o que (?:significa|quer dizer|é) ([\w\s]+)",
                r"qual (?:a|é) definição de ([\w\s]+)"
            ],
            "calculo": [
                r"quanto é ([\d\s\+\-\*\/\%\^\(\)\.]+)",
                r"calcule ([\d\s\+\-\*\/\%\^\(\)\.]+)",
                r"qual (?:o resultado|a resposta) de ([\d\s\+\-\*\/\%\^\(\)\.]+)"
            ],
            "traducao": [
                r"traduza ([\w\s]+) para ([\w]+)",
                r"como se diz ([\w\s]+) em ([\w]+)",
                r"tradução de ([\w\s]+) para ([\w]+)"
            ],
            "noticias": [
                r"quais (?:são|as) (?:últimas|recentes) notícias",
                r"me (?:dê|diga|conte) as notícias",
                r"o que está acontecendo no mundo"
            ],
            "piada": [
                r"conte uma piada",
                r"me faça rir",
                r"sabe alguma piada"
            ],
            "musica": [
                r"cante uma (?:música|canção)",
                r"pode cantar algo",
                r"cante para mim"
            ],
            "jogo": [
                r"jogue um jogo",
                r"vamos jogar",
                r"quero jogar um jogo"
            ],
            "distancia": [
                r"qual (?:a|é) distância (?:até|para|de) ([\w\s]+)",
                r"quanto (?:é|tem) daqui (?:até|para|a) ([\w\s]+)",
                r"como chego (?:até|em|a) ([\w\s]+)"
            ],
            "tempo_viagem": [
                r"quanto tempo (?:para chegar|leva) (?:até|em|a) ([\w\s]+)",
                r"quanto (?:demora|tempo leva) para (?:chegar|ir) (?:até|em|a) ([\w\s]+)"
            ],
            "informacoes": [
                r"(?:informações|me fale|me conte) sobre ([\w\s]+)",
                r"o que você sabe sobre ([\w\s]+)",
                r"quem (?:é|foi|são) ([\w\s]+)"
            ],
            
            # Produtividade e Organização
            "alarme": [
                r"defina um alarme para ([\w\s:]+)",
                r"acorde-me (?:às|as) ([\w\s:]+)",
                r"crie um alarme para ([\w\s:]+)"
            ],
            "timer": [
                r"defina um timer para ([\w\s]+)",
                r"cronômetro de ([\w\s]+)",
                r"conte ([\w\s]+) (?:minutos|segundos|horas)"
            ],
            "lembrete_horario": [
                r"crie um lembrete para ([\w\s]+) (?:às|as) ([\w\s:]+)",
                r"me lembre de ([\w\s]+) (?:às|as) ([\w\s:]+)",
                r"lembrete: ([\w\s]+) (?:às|as) ([\w\s:]+)"
            ],
            "lembrete_local": [
                r"crie um lembrete para ([\w\s]+) quando (?:eu chegar|chegar) (?:em|a|no|na) ([\w\s]+)",
                r"me lembre de ([\w\s]+) quando (?:eu chegar|chegar) (?:em|a|no|na) ([\w\s]+)"
            ],
            "lista_compras_adicionar": [
                r"adicione ([\w\s]+) (?:à|a) (?:minha)? lista de compras",
                r"coloque ([\w\s]+) na (?:minha)? lista de compras",
                r"inclua ([\w\s]+) na (?:minha)? lista de compras"
            ],
            "lista_compras_mostrar": [
                r"mostre (?:minha)? lista de compras",
                r"o que tem na (?:minha)? lista de compras",
                r"veja (?:minha)? lista de compras"
            ],
            "calendario_evento": [
                r"crie um evento (?:no calendário|na agenda) para ([\w\s]+) (?:amanhã|hoje|[\w\s]+) (?:às|as) ([\w\s:]+)",
                r"agende ([\w\s]+) para (?:amanhã|hoje|[\w\s]+) (?:às|as) ([\w\s:]+)"
            ],
            "calendario_consulta": [
                r"o que (?:eu tenho|tem) (?:na minha agenda|no meu calendário) hoje",
                r"quais (?:são meus|os) compromissos (?:para hoje|de hoje)",
                r"mostre (?:minha agenda|meu calendário) (?:de hoje|para hoje)"
            ],
            "anotacao": [
                r"faça uma anotação: ([\w\s]+)",
                r"anote ([\w\s]+)",
                r"note ([\w\s]+)"
            ],
            
            # Comunicação
            "ligar": [
                r"ligue para ([\w\s]+)",
                r"faça uma ligação para ([\w\s]+)",
                r"chame ([\w\s]+)"
            ],
            "mensagem": [
                r"(?:mande|envie) uma mensagem para ([\w\s]+) dizendo ([\w\s]+)",
                r"(?:mande|envie) para ([\w\s]+): ([\w\s]+)",
                r"mensagem para ([\w\s]+): ([\w\s]+)"
            ],
            "ler_mensagens": [
                r"leia (?:minhas|as) mensagens",
                r"tenho (?:alguma|novas) mensagens",
                r"verifique (?:minhas|as) mensagens"
            ],
            "videochamada": [
                r"faça uma videochamada para ([\w\s]+)",
                r"inicie uma chamada de vídeo com ([\w\s]+)",
                r"video para ([\w\s]+)"
            ],
            
            # Música e Mídia
            "tocar_musica": [
                r"toque ([\w\s]+)",
                r"reproduza ([\w\s]+)",
                r"coloque ([\w\s]+) para tocar"
            ],
            "volume": [
                r"(aumente|diminua) o volume",
                r"volume (mais alto|mais baixo)",
                r"(aumente|diminua) o som"
            ],
            "controle_musica": [
                r"(próxima|anterior) música",
                r"(pause|continue) a música",
                r"(pare|retome) a música"
            ],
            "musica_atual": [
                r"que música está tocando",
                r"qual é essa música",
                r"nome dessa música"
            ],
            "audiolivro": [
                r"leia meu audiolivro",
                r"continue meu audiolivro",
                r"reproduza meu audiolivro"
            ],
            
            # Casa Inteligente
            "luzes": [
                r"(acenda|apague) a luz d[ao] ([\w\s]+)",
                r"(ligue|desligue) a luz d[ao] ([\w\s]+)",
                r"(acenda|apague) [ao] ([\w\s]+)"
            ],
            "termostato": [
                r"ajuste o termostato para ([\d]+) graus",
                r"mude a temperatura para ([\d]+) graus",
                r"coloque ([\d]+) graus no ar condicionado"
            ],
            "dispositivo": [
                r"(ligue|desligue) [ao] ([\w\s]+)",
                r"(ative|desative) [ao] ([\w\s]+)"
            ],
            "camera": [
                r"mostre a câmera d[ao] ([\w\s]+)",
                r"veja a câmera d[ao] ([\w\s]+)",
                r"exiba a câmera d[ao] ([\w\s]+)"
            ],
            
            # Controles do Dispositivo
            "brilho": [
                r"(aumente|diminua) o brilho da tela",
                r"(mais|menos) brilho",
                r"brilho (mais alto|mais baixo)"
            ],
            "conectividade": [
                r"(ative|desative) o (Wi-Fi|Bluetooth|Modo Avião)",
                r"(ligue|desligue) o (Wi-Fi|Bluetooth|Modo Avião)"
            ],
            "aplicativo": [
                r"abra o (?:aplicativo|app)? ([\w\s]+)",
                r"inicie o (?:aplicativo|app)? ([\w\s]+)",
                r"execute o (?:aplicativo|app)? ([\w\s]+)"
            ],
            "foto": [
                r"tire uma foto",
                r"fotografe",
                r"capture uma imagem"
            ],
            "video": [
                r"grave um vídeo",
                r"comece a gravar",
                r"inicie gravação"
            ],
            
            # Comandos de Descoberta
            "ajuda": [
                r"o que você pode fazer",
                r"me dê algumas dicas",
                r"quais são seus comandos",
                r"como posso te usar",
                r"me ajude"
            ]
        }
        
        # Respostas pré-definidas para comandos sem integração real
        self.respostas = {
            "hora": [
                f"Agora são {datetime.datetime.now().strftime('%H:%M')}.",
                f"São {datetime.datetime.now().strftime('%H:%M')} no momento.",
                f"O horário atual é {datetime.datetime.now().strftime('%H:%M')}."
            ],
            "data": [
                f"Hoje é {datetime.datetime.now().strftime('%d/%m/%Y')}.",
                f"Estamos em {datetime.datetime.now().strftime('%d de %B de %Y')}.",
                f"A data de hoje é {datetime.datetime.now().strftime('%d/%m/%Y')}."
            ],
            "piada": [
                "Por que o computador foi ao médico? Porque estava com vírus!",
                "O que o zero disse para o oito? Belo cinto!",
                "Por que o livro de matemática está sempre triste? Porque tem muitos problemas.",
                "O que o pato disse para a pata? Vem quá!",
                "Por que a plantinha não podia usar o computador? Porque ela esqueceu a senha-flora."
            ],
            "ajuda": [
                "Posso ajudar com informações, lembretes, controle de dispositivos, reprodução de música e muito mais. Basta dizer 'Brandini' seguido do seu pedido.",
                "Estou aqui para ajudar! Posso responder perguntas, definir alarmes, controlar dispositivos inteligentes, tocar música e muito mais. Experimente perguntar algo específico.",
                "Sou o Assistente Brandini e posso ajudar com várias tarefas. Experimente pedir para definir um lembrete, tocar uma música, contar uma piada ou perguntar sobre o tempo."
            ],
            "foto": [
                "Capturando foto... Pronto!",
                "Foto tirada com sucesso!",
                "Cheese! Foto capturada."
            ],
            "video": [
                "Iniciando gravação de vídeo...",
                "Gravação de vídeo iniciada.",
                "Começando a gravar vídeo agora."
            ],
            "musica": [
                "🎵 Lá, lá, lá... Ops, não sou muito bom em cantar, mas posso tocar música para você!",
                "Não tenho uma boa voz para cantar, mas posso reproduzir suas músicas favoritas!",
                "Prefiro deixar o canto para os profissionais, mas posso tocar música para você!"
            ],
            "jogo": [
                "Vamos jogar um jogo de adivinhação! Estou pensando em um número de 1 a 10. Tente adivinhar!",
                "Que tal jogarmos pedra, papel ou tesoura? Você começa!",
                "Posso jogar um jogo de perguntas e respostas com você. Quer começar?"
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
        
        # Remover a palavra de ativação "Brandini" se presente
        text = re.sub(r'^brandini[,\s]*', '', text)
        
        # Verificar cada categoria de padrão
        for category, patterns in self.command_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, text)
                if match:
                    # Extrair parâmetros (se houver)
                    params = match.groups() if match.groups() else []
                    return self._generate_response(category, params, text)
        
        # Se nenhum padrão específico for encontrado, tentar busca na base de conhecimento
        if self.knowledge_base:
            # Tentar processar com o processador de comandos da base de conhecimento
            from modules.command_processor import CommandProcessor
            processor = CommandProcessor()
            response = processor.process_command(text)
            
            # Se a resposta não for genérica, retorná-la
            if not response.startswith("Não tenho"):
                return response
        
        # Fallback para respostas genéricas
        return self._fallback_response(text)
    
    def _generate_response(self, category, params, original_text):
        """
        Gera uma resposta com base na categoria e parâmetros identificados
        
        Args:
            category (str): Categoria do comando
            params (list): Parâmetros extraídos do comando
            original_text (str): Texto original do comando
            
        Returns:
            str: Resposta gerada
        """
        # Respostas para categorias com respostas pré-definidas
        if category in self.respostas:
            return random.choice(self.respostas[category])
        
        # Respostas para categorias específicas
        if category == "tempo":
            local = params[0] if params else "hoje"
            return f"A previsão do tempo para {local} indica temperatura agradável com possibilidade de variações. Para informações mais precisas, posso verificar um serviço de meteorologia específico."
        
        elif category == "calculo":
            try:
                expressao = params[0] if params else ""
                # Substituir 'x' por '*' para multiplicação
                expressao = expressao.replace('x', '*').replace('X', '*')
                resultado = eval(expressao)
                return f"O resultado de {expressao} é {resultado}."
            except:
                return "Desculpe, não consegui calcular essa expressão."
        
        elif category == "definicao":
            termo = params[0] if params else ""
            return f"A definição de '{termo}' não está disponível no momento. Posso buscar isso para você em uma fonte confiável."
        
        elif category == "traducao":
            texto = params[0] if len(params) > 0 else ""
            idioma = params[1] if len(params) > 1 else ""
            return f"A tradução de '{texto}' para {idioma} não está disponível no momento. Posso buscar isso para você em um serviço de tradução."
        
        elif category == "noticias":
            return "As notícias mais recentes incluem atualizações sobre política, economia, esportes e entretenimento. Posso buscar notícias específicas sobre algum tópico de seu interesse."
        
        elif category == "distancia" or category == "tempo_viagem":
            destino = params[0] if params else ""
            if category == "distancia":
                return f"A distância até {destino} depende da sua localização atual. Posso calcular isso para você com acesso à sua localização."
            else:
                return f"O tempo de viagem até {destino} depende da sua localização atual e do meio de transporte. Posso calcular isso para você com mais informações."
        
        elif category == "informacoes":
            topico = params[0] if params else ""
            # Tentar buscar na base de conhecimento se disponível
            if self.knowledge_base:
                resultados = self.knowledge_base.buscar_em_todas_categorias(topico)
                if resultados:
                    # Encontrou algo relacionado
                    categories = list(resultados.keys())
                    if len(categories) == 1:
                        category = categories[0]
                        items = resultados[category]
                        if len(items) == 1:
                            # Encontrou um único item
                            item = items[0]
                            info = self.knowledge_base.obter_informacao(category, item)
                            return self.knowledge_base.formatar_resposta(info, 'resumido')
            
            return f"Aqui estão algumas informações sobre {topico}. Para detalhes mais específicos, posso buscar em fontes confiáveis."
        
        elif category == "alarme":
            horario = params[0] if params else ""
            return f"Alarme definido para {horario}."
        
        elif category == "timer":
            duracao = params[0] if params else ""
            return f"Timer definido para {duracao}."
        
        elif category == "lembrete_horario":
            tarefa = params[0] if len(params) > 0 else ""
            horario = params[1] if len(params) > 1 else ""
            return f"Lembrete criado: {tarefa} às {horario}."
        
        elif category == "lembrete_local":
            tarefa = params[0] if len(params) > 0 else ""
            local = params[1] if len(params) > 1 else ""
            return f"Lembrete baseado em localização criado: {tarefa} quando chegar em {local}."
        
        elif category == "lista_compras_adicionar":
            item = params[0] if params else ""
            return f"{item} adicionado à sua lista de compras."
        
        elif category == "lista_compras_mostrar":
            return "Sua lista de compras está vazia ou não está disponível no momento."
        
        elif category == "calendario_evento":
            evento = params[0] if len(params) > 0 else ""
            horario = params[1] if len(params) > 1 else ""
            return f"Evento adicionado ao calendário: {evento} às {horario}."
        
        elif category == "calendario_consulta":
            return "Você não tem compromissos agendados para hoje ou seu calendário não está disponível no momento."
        
        elif category == "anotacao":
            texto = params[0] if params else ""
            return f"Anotação salva: {texto}"
        
        elif category == "ligar":
            contato = params[0] if params else ""
            return f"Ligando para {contato}..."
        
        elif category == "mensagem":
            contato = params[0] if len(params) > 0 else ""
            mensagem = params[1] if len(params) > 1 else ""
            return f"Mensagem enviada para {contato}: '{mensagem}'"
        
        elif category == "ler_mensagens":
            return "Você não tem novas mensagens ou suas mensagens não estão disponíveis no momento."
        
        elif category == "videochamada":
            contato = params[0] if params else ""
            return f"Iniciando videochamada com {contato}..."
        
        elif category == "tocar_musica":
            musica = params[0] if params else ""
            return f"Tocando {musica}..."
        
        elif category == "volume":
            acao = params[0] if params else ""
            return f"Volume {acao}."
        
        elif category == "controle_musica":
            acao = params[0] if params else ""
            return f"Música {acao}."
        
        elif category == "musica_atual":
            return "Nenhuma música está tocando no momento."
        
        elif category == "audiolivro":
            return "Continuando a reprodução do seu audiolivro..."
        
        elif category == "luzes":
            acao = params[0] if len(params) > 0 else ""
            local = params[1] if len(params) > 1 else ""
            return f"Luzes {acao}s na {local}."
        
        elif category == "termostato":
            temperatura = params[0] if params else ""
            return f"Termostato ajustado para {temperatura} graus."
        
        elif category == "dispositivo":
            acao = params[0] if len(params) > 0 else ""
            dispositivo = params[1] if len(params) > 1 else ""
            return f"{dispositivo} {acao}."
        
        elif category == "camera":
            local = params[0] if params else ""
            return f"Exibindo câmera da {local}..."
        
        elif category == "brilho":
            acao = params[0] if params else ""
            return f"Brilho da tela {acao}."
        
        elif category == "conectividade":
            acao = params[0] if len(params) > 0 else ""
            recurso = params[1] if len(params) > 1 else ""
            return f"{recurso} {acao}."
        
        elif category == "aplicativo":
            app = params[0] if params else ""
            return f"Abrindo {app}..."
        
        # Fallback para categorias não tratadas especificamente
        return f"Comando reconhecido na categoria '{category}', mas ainda não implementado completamente."
    
    def _fallback_response(self, text):
        """
        Gera uma resposta para comandos que não correspondem a padrões específicos
        
        Args:
            text (str): Texto original do comando
            
        Returns:
            str: Resposta gerada
        """
        # Respostas genéricas quando nada é encontrado
        generic_responses = [
            "Não entendi completamente o que você pediu. Pode reformular de outra maneira?",
            "Não tenho certeza do que você está pedindo. Pode ser mais específico?",
            "Desculpe, não consegui processar esse comando. Tente algo como 'Brandini, que horas são?' ou 'Brandini, defina um alarme para 8h'.",
            "Não reconheci esse comando. Diga 'Brandini, o que você pode fazer?' para ver algumas sugestões."
        ]
        return random.choice(generic_responses)

# Exemplo de uso
if __name__ == "__main__":
    processor = GeneralCommandProcessor()
    
    # Testar alguns comandos
    commands = [
        "Que horas são?",
        "Defina um alarme para 8h da manhã",
        "Conte uma piada",
        "Qual a previsão do tempo para hoje?",
        "Toque música relaxante",
        "Quanto é 15% de 200?",
        "O que você pode fazer?"
    ]
    
    for cmd in commands:
        print(f"\nComando: {cmd}")
        response = processor.process_command(cmd)
        print(f"Resposta: {response}")
