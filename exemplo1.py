"""
Exemplo 1: uso de classes Java para colecoes e manipulacao de arquivos.
Executar com Jython.
"""

from java.io import File, FileWriter, BufferedWriter, FileReader, BufferedReader
from java.util import ArrayList


def main():
    tarefas = ArrayList()
    tarefas.add("Estudar Jython")
    tarefas.add("Praticar interoperabilidade")
    tarefas.add("Executar o projeto com Docker")

    arquivo = File("tarefas.txt")

    escritor = BufferedWriter(FileWriter(arquivo))
    try:
        for tarefa in tarefas:
            escritor.write(tarefa)
            escritor.newLine()
    finally:
        escritor.close()

    print("Arquivo criado em: %s" % arquivo.getAbsolutePath())
    print("Conteudo lido usando classes Java:")

    leitor = BufferedReader(FileReader(arquivo))
    try:
        linha = leitor.readLine()
        while linha is not None:
            print("- %s" % linha)
            linha = leitor.readLine()
    finally:
        leitor.close()


if __name__ == "__main__":
    main()
