"""
Módulo de detecção de palavra de ativação (wake word)
Utiliza a biblioteca openWakeWord para detecção de palavras-chave no áudio
"""

import os
import numpy as np
import pyaudio
import wave
import io
import time
import threading
import queue

# Verificar se openWakeWord está disponível, caso contrário usar mock
try:
    import openwakeword
    OPENWAKEWORD_AVAILABLE = True
except ImportError:
    OPENWAKEWORD_AVAILABLE = False
    print("Aviso: openWakeWord não está disponível. Usando implementação simulada.")

class WakeWordDetector:
    """Detector de palavra de ativação usando openWakeWord ou simulação"""
    
    def __init__(self, model_name="ei brandini", threshold=0.5, offline=True):
        """
        Inicializa o detector de palavra de ativação
        
        Args:
            model_name (str): Nome do modelo de palavra de ativação
            threshold (float): Limiar de confiança para detecção (0.0 a 1.0)
            offline (bool): Se True, tenta usar openWakeWord, caso contrário usa simulação
        """
        self.model_name = model_name
        self.threshold = threshold
        self.offline = offline
        self.running = False
        self.detected_callback = None
        self.detection_thread = None
        self.audio_queue = queue.Queue()
        
        # Configurações de áudio
        self.sample_rate = 16000
        self.chunk_size = 1280  # 80ms a 16kHz
        
        # Inicializar PyAudio
        self.p = pyaudio.PyAudio()
        self.stream = None
        
        # Inicializar modelo se disponível
        if OPENWAKEWORD_AVAILABLE and offline:
            try:
                print(f"Inicializando modelo openWakeWord para '{model_name}'...")
                self.model = openwakeword.Model()
                print("Modelo inicializado com sucesso!")
            except Exception as e:
                print(f"Erro ao inicializar openWakeWord: {e}")
                self.model = None
        else:
            self.model = None
            print("Usando detector de palavra de ativação simulado")
    
    def start(self, callback=None):
        """
        Inicia a detecção de palavra de ativação em segundo plano
        
        Args:
            callback (callable): Função a ser chamada quando a palavra for detectada
        """
        if self.running:
            print("Detector já está em execução")
            return
        
        self.detected_callback = callback
        self.running = True
        
        # Iniciar stream de áudio
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )
        
        # Iniciar thread de detecção
        self.detection_thread = threading.Thread(target=self._detection_loop)
        self.detection_thread.daemon = True
        self.detection_thread.start()
        
        print("Detector de palavra de ativação iniciado")
    
    def stop(self):
        """Para a detecção de palavra de ativação"""
        if not self.running:
            return
        
        self.running = False
        
        # Aguardar thread terminar
        if self.detection_thread:
            self.detection_thread.join(timeout=2.0)
        
        # Fechar stream de áudio
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
        
        print("Detector de palavra de ativação parado")
    
    def _detection_loop(self):
        """Loop principal de detecção em segundo plano"""
        while self.running:
            try:
                # Ler frame de áudio
                audio_data = self.stream.read(self.chunk_size, exception_on_overflow=False)
                
                # Converter para numpy array
                audio_frame = np.frombuffer(audio_data, dtype=np.int16)
                
                # Detectar palavra de ativação
                if self.detect(audio_frame):
                    print(f"Palavra de ativação '{self.model_name}' detectada!")
                    
                    # Capturar áudio adicional após detecção
                    audio_buffer = self.capture_audio(duration=5.0)
                    
                    # Adicionar à fila
                    self.audio_queue.put(audio_buffer)
                    
                    # Chamar callback se definido
                    if self.detected_callback:
                        self.detected_callback(audio_buffer)
                
                # Pequena pausa para reduzir uso de CPU
                time.sleep(0.01)
                
            except Exception as e:
                print(f"Erro no loop de detecção: {e}")
                time.sleep(0.1)
    
    def detect(self, audio_frame):
        """
        Detecta palavra de ativação em um frame de áudio
        
        Args:
            audio_frame (numpy.ndarray): Frame de áudio como array numpy
            
        Returns:
            bool: True se a palavra de ativação foi detectada, False caso contrário
        """
        if self.model is not None:
            # Usar openWakeWord
            prediction = self.model.predict(audio_frame)
            score = prediction.get(self.model_name, 0.0)
            return score > self.threshold
        else:
            # Simulação: detecta aleatoriamente com baixa probabilidade
            # Apenas para fins de teste quando openWakeWord não está disponível
            return np.random.random() > 0.995  # ~0.5% de chance de detecção
    
    def capture_audio(self, duration=5.0):
        """
        Captura áudio adicional após detecção da palavra de ativação
        
        Args:
            duration (float): Duração em segundos
            
        Returns:
            io.BytesIO: Buffer contendo áudio WAV
        """
        frames = []
        
        # Calcular número de chunks para a duração desejada
        num_chunks = int(self.sample_rate * duration / self.chunk_size)
        
        # Capturar áudio
        for _ in range(num_chunks):
            data = self.stream.read(self.chunk_size, exception_on_overflow=False)
            frames.append(data)
        
        # Criar arquivo WAV em memória
        wav_buffer = io.BytesIO()
        with wave.open(wav_buffer, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16 bits
            wf.setframerate(self.sample_rate)
            wf.writeframes(b''.join(frames))
        
        wav_buffer.seek(0)
        return wav_buffer
    
    def get_next_audio(self, timeout=None):
        """
        Obtém o próximo áudio capturado após detecção
        
        Args:
            timeout (float): Tempo máximo de espera em segundos
            
        Returns:
            io.BytesIO: Buffer contendo áudio WAV ou None se timeout
        """
        try:
            return self.audio_queue.get(timeout=timeout)
        except queue.Empty:
            return None
    
    def __del__(self):
        """Limpar recursos ao destruir o objeto"""
        self.stop()
        
        if hasattr(self, 'p') and self.p:
            self.p.terminate()


# Exemplo de uso
if __name__ == "__main__":
    def on_wake_word(audio_buffer):
        print("Palavra de ativação detectada! Áudio capturado.")
    
    detector = WakeWordDetector(model_name="ei brandini", threshold=0.5)
    detector.start(callback=on_wake_word)
    
    try:
        print("Aguardando palavra de ativação... (Ctrl+C para sair)")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando...")
    finally:
        detector.stop()
