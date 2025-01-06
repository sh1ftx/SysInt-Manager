# interrupt_manager.py
from queue import PriorityQueue
from interrupt_handlers import (
    handle_timer_interrupt,
    handle_io_interrupt,
    handle_system_error_interrupt,
    get_current_time,
)
from term_colors import TermColors
from logging_manager import LoggingManager  # Adicionando a importação do LoggingManager
import random
import time

class InterruptManager:
    def __init__(self):
        """
        Inicializa o gerenciador de interrupções com uma fila de prioridade
        e um gerenciador de logs.
        """
        self.interrupt_queue = PriorityQueue()
        self.interrupt_handlers = {
            "TIMER": handle_timer_interrupt,
            "IO": handle_io_interrupt,
            "SYSTEM_ERROR": handle_system_error_interrupt,
        }
        self.logger = LoggingManager()  # Usando o LoggingManager para gerenciar os logs

    def generate_interrupt(self):
        """
        Simula a geração aleatória de interrupções com prioridades.
        """
        interrupts = [
            (3, "TIMER"),         # Prioridade baixa
            (2, "IO"),            # Prioridade média
            (1, "SYSTEM_ERROR"),  # Prioridade alta
        ]
        priority, interrupt_type = random.choice(interrupts)
        timestamp = get_current_time()
        message = f"{timestamp} - {TermColors.CYAN}[GERADOR] Interrupção gerada: {interrupt_type} (Prioridade {priority}){TermColors.RESET}"
        self.logger.log_event(message)  # Registrando o evento no log
        self.interrupt_queue.put((priority, interrupt_type))

    def dispatch_interrupts(self):
        """
        Despacha e trata interrupções com base na fila de prioridade.
        """
        self.logger.log_event(f"{get_current_time()} - {TermColors.CYAN}[DESPACHANTE] Iniciando o despacho das interrupções...{TermColors.RESET}")
        while not self.interrupt_queue.empty():
            priority, interrupt_type = self.interrupt_queue.get()
            message = f"{get_current_time()} - {TermColors.CYAN}[DESPACHANTE] Tratando: {interrupt_type} (Prioridade {priority}){TermColors.RESET}"
            self.logger.log_event(message)  # Registrando o evento no log
            handler = self.interrupt_handlers.get(interrupt_type)
            if handler:
                handler()
        self.logger.log_event(f"{get_current_time()} - {TermColors.CYAN}[DESPACHANTE] Todas as interrupções foram tratadas.{TermColors.RESET}")
