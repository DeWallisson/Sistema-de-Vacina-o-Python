from Elemento import Elemento

class Pilha:
    def __init__(self):
        self.primeiro = None
    
    def criarNovoElemento(self, valor):
        return Elemento(valor, None)

    def empilhar(self, valor):
        novo = self.criarNovoElemento(valor)
        if self.primeiro is not None:
            novo.proximo = self.primeiro
        self.primeiro = novo

    def desempilhar(self):
        if self.primeiro is not None:
            aux = self.primeiro
            valor = aux.valor
            self.primeiro = self.primeiro.proximo
            del(aux)
            return valor
        return None

class Fila:
    def __init__(self):
        self.primeiro = None

    def criarNovoElemento(self, valor):
        return Elemento(valor, None)

    def enfileirar(self, valor):
        if self.primeiro is not None:
            aux = self.primeiro
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = self.criarNovoElemento(valor)
        else:
            self.primeiro = self.criarNovoElemento(valor)

    def desenfileirar(self):
        if self.primeiro is not None:
            aux = self.primeiro
            valor = aux.valor
            self.primeiro = self.primeiro.proximo
            del(aux)
            return valor
        return None

    def imprimeFila(self):
        aux = self.primeiro
        if aux is not None:
            while aux is not None:
                print(f"Nome: {aux.valor['nome']} | CPF: {aux.valor['cpf']}")
                aux = aux.proximo
        else:
            print("--- Fila Vazia ---")
            