# interrupt_handlers.py
from term_colors import TermColors
from datetime import datetime
import time

def get_current_time():
    """Retorna o horário atual no formato HH:MM:SS."""
    return datetime.now().strftime("%H:%M:%S")

def handle_timer_interrupt():
    print(f"{get_current_time()} - {TermColors.GREEN}[TIMER] Interrupção de temporizador tratada.{TermColors.RESET}")
    time.sleep(1)

def handle_io_interrupt():
    print(f"{get_current_time()} - {TermColors.YELLOW}[I/O] Interrupção de Entrada/Saída tratada.{TermColors.RESET}")
    time.sleep(1)

def handle_system_error_interrupt():
    print(f"{get_current_time()} - {TermColors.RED}[ERRO] Interrupção de Erro de Sistema tratada.{TermColors.RESET}")
    time.sleep(1)
