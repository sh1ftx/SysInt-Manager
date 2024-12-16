# term_colors.py
class TermColors:
    """
    Cores ANSI para estilizar saídas no terminal.
    """
    RED = "\033[91m"         # Erro de Sistema
    GREEN = "\033[92m"       # Temporizador
    YELLOW = "\033[93m"      # Entrada/Saída
    CYAN = "\033[96m"        # Informações gerais
    RESET = "\033[0m"        # Reset para cor padrão

    @staticmethod
    def show_color_legend():
        """
        Mostra a legenda explicando cada cor usada no terminal.
        """
        print("\nLegenda das Cores:")
        print(f"{TermColors.GREEN}→ TIMER: Interrupções de Temporizador.{TermColors.RESET}")
        print(f"{TermColors.YELLOW}→ I/O: Interrupções de Entrada/Saída.{TermColors.RESET}")
        print(f"{TermColors.RED}→ ERRO: Interrupções de Erro de Sistema.{TermColors.RESET}")
        print(f"{TermColors.CYAN}→ SISTEMA: Mensagens gerais do sistema.{TermColors.RESET}")
