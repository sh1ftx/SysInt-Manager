# interrupt_manager.py
from queue import PriorityQueue
from interrupt_handlers import (
    handle_timer_interrupt,
    handle_io_interrupt,
    handle_system_error_interrupt,
    get_current_time,
)
from term_colors import TermColors
import random
import time

class InterruptManager:
    def __init__(self):
        """
        Inicializa o gerenciador de interrupções com uma fila de prioridade.
        """
        self.interrupt_queue = PriorityQueue()
        self.interrupt_handlers = {
            "TIMER": handle_timer_interrupt,
            "IO": handle_io_interrupt,
            "SYSTEM_ERROR": handle_system_error_interrupt,
        }

    def log_event(self, message):
        """
        Registra um evento no console e em um arquivo de log.
        """
        print(message)
        with open("interrupt_log.txt", "a") as log_file:
            log_file.write(f"{message}\n")

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
        self.log_event(message)
        self.interrupt_queue.put((priority, interrupt_type))

    def dispatch_interrupts(self):
        """
        Despacha e trata interrupções com base na fila de prioridade.
        """
        self.log_event(f"{get_current_time()} - {TermColors.CYAN}[DESPACHANTE] Iniciando o despacho das interrupções...{TermColors.RESET}")
        while not self.interrupt_queue.empty():
            priority, interrupt_type = self.interrupt_queue.get()
            message = f"{get_current_time()} - {TermColors.CYAN}[DESPACHANTE] Tratando: {interrupt_type} (Prioridade {priority}){TermColors.RESET}"
            self.log_event(message)
            handler = self.interrupt_handlers.get(interrupt_type)
            if handler:
                handler()
        self.log_event(f"{get_current_time()} - {TermColors.CYAN}[DESPACHANTE] Todas as interrupções foram tratadas.{TermColors.RESET}")
