"""
Exemplo 2: criacao de threads da JVM a partir de codigo Python/Jython.
Executar com Jython.
"""

from java.lang import Runnable, Thread
from java.text import SimpleDateFormat
from java.util import Date


class Trabalhador(Runnable):

    def __init__(self, nome):
        self.nome = nome

    def run(self):
        formato = SimpleDateFormat("HH:mm:ss.SSS")

        for etapa in range(1, 4):
            horario = formato.format(Date())
            print("[%s] %s executando etapa %d" % (horario, self.nome, etapa))
            Thread.sleep(300)


def main():
    nomes = ["Thread-A", "Thread-B", "Thread-C"]
    threads = []

    for nome in nomes:
        thread = Thread(Trabalhador(nome), nome)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Todas as threads da JVM finalizaram.")


if __name__ == "__main__":
    main()
