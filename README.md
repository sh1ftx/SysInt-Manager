**Simulador de Interrupções com Prioridades e Timer**  

**Participantes do projeto:**

- [Gleison Oliveira](https://github.com/sh1ftx)
- [Kayky Rodrigues](https://github.com/sh1ftx)
- [Vinycius Huellyson](https://github.com/sh1ftx)

---

## **Índice**  

1. [Introdução](#1-introdução)  
2. [Objetivo do Projeto](#2-objetivo-do-projeto)  
3. [Visão Geral do Sistema](#3-visão-geral-do-sistema)  
4. [Estrutura do Código](#4-estrutura-do-código)  
    4.1 [Arquivo: `term_colors.py`](#41-arquivo-term_colorspy)  
    4.2 [Arquivo: `legend.py`](#42-arquivo-legendpy)  
    4.3 [Arquivo: `subprocess_manager.py`](#43-arquivo-subprocess_managerpy)  
    4.4 [Arquivo: `main.py`](#44-arquivo-mainpy)  
5. [Execução do Programa](#5-execução-do-programa)  
6. [Saída e Explicação dos Resultados](#6-saída-e-explicação-dos-resultados)  
7. [Conclusão](#7-conclusão)  

---

## **1. Introdução**  
Este projeto é um **simulador de interrupções** desenvolvido em **Python**. Ele replica o funcionamento de um sistema operacional ao gerenciar eventos com base em prioridades, simulando interrupções. Cada evento (subprocesso) é identificado por uma **cor** específica, possui um **timer** para indicar o momento de execução e exibe informações detalhadas do início ao término da tarefa.  

---

## **2. Objetivo do Projeto**  
- Proporcionar uma compreensão prática sobre interrupções em sistemas operacionais.  
- Demonstrar gerenciamento de eventos com prioridades em um ambiente controlado.  
- Oferecer uma saída no terminal organizada, informativa e fácil de interpretar com uso de cores e timers.  

---

## **3. Visão Geral do Sistema**  
O programa é dividido em **subprocessos** que realizam tarefas específicas, simulando interrupções de diferentes tipos.  

**Características principais:**  
1. **Timer**: Marca o momento exato em que cada subprocesso inicia e termina.  
2. **Cores**: Diferenciam os subprocessos no terminal para facilitar a leitura.  
3. **Legenda**: Explica as cores utilizadas e suas respectivas funções.  
4. **Execução Controlada**: Os subprocessos são gerenciados sequencialmente com tempo simulado de execução.  

---

## **4. Estrutura do Código**  

O projeto está organizado em quatro arquivos principais:  

### **4.1 Arquivo: `term_colors.py`**  
**Função**: Define as **cores ANSI** para estilizar a saída no terminal.  

```python
class TermColors:
    BLUE = "\033[94m"      # Processo Principal
    RED = "\033[91m"       # Subprocesso 1
    GREEN = "\033[92m"     # Subprocesso 2
    YELLOW = "\033[93m"    # Subprocesso 3
    MAGENTA = "\033[95m"   # Subprocesso 4
    CYAN = "\033[96m"      # Subprocesso 5
    ORANGE = "\033[38;5;214m"  # Subprocesso 6
    RESET = "\033[0m"      # Reset para cor padrão
```

---

### **4.2 Arquivo: `legend.py`**  
**Função**: Exibe a legenda no terminal, associando cada **cor** ao subprocesso e explicando sua função.  

```python
from term_colors import TermColors

def printLegend():
    print(f"{TermColors.BLUE}Processo Principal:{TermColors.RESET} Gerencia os subprocessos.")
    print(f"{TermColors.RED}Subprocesso 1:{TermColors.RESET} Gera interrupção tipo 1.")
    print(f"{TermColors.GREEN}Subprocesso 2:{TermColors.RESET} Gera interrupção tipo 2.")
    print(f"{TermColors.YELLOW}Subprocesso 3:{TermColors.RESET} Temporizador (Timer).")
    print(f"{TermColors.MAGENTA}Subprocesso 4:{TermColors.RESET} Simula evento de entrada/saída.")
    print(f"{TermColors.CYAN}Subprocesso 5:{TermColors.RESET} Simula erro de sistema.")
    print(f"{TermColors.ORANGE}Subprocesso 6:{TermColors.RESET} Prioridade mais baixa.\n")
```

---

### **4.3 Arquivo: `subprocess_manager.py`**  
**Função**: Gerencia a criação e execução dos **subprocessos**, exibindo informações detalhadas e registrando os horários.  

```python
import os, time, multiprocessing
from datetime import datetime
from term_colors import TermColors

def subProcessTask(number, color, task_name):
    pid = os.getpid()
    start_time = datetime.now().strftime("%H:%M:%S")
    print(f"{color}[{task_name}] Início: {start_time} | PID: {pid}{TermColors.RESET}")
    time.sleep(3)  # Simula execução
    end_time = datetime.now().strftime("%H:%M:%S")
    print(f"{color}[{task_name}] Fim: {end_time} | PID: {pid}{TermColors.RESET}\n")

def manageSubProcesses():
    tasks = [
        ("Subprocesso 1", TermColors.RED),
        ("Subprocesso 2", TermColors.GREEN),
        ("Subprocesso 3", TermColors.YELLOW),
        ("Subprocesso 4", TermColors.MAGENTA),
        ("Subprocesso 5", TermColors.CYAN),
        ("Subprocesso 6", TermColors.ORANGE)
    ]
    for task_name, color in tasks:
        process = multiprocessing.Process(target=subProcessTask, args=(1, color, task_name))
        process.start()
        process.join()
```

---

### **4.4 Arquivo: `main.py`**  
**Função**: Arquivo principal que orquestra a execução do programa.  

```python
from legend import printLegend
from subprocess_manager import manageSubProcesses

def main():
    print("\n### Simulador de Interrupções com Timer ###\n")
    printLegend()
    manageSubProcesses()
    print("\n### Fim da Execução ###\n")

if __name__ == "__main__":
    main()
```

---

## **5. Execução do Programa**  
1. Garanta que o **Python 3.x** esteja instalado.  
2. Execute o arquivo principal:  
   ```bash
   python main.py
   ```  

---

## **6. Saída e Explicação dos Resultados**  

### **Saída Esperada:**  
- A legenda é exibida no início, associando cada cor a um subprocesso.  
- Cada subprocesso imprime:  
   - **Horário de início**  
   - **PID**  
   - **Horário de término**  
- As cores no terminal facilitam a identificação das etapas.  

### **Exemplo Simplificado:**  

```
Processo Principal: Gerencia os subprocessos.
Subprocesso 1: Gera interrupção tipo 1.  
...

[Subprocesso 1] Início: 10:30:00 | PID: 12345  
[Subprocesso 1] Fim: 10:30:03 | PID: 12345  

[Subprocesso 2] Início: 10:30:04 | PID: 12346  
[Subprocesso 2] Fim: 10:30:07 | PID: 12346  
...
```

---

## **7. Conclusão**  
O projeto cumpre os requisitos propostos, simulando interrupções de forma clara, utilizando **cores**, **timers** e **organização modular**. A documentação detalha cada componente, facilitando o entendimento e a apresentação.
