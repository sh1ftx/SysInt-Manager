# main.py
from interrupt_manager import InterruptManager
from term_colors import TermColors
from interrupt_handlers import get_current_time  # Importa a função get_current_time
import threading
import time


def main():
    """
    Função principal que inicia a simulação de gerenciamento de interrupções.
    """
    print(f"\n{'='*50}\nSIMULAÇÃO DE GERENCIAMENTO DE INTERRUPÇÕES EM PYTHON\n{'='*50}")
    interrupt_manager = InterruptManager()

    # Limpa o arquivo de log e adiciona a data e hora da simulação
    with open("interrupt_log.txt", "w") as log_file:
        log_file.write(f"Log de Interrupções - Iniciado em {get_current_time()}\n")

    # Função que gera interrupções aleatórias
    def generate_interrupts():
        for _ in range(10):  # Número de interrupções geradas
            interrupt_manager.generate_interrupt()
            time.sleep(0.5)  # Intervalo entre as interrupções

    # Geração das interrupções em uma thread separada
    generator_thread = threading.Thread(target=generate_interrupts)
    generator_thread.start()
    
    # Garantir que a thread de geração de interrupções termine antes de despachar
    generator_thread.join()  # Espera a thread terminar

    # Despacha e trata as interrupções
    interrupt_manager.dispatch_interrupts()

    # Exibe a legenda de cores
    TermColors.show_color_legend()

    print("\n==== SIMULAÇÃO FINALIZADA ====")

if __name__ == "__main__":
    main()
