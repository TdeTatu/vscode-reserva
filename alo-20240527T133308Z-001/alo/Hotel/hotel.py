from abc import abstractmethod
from datetime import datetime

class Hospede:
    def __init__(self, id, nome, endereco, telefone, email, documento):
        self.__id = id
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email
        self.__documento = documento

    #GET

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getTelefone(self):
        return self.__telefone

    def getEmail(self):
        return self.__email

    def getDocumento(self):
        return self.__documento   

    #SET

    def setId(self, id):
        self.__id = id

    def setNome(self, nome):
        self.__nome = nome

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def setEmail(self, email):
        self.__email = email

    def setDocumento(self, documento):
        self.__documento = documento
    
    @abstractmethod
    def profile(self):
        pass

class Quarto:
    def __init__(self, numero, tipo, diaria, capacidade, disponibilidade):
        self.__numero = numero
        self.__tipo = tipo
        self.__diaria = diaria
        self.__capacidade = capacidade
        self.__disponibilidade = disponibilidade

#GET
    def getNumero(self):
        return self.__numero

    def getTipo(self):
        return self.__tipo

    def getDiaria(self):
        return self.__diaria

    def getCapacidade(self):
        return self.__capacidade

    def getDisponibilidade(self):
        return self.__disponibilidade   
#SET

    def setNumero(self, numero):
        self.__numero = numero

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setDiaria(self, diaria):
        self.__diaria = diaria

    def setCapacidade(self, capacidade):
        self.__capacidade = capacidade

    def setDisponibilidade(self, disponibilidade):
        self.__disponibilidade =  disponibilidade
    
    @abstractmethod
    def profile(self):
        pass

class Reserva:
    def __init__(self, idmed, dataEntrada, dataSaída, valor, formaPagamento):
        self.__idmed = idmed
        self.__dataEntrada = dataEntrada
        self.__dataSaída = dataSaída
        self.__valor = valor
        self.__formaPagamento = formaPagamento

#GET
    def getIdmed(self):
        return self.__idmed

    def getDataEntrada(self):
        return self.__dataEntrada

    def getDataSaída(self):
        return self.__dataSaída

    def getValor(self):
        return self.__valor

    def getFormaPagamento(self):
        return self.__formaPagamento 

#SET

    def setIdmed(self, idmed):
        self.__idmed = idmed

    def setDataEntrada(self, dataEntrada):
        self.__dataEntrada = dataEntrada

    def setDataSaída(self, dataSaída):
        self.__dataSaída = dataSaída

    def setValor(self, valor):
        self.__valor = valor

    def setFormaPagamento(self, formaPagamento):
        self.__formaPagamento =  formaPagamento
    
    @abstractmethod
    def profile(self):
        pass

h1 = Hospede(12, 'Bernardo Silva', 'Weeblandia', '6199954557', 'nadinho69@gmail.com', 'CPF-3362535')
q1 = Quarto(110, 'Suíte-Solteio', 119.99, 2, True)
r1 = Reserva(5678, datetime.now(), datetime.now(), 219.00, 'Crédito')

print(H1.getNome())
print(q1.getNumero())
print(r1.getFormaPagamento())