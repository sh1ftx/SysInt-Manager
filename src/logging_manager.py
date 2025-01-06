# logging_manager.py
from datetime import datetime

class LoggingManager:
    """
    Classe responsável pela gestão dos logs do sistema.
    Registra eventos no console e em um arquivo.
    """
    def log_event(self, message):
        """
        Registra um evento no console e no arquivo de log.
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"{timestamp} - {message}"

        # Exibe o log no console
        print(log_message)

        # Grava o log no arquivo
        with open("interrupt_log.txt", "a") as log_file:
            log_file.write(f"{log_message}\n")
