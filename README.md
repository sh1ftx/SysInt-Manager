## **Simulador de Interrupções com Prioridades e Timer**

**Participantes do projeto:**

- [Gleison Oliveira](https://github.com/gleiSUN)
- [Kayky Rodrigues](https://github.com/xFrostzss)
- [Fernando Sena](https://github.com/FernandosenaDev)
- [João Henrique](https://github.com/xFrostzss)
- [Vinycius Huellyson](https://github.com/VINYCIU51)

---

## **Índice**

1. [Introdução](#1-introdução)  
2. [Objetivo do Projeto](#2-objetivo-do-projeto)  
3. [Visão Geral do Sistema](#3-visão-geral-do-sistema)  
4. [Arquitetura e Estrutura do Código](#4-arquitetura-e-estrutura-do-código)  
    4.1 [Como o sistema é dividido](#41-como-o-sistema-é-dividido)  
    4.2 [Explicação de cada arquivo e função](#42-explicação-de-cada-arquivo-e-função)  
5. [Execução do Programa](#5-execução-do-programa)  
6. [Saída e Explicação dos Resultados](#6-saída-e-explicação-dos-resultados)  
7. [Conclusão](#7-conclusão)

---

## **1. Introdução**  

O **Simulador de Interrupções com Prioridades e Timer** foi desenvolvido para simular como as interrupções em sistemas operacionais são gerenciadas de maneira eficiente. O projeto simula a criação, despacho e tratamento de interrupções, permitindo que se entenda melhor o conceito de interrupções com diferentes níveis de prioridade. A simulação usa conceitos de programação orientada a objetos para modularizar o código e torná-lo mais compreensível.

Neste projeto, utilizamos um **timer** para marcar o tempo de execução de cada interrupção e **cores** para diferenciar os tipos de interrupções, ajudando a visualizar melhor o que está acontecendo em tempo real. Além disso, o projeto conta com uma estrutura de logs detalhada que fornece uma visão clara do processo de gerenciamento das interrupções.

---

## **2. Objetivo do Projeto**  

O objetivo principal deste projeto é simular e gerenciar interrupções em um sistema operacional com base nas prioridades. O projeto oferece uma maneira prática e visual de compreender como interrupções de diferentes tipos são tratadas e como elas são priorizadas. Os objetivos específicos são:

- **Simular a geração de interrupções** com diferentes tipos e prioridades.
- **Gerenciar as interrupções** para garantir que as de maior prioridade sejam tratadas primeiro.
- **Exibir informações no terminal** de forma clara e organizada, com a utilização de cores para diferenciar tipos de interrupções.
- **Registrar eventos importantes** no sistema através de logs, para rastrear o que está acontecendo durante a execução.

---

## **3. Visão Geral do Sistema**  

O sistema simula interrupções de diferentes tipos (erro de sistema, entrada/saída, temporizador) e os trata de acordo com a sua prioridade. O programa é dividido em várias classes e módulos que gerenciam a geração e o despacho dessas interrupções.

### **Componentes Principais:**

1. **Gerador de Interrupções**: Esta parte do sistema é responsável por criar as interrupções. Cada interrupção tem um tipo e uma prioridade associada.
2. **Despachante de Interrupções**: O despachante gerencia a execução das interrupções. Ele garante que as interrupções com maior prioridade sejam tratadas antes das de menor prioridade.
3. **Logger**: O sistema registra todos os eventos, incluindo a criação, despacho e tratamento de interrupções, com timestamps e níveis de prioridade.

### **Características Visuais e Funcionais:**

- **Cores**: Cada tipo de interrupção tem uma cor específica no terminal, facilitando a leitura e acompanhamento do que está acontecendo.
- **Timer**: O tempo de execução de cada interrupção é registrado, mostrando quando a interrupção foi gerada e quando foi tratada.
- **Registro de Logs**: Um log detalhado é gerado para cada evento importante, permitindo uma análise mais profunda do processo de gerenciamento das interrupções.

---

## **4. Arquitetura e Estrutura do Código**  

O código é dividido em vários arquivos, cada um com uma função específica no sistema. A seguir, vamos explicar como o código está estruturado e qual a responsabilidade de cada parte:

### **4.1 Como o sistema é dividido**

O sistema é composto pelos seguintes componentes principais:

- **Geração de Interrupções**: O gerador cria interrupções de forma aleatória e as coloca em uma fila.
- **Despacho de Interrupções**: O despachante organiza as interrupções na fila de acordo com sua prioridade e as trata uma a uma.
- **Gerenciamento de Logs**: O logger registra todos os eventos importantes, como a criação e o tratamento de interrupções.

### **4.2 Explicação de cada arquivo e função**

#### **Arquivo: `interrupt_manager.py`**
Este arquivo contém a **classe `InterruptManager`**, que é responsável pela geração, armazenamento e despacho das interrupções. O código dentro dessa classe garante que as interrupções sejam ordenadas e tratadas conforme suas prioridades.

#### **Arquivo: `logging_manager.py`**
Contém a **classe `LoggingManager`**, responsável pela geração de logs durante a execução do programa. O logger formata os eventos com timestamps e categoriza as interrupções com base em sua prioridade e tipo.

#### **Arquivo: `main.py`**
Este é o arquivo principal. Ele coordena a execução do programa, inicializa o gerenciador de interrupções e o despachante, e começa a geração e o tratamento das interrupções. Ele também define o comportamento do sistema, controlando a execução de cada parte.

---

## **5. Execução do Programa**  

### **Passo a Passo para Execução**:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/sh1ftx/SysInt-Manager.git
   ```
2. **Acesse a pasta do projeto**:
   ```bash
   cd SysInt-Manager
   ```
3. **Execute o programa**:
   ```bash
   python3 src/main.py
   ```

### **Requisitos**:
- **Python 3.x**: Certifique-se de ter o Python 3 instalado no seu sistema.
- Não há dependências externas, então não há necessidade de instalar pacotes adicionais.

---

## **6. Saída e Explicação dos Resultados**  

Quando o programa é executado, ele gera interrupções que são tratadas e exibidas no terminal. A saída pode ser algo como:

```
13:23:22 - [GERADOR] Interrupção gerada: SYSTEM_ERROR (Prioridade 1)
13:23:23 - [GERADOR] Interrupção gerada: IO (Prioridade 2)
13:23:24 - [DESPACHANTE] Iniciando o despacho das interrupções...
13:23:24 - [DESPACHANTE] Tratando: SYSTEM_ERROR (Prioridade 1)
13:23:25 - [DESPACHANTE] Tratando: IO (Prioridade 2)
```

**Explicação**:
- **Gerador**: O gerador cria interrupções do tipo `SYSTEM_ERROR` e `IO`, com prioridades diferentes.
- **Despachante**: O despachante começa o processo de tratamento, primeiro tratando a interrupção `SYSTEM_ERROR` (de maior prioridade) e depois a `IO`.
- **Log**: Todos os eventos são registrados com timestamps e informações detalhadas sobre o tipo da interrupção e sua prioridade.

---

## **7. Conclusão**  

Este projeto tem como objetivo simular o comportamento de interrupções em um sistema operacional, implementando a lógica de prioridades e o uso de timers para controlar a execução das interrupções. A utilização de cores no terminal e logs detalhados ajuda a visualizar e entender como as interrupções são gerenciadas em tempo real.

O projeto é altamente modularizado, o que facilita a manutenção e a expansão de suas funcionalidades. Ele serve como uma excelente ferramenta educacional para entender o funcionamento interno de sistemas operacionais e a forma como as interrupções são tratadas.

---

**Link para o Repositório**: [SysInt-Manager no GitHub](https://github.com/sh1ftx/SysInt-Manager)
