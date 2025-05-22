"""
Módulo de base de conhecimento para o Assistente Brandini
Contém informações sobre assistentes virtuais, LLMs, IAs e chatbots
"""

class KnowledgeBase:
    """Base de conhecimento com informações sobre tecnologias de IA"""
    
    def __init__(self):
        """Inicializa a base de conhecimento"""
        # Dicionário com informações sobre assistentes virtuais
        self.assistentes_virtuais = {
            "siri": {
                "nome": "Siri",
                "empresa": "Apple",
                "dispositivos": ["iPhone", "iPad", "Mac", "Apple Watch", "HomePod"],
                "descricao": "Assistente virtual da Apple lançado em 2011, integrado a todos os dispositivos da empresa. Responde a comandos de voz, realiza tarefas como enviar mensagens, fazer ligações, definir lembretes e controlar dispositivos domésticos inteligentes.",
                "recursos": ["Controle de casa inteligente", "Respostas a perguntas", "Envio de mensagens", "Chamadas telefônicas", "Lembretes e alarmes", "Reprodução de música"],
                "idiomas": ["Português", "Inglês", "Espanhol", "Francês", "Alemão", "Japonês", "Chinês", "entre outros"]
            },
            "alexa": {
                "nome": "Alexa",
                "empresa": "Amazon",
                "dispositivos": ["Echo", "Echo Dot", "Echo Show", "Fire TV", "dispositivos de terceiros"],
                "descricao": "Assistente virtual da Amazon lançado em 2014, inicialmente para os alto-falantes inteligentes Echo. Destaca-se pelo controle de casa inteligente e integração com o ecossistema de serviços da Amazon, como compras online e streaming de música.",
                "recursos": ["Controle de casa inteligente", "Compras na Amazon", "Reprodução de música", "Notícias e previsão do tempo", "Jogos e entretenimento", "Chamadas e mensagens"],
                "idiomas": ["Português", "Inglês", "Espanhol", "Francês", "Alemão", "Italiano", "Japonês", "entre outros"]
            },
            "google assistente": {
                "nome": "Google Assistente",
                "empresa": "Google",
                "dispositivos": ["Smartphones Android", "Google Home/Nest", "Smart TVs", "Chromebooks", "Dispositivos iOS"],
                "descricao": "Assistente virtual do Google lançado em 2016, conhecido por sua capacidade de responder perguntas complexas e integração com os serviços Google. Utiliza o poder de busca do Google e inteligência artificial avançada para fornecer respostas contextuais.",
                "recursos": ["Pesquisa na web", "Controle de casa inteligente", "Tradução em tempo real", "Agendamento de compromissos", "Navegação e mapas", "Reprodução de mídia"],
                "idiomas": ["Português", "Inglês", "Espanhol", "Francês", "Alemão", "Japonês", "Hindi", "entre outros"]
            },
            "cortana": {
                "nome": "Cortana",
                "empresa": "Microsoft",
                "dispositivos": ["Windows 10/11", "Aplicativos Microsoft 365", "Anteriormente em Xbox e smartphones"],
                "descricao": "Assistente virtual da Microsoft lançado em 2014, inicialmente para Windows Phone e posteriormente para Windows 10. Embora sua presença tenha diminuído em produtos de consumo, ainda é utilizada em contextos empresariais e serviços Microsoft.",
                "recursos": ["Integração com Microsoft 365", "Lembretes e calendário", "Pesquisa no Windows", "Gerenciamento de e-mails", "Configurações do sistema"],
                "idiomas": ["Inglês", "Português", "Espanhol", "Francês", "Alemão", "Italiano", "Chinês", "Japonês"]
            },
            "bixby": {
                "nome": "Bixby",
                "empresa": "Samsung",
                "dispositivos": ["Smartphones Galaxy", "Smart TVs Samsung", "Eletrodomésticos Samsung"],
                "descricao": "Assistente virtual da Samsung lançado em 2017, projetado para facilitar o uso de dispositivos Samsung através de comandos de voz. Foca na automação de tarefas dentro do ecossistema Samsung.",
                "recursos": ["Controle de dispositivos Samsung", "Bixby Vision (reconhecimento visual)", "Bixby Routines (automação)", "Tradução", "Pesquisa de informações"],
                "idiomas": ["Inglês", "Coreano", "Chinês", "Espanhol", "Alemão", "Italiano", "Francês"]
            },
            "alice": {
                "nome": "Alice",
                "empresa": "Artificial Linguistic Internet Computer Entity",
                "dispositivos": ["Software para computadores"],
                "descricao": "Um dos primeiros chatbots de processamento de linguagem natural, criado por Richard Wallace em 1995. Alice (Artificial Linguistic Internet Computer Entity) foi pioneira no uso de AIML (Artificial Intelligence Markup Language) para simular conversas.",
                "recursos": ["Conversação básica", "Respostas pré-programadas", "Reconhecimento de padrões de linguagem"],
                "idiomas": ["Principalmente inglês"]
            },
            "android auto": {
                "nome": "Android Auto",
                "empresa": "Google",
                "dispositivos": ["Sistemas de infotainment de veículos compatíveis", "Smartphones Android"],
                "descricao": "Interface de usuário projetada para veículos, que permite acesso a funções do smartphone Android enquanto dirige. Integra-se com o Google Assistente para comandos de voz, minimizando distrações.",
                "recursos": ["Navegação com Google Maps", "Reprodução de música", "Mensagens de texto por voz", "Chamadas telefônicas", "Acesso a aplicativos compatíveis"],
                "idiomas": ["Suporta os mesmos idiomas do Google Assistente"]
            },
            "carplay": {
                "nome": "CarPlay",
                "empresa": "Apple",
                "dispositivos": ["Sistemas de infotainment de veículos compatíveis", "iPhone"],
                "descricao": "Interface da Apple para veículos, permitindo que motoristas usem aplicativos do iPhone de forma segura enquanto dirigem. Integra-se com a Siri para comandos de voz.",
                "recursos": ["Navegação com Apple Maps", "Reprodução de música", "Mensagens de texto por voz", "Chamadas telefônicas", "Acesso a aplicativos compatíveis"],
                "idiomas": ["Suporta os mesmos idiomas da Siri"]
            }
        }
        
        # Dicionário com informações sobre LLMs (Large Language Models)
        self.llms = {
            "gemini": {
                "nome": "Gemini",
                "empresa": "Google",
                "lançamento": "2023",
                "descricao": "Modelo multimodal avançado do Google, sucessor do PaLM. Disponível em diferentes tamanhos (Ultra, Pro e Nano) e capaz de processar texto, imagens, áudio e vídeo simultaneamente.",
                "capacidades": ["Compreensão multimodal", "Raciocínio complexo", "Geração de código", "Análise de imagens e vídeos", "Respostas contextuais"],
                "acesso": ["API Google AI Studio", "Aplicativo Gemini", "Integrado ao Google Workspace"]
            },
            "chatgpt": {
                "nome": "ChatGPT",
                "empresa": "OpenAI",
                "lançamento": "2022",
                "descricao": "Um dos LLMs mais populares, baseado na arquitetura GPT (Generative Pre-trained Transformer). Conhecido por sua capacidade de gerar texto semelhante ao humano e manter conversas contextuais.",
                "capacidades": ["Conversação natural", "Escrita criativa", "Resumo de textos", "Tradução", "Explicação de conceitos complexos", "Geração de código"],
                "acesso": ["Site ChatGPT", "API OpenAI", "Aplicativos móveis", "Plugins e integrações"]
            },
            "deepseek": {
                "nome": "DeepSeek",
                "empresa": "DeepSeek AI",
                "lançamento": "2023",
                "descricao": "Série de modelos de linguagem desenvolvidos pela DeepSeek AI, incluindo versões especializadas em código e raciocínio matemático.",
                "capacidades": ["Programação avançada", "Raciocínio matemático", "Compreensão de texto", "Geração de conteúdo"],
                "acesso": ["API", "Modelos de código aberto disponíveis no Hugging Face"]
            },
            "claude": {
                "nome": "Claude",
                "empresa": "Anthropic",
                "lançamento": "2022",
                "descricao": "LLM desenvolvido pela Anthropic com foco em segurança, utilidade e harmlessness. Projetado para ser útil, inofensivo e honesto em suas respostas.",
                "capacidades": ["Conversação natural", "Análise de documentos longos", "Resumo de textos", "Escrita criativa", "Respostas éticas e seguras"],
                "acesso": ["Site Claude.ai", "API Anthropic", "Integrações com plataformas como Slack"]
            },
            "llama": {
                "nome": "Llama",
                "empresa": "Meta",
                "lançamento": "2023",
                "descricao": "Família de LLMs de código aberto desenvolvida pela Meta (anteriormente Facebook). Disponível em diferentes tamanhos e versões, com Llama 2 e Llama 3 sendo as mais recentes.",
                "capacidades": ["Geração de texto", "Compreensão contextual", "Raciocínio", "Tradução", "Resumo"],
                "acesso": ["Download dos pesos do modelo", "Hugging Face", "Implementações de terceiros"]
            },
            "gpt-4": {
                "nome": "GPT-4",
                "empresa": "OpenAI",
                "lançamento": "2023",
                "descricao": "A versão mais avançada da série GPT da OpenAI, com capacidades multimodais (texto e imagem) e raciocínio significativamente melhorado em relação às versões anteriores.",
                "capacidades": ["Compreensão de imagens", "Raciocínio complexo", "Geração de código avançada", "Maior precisão factual", "Contexto estendido"],
                "acesso": ["ChatGPT Plus", "API OpenAI", "Integrações em produtos Microsoft"]
            },
            "palm": {
                "nome": "PaLM",
                "empresa": "Google",
                "lançamento": "2022",
                "descricao": "Pathways Language Model, precursor do Gemini. Um modelo de linguagem de grande escala treinado usando a arquitetura Pathways do Google, que permite treinamento em múltiplos tipos de dados.",
                "capacidades": ["Raciocínio de múltiplos passos", "Tradução", "Geração de código", "Respostas a perguntas"],
                "acesso": ["Anteriormente disponível via API PaLM", "Substituído pelo Gemini"]
            }
        }
        
        # Dicionário com informações sobre outras IAs notáveis
        self.outras_ias = {
            "alphago": {
                "nome": "AlphaGo/AlphaZero",
                "empresa": "DeepMind/Google",
                "tipo": "IA para jogos",
                "descricao": "Sistema de IA que demonstrou maestria em jogos de tabuleiro como Go e xadrez. AlphaGo foi a primeira IA a derrotar um campeão mundial de Go, enquanto AlphaZero aprendeu a jogar xadrez, Go e shogi em nível sobre-humano apenas jogando contra si mesma.",
                "conquistas": ["Derrotou o campeão mundial de Go Lee Sedol em 2016", "AlphaZero aprendeu xadrez em apenas 4 horas e superou os melhores programas existentes"]
            },
            "dall-e": {
                "nome": "DALL-E",
                "empresa": "OpenAI",
                "tipo": "IA de geração de imagens",
                "descricao": "Modelo de IA que gera imagens a partir de descrições textuais. DALL-E 2 e DALL-E 3 são versões mais avançadas com maior qualidade e precisão na geração de imagens.",
                "capacidades": ["Criação de imagens realistas", "Edição e variações de imagens", "Compreensão de conceitos abstratos", "Combinação de elementos díspares"]
            },
            "midjourney": {
                "nome": "Midjourney",
                "empresa": "Midjourney, Inc.",
                "tipo": "IA de geração de imagens",
                "descricao": "Ferramenta de IA que cria imagens a partir de descrições textuais, conhecida por seu estilo artístico distintivo e alta qualidade estética.",
                "capacidades": ["Geração de arte digital", "Ilustrações detalhadas", "Estilos artísticos variados", "Renderizações fotorrealistas"]
            },
            "carros_autonomos": {
                "nome": "IAs para Carros Autônomos",
                "empresas": ["Tesla (Autopilot/FSD)", "Waymo (Google)", "Cruise (GM)", "Mobileye (Intel)"],
                "tipo": "IA para veículos",
                "descricao": "Sistemas de inteligência artificial que permitem que veículos naveguem e tomem decisões sem intervenção humana, usando uma combinação de visão computacional, aprendizado profundo e sensores.",
                "tecnologias": ["Visão computacional", "Detecção de objetos", "Planejamento de rotas", "Tomada de decisões em tempo real"]
            },
            "ia_medicina": {
                "nome": "IAs para Diagnóstico Médico",
                "exemplos": ["IBM Watson Health", "Google Health", "Aidoc", "Zebra Medical Vision"],
                "tipo": "IA para saúde",
                "descricao": "Sistemas de IA aplicados à medicina para auxiliar no diagnóstico, análise de imagens médicas, descoberta de medicamentos e personalização de tratamentos.",
                "aplicações": ["Detecção de câncer em imagens", "Análise de registros médicos", "Previsão de surtos de doenças", "Descoberta de medicamentos"]
            },
            "sistemas_recomendacao": {
                "nome": "IAs para Sistemas de Recomendação",
                "exemplos": ["Netflix", "Amazon", "Spotify", "YouTube"],
                "tipo": "IA para personalização",
                "descricao": "Algoritmos que analisam comportamentos e preferências dos usuários para recomendar produtos, conteúdos ou serviços relevantes.",
                "técnicas": ["Filtragem colaborativa", "Filtragem baseada em conteúdo", "Modelos de deep learning", "Análise de sequência temporal"]
            }
        }
        
        # Dicionário com informações sobre chatbots
        self.chatbots = {
            "llm_chatbots": {
                "nome": "Chatbots baseados em LLMs",
                "exemplos": ["ChatGPT", "Gemini (Bard)", "Claude", "Microsoft Copilot", "Perplexity AI", "YouChat", "HuggingChat"],
                "descricao": "Chatbots avançados que utilizam modelos de linguagem grandes para gerar respostas contextuais e naturais, capazes de manter conversas complexas.",
                "capacidades": ["Conversação natural", "Respostas contextuais", "Memória de conversa", "Geração de conteúdo", "Respostas a perguntas complexas"]
            },
            "perplexity": {
                "nome": "Perplexity AI",
                "empresa": "Perplexity Labs",
                "tipo": "Chatbot de pesquisa",
                "descricao": "Motor de busca conversacional que combina capacidades de LLMs com pesquisa na web em tempo real para fornecer respostas atualizadas e com citação de fontes.",
                "recursos": ["Citação de fontes", "Informações atualizadas", "Pesquisa em tempo real", "Modo de conversação", "Compartilhamento de respostas"]
            },
            "copilot": {
                "nome": "Microsoft Copilot",
                "empresa": "Microsoft",
                "tipo": "Assistente de IA",
                "descricao": "Anteriormente conhecido como Bing Chat, é um assistente de IA da Microsoft que combina capacidades de busca com modelos de linguagem da OpenAI, integrado ao Windows, Edge e aplicativos Microsoft 365.",
                "recursos": ["Pesquisa na web", "Criação de conteúdo", "Integração com Windows", "Assistência em aplicativos Office", "Geração de imagens"]
            },
            "atendimento_cliente": {
                "nome": "Chatbots para Atendimento ao Cliente",
                "exemplos": ["Zendesk", "Intercom", "Drift", "JivoChat", "Landbot", "Blip"],
                "descricao": "Chatbots especializados em automatizar o atendimento ao cliente, responder perguntas frequentes e encaminhar casos complexos para atendentes humanos.",
                "recursos": ["Respostas automáticas", "Transferência para humanos", "Integração com CRM", "Análise de sentimento", "Automação de processos"]
            },
            "whatsapp_chatbots": {
                "nome": "Chatbots para WhatsApp",
                "plataformas": ["WhatsApp Business API", "Twilio", "MessageBird", "Take Blip", "Zenvia"],
                "descricao": "Chatbots desenvolvidos especificamente para a plataforma WhatsApp, permitindo que empresas automatizem comunicações com clientes através do aplicativo de mensagens mais popular do mundo.",
                "casos_uso": ["Atendimento ao cliente", "Notificações", "Vendas", "Agendamentos", "Pesquisas de satisfação"]
            }
        }
        
        # Dicionário com comparações entre tecnologias
        self.comparacoes = {
            "assistentes_populares": {
                "titulo": "Comparação entre Siri, Alexa e Google Assistente",
                "siri": {
                    "pontos_fortes": ["Integração com ecossistema Apple", "Privacidade", "Controle de dispositivos Apple"],
                    "pontos_fracos": ["Conhecimento geral mais limitado", "Menos dispositivos compatíveis", "Menos habilidades de terceiros"]
                },
                "alexa": {
                    "pontos_fortes": ["Maior número de skills", "Excelente para compras online", "Ampla compatibilidade com dispositivos"],
                    "pontos_fracos": ["Menos natural em conversas", "Questões de privacidade", "Menos integração com smartphones"]
                },
                "google_assistente": {
                    "pontos_fortes": ["Melhor em conhecimento geral", "Reconhecimento de voz superior", "Integração com serviços Google"],
                    "pontos_fracos": ["Questões de privacidade", "Menos foco em compras", "Experiência fragmentada entre dispositivos"]
                },
                "conclusao": "A escolha entre esses assistentes depende principalmente do ecossistema de dispositivos que você já possui e dos serviços que mais utiliza. Siri é ideal para usuários Apple, Alexa para quem prioriza casa inteligente e compras, e Google Assistente para quem valoriza conhecimento geral e usa serviços Google."
            },
            "chatgpt_vs_claude": {
                "titulo": "Diferenças entre ChatGPT e Claude",
                "chatgpt": {
                    "pontos_fortes": ["Mais versátil", "Melhor em programação", "Maior base de conhecimento", "Mais integrações"],
                    "pontos_fracos": ["Pode 'alucinar' fatos", "Menos transparente sobre limitações", "Restrições de uso em alguns casos"]
                },
                "claude": {
                    "pontos_fortes": ["Melhor em seguir instruções", "Mais transparente sobre limitações", "Processamento de documentos longos", "Foco em respostas seguras"],
                    "pontos_fracos": ["Base de conhecimento menor", "Menos recursos avançados", "Menos integrações disponíveis"]
                },
                "conclusao": "ChatGPT tende a ser mais versátil e tem mais recursos, enquanto Claude se destaca em seguir instruções precisas e lidar com textos longos. Claude também tende a ser mais cauteloso e transparente sobre suas limitações."
            },
            "assistentes_vs_chatbots": {
                "titulo": "Assistentes Virtuais vs. Chatbots",
                "assistentes_virtuais": {
                    "características": ["Multimodais (voz, texto, imagem)", "Controle de dispositivos", "Execução de ações no mundo real", "Personalidade consistente", "Presença contínua"],
                    "exemplos": ["Siri", "Alexa", "Google Assistente"]
                },
                "chatbots": {
                    "características": ["Principalmente baseados em texto", "Focados em conversação", "Geralmente limitados a um canal", "Podem ser mais especializados", "Interação por demanda"],
                    "exemplos": ["Chatbots de atendimento", "ChatGPT web", "Assistentes de sites"]
                },
                "conclusao": "Assistentes virtuais são mais abrangentes e multimodais, projetados para serem companheiros digitais contínuos, enquanto chatbots tendem a ser mais focados em tarefas específicas e geralmente limitados a interfaces de texto."
            },
            "llms_codigo_aberto": {
                "titulo": "Melhores LLMs de Código Aberto",
                "modelos": {
                    "llama": {
                        "pontos_fortes": ["Desempenho próximo a modelos proprietários", "Várias versões e tamanhos", "Grande comunidade", "Licença permissiva para uso comercial"],
                        "limitações": ["Requer hardware potente", "Instalação complexa para iniciantes"]
                    },
                    "mistral": {
                        "pontos_fortes": ["Excelente desempenho em tamanho pequeno", "Eficiente em recursos", "Bom para fine-tuning"],
                        "limitações": ["Base de conhecimento menor que modelos maiores"]
                    },
                    "falcon": {
                        "pontos_fortes": ["Bom equilíbrio entre tamanho e desempenho", "Treinado com dados diversos"],
                        "limitações": ["Menos suporte da comunidade que Llama"]
                    },
                    "mpt": {
                        "pontos_fortes": ["Arquitetura otimizada", "Variantes especializadas disponíveis"],
                        "limitações": ["Menos popular que outras opções"]
                    }
                },
                "conclusao": "Llama (Meta) é atualmente o LLM de código aberto mais popular e versátil, com melhor desempenho geral, enquanto Mistral oferece excelente eficiência para modelos menores. A escolha depende do caso de uso, recursos computacionais disponíveis e necessidades específicas."
            },
            "assistentes_em_portugues": {
                "titulo": "Assistentes Virtuais em Português",
                "avaliacao": {
                    "google_assistente": {
                        "qualidade": "Excelente",
                        "pontos_fortes": ["Melhor compreensão de sotaques brasileiros", "Conhecimento local", "Respostas naturais em português"],
                        "limitações": ["Algumas funções avançadas só em inglês"]
                    },
                    "alexa": {
                        "qualidade": "Muito boa",
                        "pontos_fortes": ["Boa integração com serviços brasileiros", "Habilidades locais", "Compreensão de comandos naturais"],
                        "limitações": ["Ocasionalmente confunde termos similares"]
                    },
                    "siri": {
                        "qualidade": "Boa",
                        "pontos_fortes": ["Integração com serviços Apple", "Comandos básicos funcionam bem"],
                        "limitações": ["Menos recursos em português que em inglês", "Compreensão de contexto mais limitada"]
                    }
                },
                "conclusao": "O Google Assistente geralmente oferece a melhor experiência em português brasileiro, seguido de perto pela Alexa. A Siri funciona bem para comandos básicos, mas tem menos recursos localizados para o Brasil."
            }
        }
        
        # Dicionário com guias práticos
        self.guias_praticos = {
            "configurar_assistente_casa": {
                "titulo": "Como Configurar um Assistente Virtual em Casa",
                "passos": [
                    "Escolha o assistente adequado ao seu ecossistema (Alexa, Google Assistente, Siri)",
                    "Adquira um alto-falante inteligente compatível",
                    "Baixe o aplicativo correspondente no smartphone",
                    "Conecte o dispositivo à sua rede Wi-Fi",
                    "Faça login com sua conta (Amazon, Google ou Apple)",
                    "Configure preferências de voz, localização e serviços",
                    "Conecte serviços de streaming e outros aplicativos",
                    "Adicione dispositivos inteligentes compatíveis"
                ],
                "dicas": [
                    "Posicione o alto-falante em local central e livre de obstáculos",
                    "Configure rotinas para automatizar tarefas frequentes",
                    "Revise configurações de privacidade regularmente",
                    "Atualize o firmware do dispositivo quando disponível"
                ]
            },
            "comandos_alexa": {
                "titulo": "Comandos Básicos da Alexa",
                "categorias": {
                    "informações": [
                        "Alexa, que horas são?",
                        "Alexa, como está o tempo?",
                        "Alexa, quais são as notícias de hoje?",
                        "Alexa, quanto é [cálculo matemático]?"
                    ],
                    "entretenimento": [
                        "Alexa, toque [música/artista/playlist]",
                        "Alexa, conte uma piada",
                        "Alexa, conte uma história",
                        "Alexa, jogue [nome do jogo]"
                    ],
                    "casa_inteligente": [
                        "Alexa, ligue/desligue [dispositivo]",
                        "Alexa, aumente/diminua [dispositivo]",
                        "Alexa, defina [dispositivo] para [valor]",
                        "Alexa, ative a rotina [nome da rotina]"
                    ],
                    "produtividade": [
                        "Alexa, adicione [item] à minha lista de compras",
                        "Alexa, defina um alarme para [horário]",
                        "Alexa, defina um lembrete para [tarefa] às [horário]",
                        "Alexa, qual é a minha agenda para hoje?"
                    ]
                }
            },
            "usar_llms_estudar": {
                "titulo": "Como Usar LLMs para Estudar",
                "estratégias": [
                    {
                        "nome": "Explicações personalizadas",
                        "descrição": "Peça ao LLM para explicar conceitos complexos de forma adaptada ao seu nível de conhecimento",
                        "exemplo": "Explique o teorema de Pitágoras como se eu fosse um estudante do 7º ano"
                    },
                    {
                        "nome": "Questionamento socrático",
                        "descrição": "Use o LLM para fazer perguntas que aprofundem seu entendimento",
                        "exemplo": "Faça-me 5 perguntas sobre fotossíntese que me ajudem a entender melhor o processo"
                    },
                    {
                        "nome": "Resumos e sínteses",
                        "descrição": "Peça ao LLM para resumir textos longos ou sintetizar múltiplas fontes",
                        "exemplo": "Resuma os principais argumentos deste artigo científico em linguagem simples"
                    },
                    {
                        "nome": "Preparação para provas",
                        "descrição": "Use o LLM para criar questões de prática e simulados",
                        "exemplo": "Crie 10 questões de múltipla escolha sobre História do Brasil no século XIX"
                    },
                    {
                        "nome": "Verificação de entendimento",
                        "descrição": "Explique conceitos para o LLM e peça feedback",
                        "exemplo": "Verifique se minha explicação sobre mitose está correta e complete o que estiver faltando"
                    }
                ],
                "cuidados": [
                    "Verifique as informações com fontes confiáveis",
                    "Use LLMs como complemento, não substituto para materiais didáticos",
                    "Pratique ativamente, não apenas leia passivamente as respostas",
                    "Desenvolva pensamento crítico sobre as respostas geradas"
                ]
            },
            "privacidade_assistentes": {
                "titulo": "Assistentes Virtuais e Privacidade",
                "comparativo": {
                    "apple_siri": {
                        "nível_privacidade": "Alto",
                        "práticas": ["Processamento local de muitos comandos", "Não associa dados a identidade do usuário", "Gravações anônimas", "Opt-in para análise de áudio"],
                        "configurações": ["Desativar 'Ouvir Hey Siri'", "Excluir histórico de Siri", "Desativar Siri quando o dispositivo estiver bloqueado"]
                    },
                    "amazon_alexa": {
                        "nível_privacidade": "Médio",
                        "práticas": ["Armazena gravações em servidores", "Permite exclusão manual", "Usa dados para melhorar serviços"],
                        "configurações": ["Excluir gravações de voz", "Desativar uso de gravações para desenvolvimento", "Usar modo de privacidade"]
                    },
                    "google_assistente": {
                        "nível_privacidade": "Médio-baixo",
                        "práticas": ["Integração com perfil Google", "Armazenamento de interações", "Personalização baseada em histórico"],
                        "configurações": ["Pausar histórico de atividades", "Excluir interações automaticamente", "Desativar resultados personalizados"]
                    }
                },
                "recomendações": [
                    "Revise e exclua seu histórico regularmente",
                    "Desative microfones quando não estiver usando",
                    "Use configurações de privacidade mais restritivas",
                    "Considere alternativas offline para funções sensíveis",
                    "Leia as políticas de privacidade antes de usar novos recursos"
                ]
            },
            "integrar_chatbots_site": {
                "titulo": "Como Integrar Chatbots em um Site",
                "opções": {
                    "plataformas_prontas": {
                        "descrição": "Serviços que oferecem chatbots pré-configurados com interface visual",
                        "exemplos": ["Tidio", "Tawk.to", "Intercom", "Zendesk", "Drift"],
                        "vantagens": ["Fácil implementação", "Sem necessidade de programação", "Recursos prontos"],
                        "desvantagens": ["Personalização limitada", "Custos recorrentes", "Dependência de terceiros"]
                    },
                    "frameworks_desenvolvimento": {
                        "descrição": "Bibliotecas e frameworks para criar chatbots personalizados",
                        "exemplos": ["Botpress", "Rasa", "Microsoft Bot Framework", "Dialogflow"],
                        "vantagens": ["Alta personalização", "Controle total", "Integração com sistemas existentes"],
                        "desvantagens": ["Requer conhecimento técnico", "Desenvolvimento mais demorado", "Manutenção necessária"]
                    },
                    "apis_llm": {
                        "descrição": "Integração direta com APIs de modelos de linguagem",
                        "exemplos": ["OpenAI API", "Google Gemini API", "Anthropic Claude API", "Hugging Face Inference API"],
                        "vantagens": ["Respostas avançadas", "Flexibilidade", "Capacidades conversacionais superiores"],
                        "desvantagens": ["Custos baseados em uso", "Complexidade de implementação", "Latência potencial"]
                    }
                },
                "passos_básicos": [
                    "Defina os objetivos do chatbot (suporte, vendas, FAQ, etc.)",
                    "Escolha a plataforma ou tecnologia adequada",
                    "Projete o fluxo de conversação e respostas",
                    "Implemente o código de integração no site",
                    "Teste extensivamente com diferentes cenários",
                    "Colete feedback e refine continuamente",
                    "Monitore desempenho e satisfação dos usuários"
                ]
            }
        }
    
    def obter_informacao(self, categoria, termo, tipo_info=None):
        """
        Obtém informações sobre um termo específico em uma categoria
        
        Args:
            categoria (str): Categoria da informação ('assistentes_virtuais', 'llms', 'outras_ias', 'chatbots', 'comparacoes', 'guias_praticos')
            termo (str): Termo específico a ser buscado
            tipo_info (str, opcional): Tipo específico de informação desejada
            
        Returns:
            dict/str: Informações solicitadas ou mensagem de erro
        """
        # Normalizar termo para busca (minúsculas, sem acentos)
        termo_norm = termo.lower().strip()
        
        # Selecionar dicionário apropriado
        if categoria == 'assistentes_virtuais':
            dicionario = self.assistentes_virtuais
        elif categoria == 'llms':
            dicionario = self.llms
        elif categoria == 'outras_ias':
            dicionario = self.outras_ias
        elif categoria == 'chatbots':
            dicionario = self.chatbots
        elif categoria == 'comparacoes':
            dicionario = self.comparacoes
        elif categoria == 'guias_praticos':
            dicionario = self.guias_praticos
        else:
            return f"Categoria '{categoria}' não encontrada."
        
        # Buscar termo
        if termo_norm in dicionario:
            if tipo_info and tipo_info in dicionario[termo_norm]:
                return dicionario[termo_norm][tipo_info]
            return dicionario[termo_norm]
        
        # Busca alternativa para termos similares
        for key in dicionario:
            if termo_norm in key or key in termo_norm:
                if tipo_info and tipo_info in dicionario[key]:
                    return dicionario[key][tipo_info]
                return dicionario[key]
        
        return f"Informação sobre '{termo}' não encontrada na categoria '{categoria}'."
    
    def buscar_em_todas_categorias(self, termo):
        """
        Busca um termo em todas as categorias
        
        Args:
            termo (str): Termo a ser buscado
            
        Returns:
            dict: Resultados encontrados em cada categoria
        """
        resultados = {}
        categorias = [
            ('assistentes_virtuais', self.assistentes_virtuais),
            ('llms', self.llms),
            ('outras_ias', self.outras_ias),
            ('chatbots', self.chatbots),
            ('comparacoes', self.comparacoes),
            ('guias_praticos', self.guias_praticos)
        ]
        
        termo_norm = termo.lower().strip()
        
        for nome_cat, dicionario in categorias:
            for key in dicionario:
                if termo_norm in key or key in termo_norm:
                    if nome_cat not in resultados:
                        resultados[nome_cat] = []
                    resultados[nome_cat].append(key)
        
        return resultados
    
    def listar_itens_categoria(self, categoria):
        """
        Lista todos os itens disponíveis em uma categoria
        
        Args:
            categoria (str): Categoria desejada
            
        Returns:
            list: Lista de itens na categoria
        """
        if categoria == 'assistentes_virtuais':
            return list(self.assistentes_virtuais.keys())
        elif categoria == 'llms':
            return list(self.llms.keys())
        elif categoria == 'outras_ias':
            return list(self.outras_ias.keys())
        elif categoria == 'chatbots':
            return list(self.chatbots.keys())
        elif categoria == 'comparacoes':
            return list(self.comparacoes.keys())
        elif categoria == 'guias_praticos':
            return list(self.guias_praticos.keys())
        else:
            return []
    
    def formatar_resposta(self, info, formato='texto'):
        """
        Formata informações para resposta ao usuário
        
        Args:
            info (dict/str): Informações a serem formatadas
            formato (str): Formato desejado ('texto', 'detalhado', 'resumido')
            
        Returns:
            str: Resposta formatada
        """
        if isinstance(info, str):
            return info
        
        if not info or not isinstance(info, dict):
            return "Não foi possível encontrar informações sobre este tópico."
        
        # Verificar se é um item de assistente virtual
        if 'nome' in info and 'empresa' in info and 'dispositivos' in info:
            if formato == 'resumido':
                return f"{info['nome']} é um assistente virtual da {info['empresa']} disponível em {', '.join(info['dispositivos'][:2])}... {info.get('descricao', '').split('.')[0]}."
            
            resposta = f"# {info['nome']}\n\n"
            resposta += f"**Empresa:** {info['empresa']}\n\n"
            resposta += f"**Descrição:** {info.get('descricao', 'Não disponível')}\n\n"
            resposta += f"**Dispositivos compatíveis:** {', '.join(info.get('dispositivos', ['Não especificado']))}\n\n"
            
            if 'recursos' in info:
                resposta += "**Principais recursos:**\n"
                for recurso in info['recursos']:
                    resposta += f"- {recurso}\n"
                resposta += "\n"
            
            if 'idiomas' in info:
                resposta += f"**Idiomas suportados:** {', '.join(info['idiomas'][:5])}"
                if len(info['idiomas']) > 5:
                    resposta += " e outros."
            
            return resposta
        
        # Verificar se é um item de LLM
        if 'nome' in info and 'empresa' in info and 'capacidades' in info:
            if formato == 'resumido':
                return f"{info['nome']} é um modelo de linguagem da {info['empresa']} lançado em {info.get('lançamento', 'data não especificada')}. {info.get('descricao', '').split('.')[0]}."
            
            resposta = f"# {info['nome']}\n\n"
            resposta += f"**Empresa:** {info['empresa']}\n\n"
            resposta += f"**Lançamento:** {info.get('lançamento', 'Não especificado')}\n\n"
            resposta += f"**Descrição:** {info.get('descricao', 'Não disponível')}\n\n"
            
            if 'capacidades' in info:
                resposta += "**Principais capacidades:**\n"
                for cap in info['capacidades']:
                    resposta += f"- {cap}\n"
                resposta += "\n"
            
            if 'acesso' in info:
                resposta += "**Formas de acesso:**\n"
                for acesso in info['acesso']:
                    resposta += f"- {acesso}\n"
            
            return resposta
        
        # Para outros tipos de itens, tentar um formato genérico
        resposta = ""
        for chave, valor in info.items():
            if isinstance(valor, list):
                resposta += f"**{chave.replace('_', ' ').title()}:**\n"
                for item in valor:
                    if isinstance(item, dict):
                        for k, v in item.items():
                            resposta += f"- **{k}**: {v}\n"
                    else:
                        resposta += f"- {item}\n"
                resposta += "\n"
            elif isinstance(valor, dict):
                resposta += f"**{chave.replace('_', ' ').title()}:**\n"
                for k, v in valor.items():
                    if isinstance(v, list):
                        resposta += f"- **{k}**: {', '.join(v[:3])}"
                        if len(v) > 3:
                            resposta += " e outros"
                        resposta += "\n"
                    elif isinstance(v, dict):
                        resposta += f"- **{k}**:\n"
                        for sub_k, sub_v in v.items():
                            resposta += f"  - {sub_k}: {sub_v}\n"
                    else:
                        resposta += f"- **{k}**: {v}\n"
                resposta += "\n"
            else:
                resposta += f"**{chave.replace('_', ' ').title()}:** {valor}\n\n"
        
        return resposta

# Exemplo de uso
if __name__ == "__main__":
    kb = KnowledgeBase()
    
    # Testar busca de informações
    info = kb.obter_informacao('assistentes_virtuais', 'alexa')
    print(kb.formatar_resposta(info, 'resumido'))
    
    # Testar busca em todas as categorias
    resultados = kb.buscar_em_todas_categorias('google')
    print(resultados)
