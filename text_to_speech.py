"""
Módulo de síntese de voz (text-to-speech)
Implementa funcionalidades de conversão de texto para fala
"""

import os
import tempfile
from datetime import datetime
import io

# Verificar se pyttsx3 está disponível para síntese offline
try:
    import pyttsx3
    PYTTSX3_AVAILABLE = True
except ImportError:
    PYTTSX3_AVAILABLE = False
    print("Aviso: pyttsx3 não está disponível. Síntese offline limitada.")

# Verificar se gTTS está disponível para síntese online
try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False
    print("Aviso: gTTS não está disponível. Síntese online não funcionará.")

class TextToSpeech:
    """Sintetizador de voz com suporte a modos online e offline"""
    
    def __init__(self, use_offline=True, language="pt-br", voice=None, rate=180):
        """
        Inicializa o sintetizador de voz
        
        Args:
            use_offline (bool): Se True, usa pyttsx3 (offline), caso contrário usa gTTS (online)
            language (str): Código do idioma (ex: 'pt-br', 'en')
            voice (str): ID da voz a ser usada (apenas para pyttsx3)
            rate (int): Velocidade da fala (apenas para pyttsx3)
        """
        self.use_offline = use_offline
        self.language = language
        self.voice = voice
        self.rate = rate
        
        # Verificar disponibilidade das bibliotecas
        if use_offline and not PYTTSX3_AVAILABLE:
            print("pyttsx3 não disponível, alternando para gTTS se disponível")
            self.use_offline = False
        
        if not self.use_offline and not GTTS_AVAILABLE:
            print("gTTS não disponível, alternando para modo simulado")
        
        # Diretório para arquivos de áudio - CORREÇÃO: usar caminho relativo ao script
        # Obter o diretório do script atual
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.output_dir = os.path.join(script_dir, "audio_output")
        
        # Garantir que o diretório exista
        try:
            os.makedirs(self.output_dir, exist_ok=True)
            print(f"Diretório de áudio criado/verificado: {self.output_dir}")
        except Exception as e:
            print(f"Erro ao criar diretório de áudio: {e}")
            # Fallback para diretório temporário do sistema
            self.output_dir = os.path.join(os.path.expanduser("~"), "assistente_audio")
            os.makedirs(self.output_dir, exist_ok=True)
            print(f"Usando diretório alternativo: {self.output_dir}")
        
        # Inicializar engine offline
        self.engine = None
        if self.use_offline and PYTTSX3_AVAILABLE:
            try:
                self.engine = pyttsx3.init()
                self.engine.setProperty('rate', self.rate)
                
                # Configurar voz se especificada
                if self.voice:
                    self.engine.setProperty('voice', self.voice)
                else:
                    # Tentar encontrar voz no idioma especificado
                    voices = self.engine.getProperty('voices')
                    for voice in voices:
                        if self.language[:2].lower() in voice.id.lower():
                            self.engine.setProperty('voice', voice.id)
                            break
                
                print("Engine de síntese offline inicializada com sucesso")
            except Exception as e:
                print(f"Erro ao inicializar engine de síntese offline: {e}")
                self.engine = None
                self.use_offline = False
    
    def synthesize(self, text, filename=None):
        """
        Sintetiza texto em fala e salva em arquivo
        
        Args:
            text (str): Texto a ser sintetizado
            filename (str): Nome do arquivo de saída (opcional)
            
        Returns:
            str: Caminho para o arquivo de áudio gerado
        """
        if not text:
            return None
        
        # Gerar nome de arquivo se não fornecido
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"tts_{timestamp}.mp3"
        
        filepath = os.path.join(self.output_dir, filename)
        
        try:
            if self.use_offline and self.engine:
                # Modo offline com pyttsx3
                self.engine.save_to_file(text, filepath)
                self.engine.runAndWait()
            elif GTTS_AVAILABLE:
                # Modo online com gTTS
                tts = gTTS(text=text, lang=self.language[:2], slow=False)
                tts.save(filepath)
            else:
                # Modo simulado - criar arquivo de áudio vazio
                with open(filepath, 'wb') as f:
                    f.write(b'')
                print(f"Simulação de síntese: '{text}'")
            
            # Verificar se o arquivo foi realmente criado
            if os.path.exists(filepath):
                print(f"Arquivo de áudio criado com sucesso: {filepath}")
                return filepath
            else:
                print(f"Erro: Arquivo de áudio não foi criado: {filepath}")
                return None
            
        except Exception as e:
            print(f"Erro na síntese de voz: {e}")
            # Tentar criar um arquivo vazio como fallback
            try:
                with open(filepath, 'wb') as f:
                    f.write(b'')
                print(f"Arquivo de áudio vazio criado como fallback: {filepath}")
                return filepath
            except:
                return None
    
    def speak(self, text, save_to_file=True, play_sound=False):
        """
        Sintetiza texto em fala e opcionalmente reproduz o som
        
        Args:
            text (str): Texto a ser sintetizado
            save_to_file (bool): Se True, salva o áudio em arquivo
            play_sound (bool): Se True, reproduz o som
            
        Returns:
            str: Caminho para o arquivo de áudio gerado ou None
        """
        if not text:
            return None
        
        if save_to_file or not self.use_offline:
            # Sintetizar e salvar em arquivo
            filepath = self.synthesize(text)
            
            # Reproduzir som se solicitado
            if play_sound and filepath and os.path.exists(filepath):
                self._play_audio(filepath)
            
            return filepath
        elif self.use_offline and self.engine:
            # Apenas reproduzir sem salvar
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                print(f"Erro ao reproduzir fala: {e}")
        else:
            print(f"Simulação de fala: '{text}'")
        
        return None
    
    def _play_audio(self, filepath):
        """
        Reproduz arquivo de áudio
        
        Args:
            filepath (str): Caminho para o arquivo de áudio
        """
        if not os.path.exists(filepath):
            print(f"Erro: Arquivo de áudio não encontrado: {filepath}")
            return
            
        try:
            # Tentar reproduzir com diferentes métodos
            try:
                # Método 1: playsound
                from playsound import playsound
                playsound(filepath)
                return
            except ImportError:
                pass
            
            try:
                # Método 2: pygame
                import pygame
                pygame.mixer.init()
                pygame.mixer.music.load(filepath)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                return
            except ImportError:
                pass
            
            # Método 3: sistema operacional
            import platform
            import subprocess
            
            system = platform.system()
            if system == 'Darwin':  # macOS
                subprocess.call(['afplay', filepath])
            elif system == 'Linux':
                subprocess.call(['aplay', filepath])
            elif system == 'Windows':
                try:
                    import winsound
                    winsound.PlaySound(filepath, winsound.SND_FILENAME)
                except Exception as e:
                    print(f"Erro ao reproduzir com winsound: {e}")
                    # Alternativa para Windows
                    os.startfile(filepath)
            
        except Exception as e:
            print(f"Erro ao reproduzir áudio: {e}")
    
    def get_available_voices(self):
        """
        Obtém lista de vozes disponíveis
        
        Returns:
            list: Lista de IDs de vozes disponíveis
        """
        if self.use_offline and self.engine:
            voices = self.engine.getProperty('voices')
            return [voice.id for voice in voices]
        return []


# Exemplo de uso
if __name__ == "__main__":
    # Criar sintetizador
    tts = TextToSpeech(use_offline=True, language="pt-br")
    
    # Testar síntese
    text = "Olá, eu sou um assistente de voz. Como posso ajudar você hoje?"
    print(f"Sintetizando: '{text}'")
    
    # Sintetizar e reproduzir
    filepath = tts.speak(text, save_to_file=True, play_sound=True)
    
    if filepath:
        print(f"Áudio salvo em: {filepath}")
    
    # Listar vozes disponíveis
    voices = tts.get_available_voices()
    if voices:
        print("Vozes disponíveis:")
        for voice in voices:
            print(f"  - {voice}")
