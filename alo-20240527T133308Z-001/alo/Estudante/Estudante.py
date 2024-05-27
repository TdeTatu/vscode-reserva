from abc import abstractmethod
from datetime import datetime

class Usuario:
    def __init__(self, nome, endereco, telefone, email, numeroDocumento, dataNascimento):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email
        self.__numeroDocumento = numeroDocumento
        self.__dataNascimento = dataNascimento

    #GET

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getTelefone(self):
        return self.__telefone

    def getEmail(self):
        return self.__email

    def getNumeroDocumento(self):
        return self.__numeroDocumento

    def getDataNascimento(self):
        return self.__dataNascimento

    #SET

    def setNome(self, nome):
        self.__nome = nome

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def setEmail(self, email):
        self.__email = email

    def setNumeroDocumento(self, numeroDocumento):
        self.__numeroDocumento = numeroDocumento

    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento
    
    @abstractmethod
    def profile(self):
        pass

class Emprestimo:
    def __init__(self, numeroIdentificacao, dataEmprestimo, dataDevolucaoPrevista, status):
        self.__numeroIdentificacao = numeroIdentificacao
        self.__dataEmprestimo = dataEmprestimo
        self.__dataDevolucaoPrevista =  dataDevolucaoPrevista
        self.__status = status

    #GET

    def getNumeroIdentificacao(self):
        return self.__numeroIdentificacao

    def getDataEmprestimo(self):
        return self.__dataEmprestimo

    def getDataDevolucaoPrevista(self):
        return self.__dataDevolucaoPrevista

    def getStatus(self):
        return self.__status
    
    #SET

    def setNumeroIdentificacao(self, numeroIdentificacao):
        self.__numeroIdentificacao = numeroIdentificacao

    def setDataEmprestimo(self, dataEmprestimo):
        self.__dataEmprestimo = dataEmprestimo

    def setDataDevolucaoPrevista(self, dataDevolucaoPrevista):
        self.__dataDevolucaoPrevista = dataDevolucaoPrevista

    def setStatus(self, status):
        self.__status = status

    @abstractmethod
    def profile(self):
        pass

class Livro:
    def __init__(self, titulo, autor, genero, editora, isbn, resumo, capa, disponibilidade):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__editora = editora
        self.__isbn = isbn
        self.__resumo = resumo
        self.__capa = capa
        self.__disponibilidade = disponibilidade
    
    #GET

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getGenero(self):
        return self.__genero

    def getEditora(self):
        return self.__editora

    def getIsbn(self):
        return self.__isbn

    def getResumo(self):
        return self.__resumo
    
    def getCapa(self):
        return self.__capa
    
    def getDisponibilidade(self):
        return self.__disponibilidade

    #SET

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setAutor(self, autor):
        self.__autor = autor

    def setGenero(self, genero):
        self.__genero = genero

    def setEditora(self, editora):
        self.__editora = editora

    def setIsbn(self, isbn):
        self.__isbn = isbn

    def setResumo(self, resumo):
        self.__resumo = resumo

    def setCapa(self, capa):
        self.__capa = capa

    def setDisponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade
    
    @abstractmethod
    def profile(self):
        pass

class Avaliacao:
    def __init__(self, nota, comentario):
        self.__nota = nota
        self.__comentario = comentario

    #GET

    def getNota(self):
        return self.__nota
    
    def getComentario(self):
        return self.__comentario

    #SET

    def setNota(self, nota):
        self.__nota = nota

    def setComentario(self, comentario):
        self.__comentario = comentario    

    @abstractmethod
    def profile(self):
        pass

class Relatorio:
    def __init__(self, dados):
        self.__dados = dados

    #GET

    def getDados(self):
        return self.__dados

    #SET    

    def setDados(self, dados):
        self.__dados = dados

    @abstractmethod
    def profile(self):
        pass

class SistemaBibliotecaInfoUser(Usuario, Emprestimo):
    def __init__(self, nome, numeroDocumento, numeroIdentificacao, status, dataEmprestimo, dataDevolucao):
        super().__init__(nome, numeroDocumento, numeroIdentificacao, status, dataEmprestimo, dataDevolucao)

    def sistemau(self):
        print(f"<<<<<<Sistema biblioteca Readers>>>>>>\n!!!Perfil!!!\nUsuário: {self.getNome()}\nDocumento: {self.getNumeroDocumento()}\n!!!INFO!!!\nId-Emprestimo: {self.getNumeroIdentificacao()}\nStatus: {self.getStatus()}\nData-Emprestimo: {self.getDataEmprestimo()}\nLimite-Devolução: {self.getDataDevolucaoPrevista()}\n")

class SistemaBibliotecaInfoLivro(Livro, Avaliacao):
    def __init__(self, titulo, autor, genero, nota, comentario):
        super().__init__(titulo, autor, genero, nota, comentario)

    def sistemal(self):
        print(f"!!!Livro!!!\nTitulo: {self.getTitulo()}\nAutor: {self.getAutor()}\nGenero: {self.getGenero()}\nNota: {self.getNota()}\nReview: {self.getComentario()}\n <<<<<< FIM >>>>>>")

testesistemauser = SistemaBibliotecaInfoUser('Lucas Althoff', '085-193-072-77', '40028922', 'Alugado', datetime.now(), '02/06/2024')
testesistemalivro = SistemaBibliotecaInfoLivro('O labirinto do Fauno', 'Guillermo del Toro & Cornelia Funke', 'Fantasia, Sobrenatural', 100, 'Uma história emocionante e mirabolante para exercitar o coração e a imaginação')

print(testesistemauser.sistemau())
print(testesistemalivro.sistemal())
