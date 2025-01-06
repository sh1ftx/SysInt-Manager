# interrupt_handlers.py
from term_colors import TermColors
import time

def get_current_time():
    """Retorna o horário atual no formato HH:MM:SS."""
    return time.strftime("%H:%M:%S", time.gmtime())

def handle_timer_interrupt():
    """Tratador de interrupção de temporizador (TIMER)."""
    try:
        print(f"{get_current_time()} - {TermColors.GREEN}[TIMER] Interrupção de temporizador tratada.{TermColors.RESET}")
        time.sleep(1)
    except Exception as e:
        print(f"{get_current_time()} - {TermColors.RED}[ERRO] Falha ao tratar interrupção de temporizador: {e}{TermColors.RESET}")

def handle_io_interrupt():
    """Tratador de interrupção de Entrada/Saída (IO)."""
    try:
        print(f"{get_current_time()} - {TermColors.YELLOW}[I/O] Interrupção de Entrada/Saída tratada.{TermColors.RESET}")
        time.sleep(1)
    except Exception as e:
        print(f"{get_current_time()} - {TermColors.RED}[ERRO] Falha ao tratar interrupção de I/O: {e}{TermColors.RESET}")

def handle_system_error_interrupt():
    """Tratador de interrupção de Erro de Sistema (SYSTEM_ERROR)."""
    try:
        print(f"{get_current_time()} - {TermColors.RED}[ERRO] Interrupção de Erro de Sistema tratada.{TermColors.RESET}")
        time.sleep(1)
    except Exception as e:
        print(f"{get_current_time()} - {TermColors.RED}[ERRO] Falha ao tratar interrupção de Erro de Sistema: {e}{TermColors.RESET}")
