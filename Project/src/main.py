# main.py
from interrupt_manager import InterruptManager
from term_colors import TermColors
import threading
import time

def main():
    print(f"\n{'='*50}\nSIMULAÇÃO DE GERENCIAMENTO DE INTERRUPÇÕES EM PYTHON\n{'='*50}")
    interrupt_manager = InterruptManager()

    # Limpa o arquivo de log
    with open("interrupt_log.txt", "w") as log_file:
        log_file.write("Log de Interrupções:\n")

    # Gerar interrupções aleatórias em uma thread separada
    def generate_interrupts():
        for _ in range(10):
            interrupt_manager.generate_interrupt()
            time.sleep(0.5)

    generator_thread = threading.Thread(target=generate_interrupts)
    generator_thread.start()
    generator_thread.join()

    # Despachar e tratar as interrupções
    interrupt_manager.dispatch_interrupts()

    # Mostrar a legenda de cores
    TermColors.show_color_legend()
    print("\n==== SIMULAÇÃO FINALIZADA ====")

if __name__ == "__main__":
    main()
