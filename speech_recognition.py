"""
Módulo de reconhecimento de fala usando Whisper
Implementa funcionalidades de transcrição de áudio para texto
"""

import os
import tempfile
import io
import numpy as np
import wave

# Verificar se Whisper está disponível, caso contrário usar mock
try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False
    print("Aviso: Whisper não está disponível. Usando implementação simulada.")

class WhisperRecognizer:
    """Reconhecedor de fala usando Whisper ou simulação"""
    
    def __init__(self, model_size="base", language="pt", offline=True):
        """
        Inicializa o reconhecedor de fala
        
        Args:
            model_size (str): Tamanho do modelo Whisper ('tiny', 'base', 'small', 'medium', 'large')
            language (str): Código do idioma (ex: 'pt', 'en')
            offline (bool): Se True, tenta usar Whisper, caso contrário usa simulação
        """
        self.model_size = model_size
        self.language = language
        self.offline = offline
        
        # Inicializar modelo se disponível
        if WHISPER_AVAILABLE and offline:
            try:
                print(f"Carregando modelo Whisper {model_size}...")
                self.model = whisper.load_model(model_size)
                print("Modelo Whisper carregado com sucesso!")
            except Exception as e:
                print(f"Erro ao carregar modelo Whisper: {e}")
                self.model = None
        else:
            self.model = None
            print("Usando reconhecedor de fala simulado")
    
    def transcribe(self, audio_data):
        """
        Transcreve áudio para texto
        
        Args:
            audio_data: Objeto BytesIO contendo áudio WAV ou caminho para arquivo de áudio
            
        Returns:
            str: Texto transcrito
        """
        # Se não tiver modelo, usar simulação
        if self.model is None:
            return self._mock_transcribe(audio_data)
        
        # Se audio_data for um objeto BytesIO, salvar em arquivo temporário
        if isinstance(audio_data, io.BytesIO):
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
                temp_file.write(audio_data.getvalue())
                temp_path = temp_file.name
            
            try:
                result = self.model.transcribe(
                    temp_path,
                    language=self.language,
                    fp16=False  # Usar precisão FP32 para CPU
                )
                return result["text"].strip()
            finally:
                # Limpar arquivo temporário
                if os.path.exists(temp_path):
                    os.remove(temp_path)
        else:
            # Se for um caminho de arquivo
            result = self.model.transcribe(
                audio_data,
                language=self.language,
                fp16=False
            )
            return result["text"].strip()
    
    def _mock_transcribe(self, audio_data):
        """
        Simulação de transcrição quando Whisper não está disponível
        
        Args:
            audio_data: Objeto BytesIO contendo áudio WAV ou caminho para arquivo
            
        Returns:
            str: Texto simulado
        """
        # Verificar se há áudio real
        if isinstance(audio_data, io.BytesIO):
            # Extrair duração do áudio
            audio_data.seek(0)
            with wave.open(audio_data, 'rb') as wf:
                frames = wf.getnframes()
                rate = wf.getframerate()
                duration = frames / float(rate)
            
            # Simular texto baseado na duração
            if duration < 1.0:
                return "Olá."
            elif duration < 2.0:
                return "Olá, como posso ajudar?"
            else:
                return "Olá, como posso ajudar você hoje? Estou ouvindo."
        else:
            # Caminho de arquivo ou outro formato
            return "Olá, como posso ajudar você hoje? Estou ouvindo."


# Exemplo de uso
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        audio_file = sys.argv[1]
        recognizer = WhisperRecognizer(model_size="base", language="pt")
        
        print(f"Transcrevendo {audio_file}...")
        text = recognizer.transcribe(audio_file)
        print(f"Texto reconhecido: {text}")
