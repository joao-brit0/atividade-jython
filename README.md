# Atividade Jython - Integração entre Python e Java

Projeto desenvolvido para demonstrar, de forma prática, a interoperabilidade entre Python e Java utilizando **Jython**.

## O que é Jython?

Jython é uma implementação da linguagem Python que executa sobre a **Java Virtual Machine (JVM)**. Por executar na JVM, um programa escrito em Python pode importar e utilizar diretamente classes e bibliotecas Java, sem precisar escrever um programa Java separado apenas para fazer essa comunicação.

Neste projeto foi utilizado o Jython 2.7.4 e uma imagem Java 11 no Docker.

## Estrutura do projeto

```text
atividade-jython/
├── README.md
├── Dockerfile
├── exemplo1.py
├── exemplo2.py
└── .gitignore
```

## Exemplo 1 - Arquivos e estruturas de dados Java

O arquivo `exemplo1.py` cria uma lista de tarefas e grava essas informações em um arquivo chamado `tarefas.txt`. Depois, o próprio programa abre o arquivo novamente e mostra o conteúdo no terminal.

### Classes Java utilizadas

- `java.util.ArrayList`
- `java.io.File`
- `java.io.FileWriter`
- `java.io.BufferedWriter`
- `java.io.FileReader`
- `java.io.BufferedReader`

### Como ocorre a integração?

O fluxo do programa é escrito em Python, utilizando funções, laços e listas de controle do código Python. Porém, a estrutura que armazena as tarefas é um `ArrayList` do Java e toda a leitura e escrita do arquivo é feita com classes de `java.io`.

Um exemplo direto da interoperabilidade é:

```python
from java.util import ArrayList

tarefas = ArrayList()
tarefas.add("Estudar Jython")
```

Apesar de o código estar em um arquivo `.py`, `ArrayList` é uma classe Java sendo utilizada diretamente pelo Jython.

## Exemplo 2 - Threads da JVM

O arquivo `exemplo2.py` cria três tarefas que são executadas por threads da JVM. Cada thread mostra no terminal seu nome, a etapa atual e o horário da execução.

### Classes e interfaces Java utilizadas

- `java.lang.Runnable`
- `java.lang.Thread`
- `java.text.SimpleDateFormat`
- `java.util.Date`

### Como ocorre a integração?

A classe `Trabalhador` é escrita em Python, mas implementa a interface Java `Runnable`:

```python
class Trabalhador(Runnable):
    def run(self):
        # codigo executado pela thread
        pass
```

Depois, o objeto Python é passado diretamente para uma `java.lang.Thread`:

```python
thread = Thread(Trabalhador("Thread-A"), "Thread-A")
thread.start()
```

Isso demonstra que um objeto definido em Python pode participar diretamente de uma API Java e ser executado por uma thread da JVM.

## Executando com Jython instalado na máquina

### Pré-requisitos

- Java 8 ou Java 11;
- Jython 2.7.4.

Após instalar o Jython e deixar o comando `jython` disponível no terminal, entre na pasta do projeto e execute:

```bash
jython exemplo1.py
jython exemplo2.py
```

### Executando com o JAR standalone

Também é possível utilizar o JAR standalone do Jython sem fazer uma instalação tradicional.

Com o arquivo `jython-standalone-2.7.4.jar` disponível na máquina, execute:

```bash
java -jar jython-standalone-2.7.4.jar exemplo1.py
java -jar jython-standalone-2.7.4.jar exemplo2.py
```

## Executando com Docker

Com o Docker instalado, abra o terminal na pasta do projeto.

### 1. Construir a imagem

```bash
docker build -t atividade-jython .
```

Durante o build, o Docker baixa o Jython 2.7.4 automaticamente. Portanto, não é necessário instalar Jython manualmente na máquina.

### 2. Executar os exemplos

```bash
docker run --rm atividade-jython
```

O container executará primeiro o `exemplo1.py` e depois o `exemplo2.py`.

## Saída esperada

No primeiro exemplo, será exibido o caminho do arquivo criado e as tarefas lidas por meio das classes Java.

Exemplo aproximado:

```text
=== Exemplo 1: java.io + java.util ===
Arquivo criado em: /app/tarefas.txt
Conteudo lido usando classes Java:
- Estudar Jython
- Praticar interoperabilidade
- Executar o projeto com Docker
```

No segundo exemplo, as threads serão executadas concorrentemente. A ordem das linhas pode variar, porque as threads funcionam de forma independente.

```text
=== Exemplo 2: Threads da JVM ===
[14:20:01.100] Thread-A executando etapa 1
[14:20:01.102] Thread-B executando etapa 1
[14:20:01.103] Thread-C executando etapa 1
...
Todas as threads da JVM finalizaram.
```

## Interoperabilidade observada

Os dois exemplos mostram que o Jython permite misturar os recursos da linguagem Python com APIs da plataforma Java no mesmo código.

No primeiro exemplo, Python controla o fluxo do programa enquanto objetos de `java.util` e `java.io` armazenam dados e manipulam arquivos. No segundo, uma classe escrita em Python implementa `Runnable` e é executada por objetos `Thread` da própria JVM.

Assim, não existe uma comunicação por arquivos, HTTP ou outro processo separado: Python e Java estão sendo utilizados dentro da mesma JVM.

## Vídeo de demonstração

Link do vídeo: https://youtu.be/Uvywn532G4c

