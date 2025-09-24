from collections import deque
import time

class Impressora:
    def __init__(self):
        self.fila = deque()

    def adicionar_documento(self, documento):
        self.fila.append(documento)
        print(f"Documento '{documento}' adicionado à fila.")

    def imprimir(self):
        if self.fila:
            documento = self.fila.popleft()
            print(f"Imprimindo: {documento}...")
            time.sleep(1)  
            print(f"Documento '{documento}' impresso com sucesso!\n")
        else:
            print("Nenhum documento na fila para imprimir.\n")

    def status_fila(self):
        if self.fila:
            print("Fila de impressão:", list(self.fila))
        else:
            print("Fila de impressão vazia.")


impressora = Impressora()

impressora.adicionar_documento("Trabalho de Matemática")
impressora.adicionar_documento("Relatório de Vendas")
impressora.adicionar_documento("Certificado")

impressora.status_fila()


impressora.imprimir()
impressora.imprimir()

impressora.status_fila()
impressora.imprimir()
impressora.imprimir()  