from abc import abstractmethod

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def happyBday(self):
        # fazer anaiversário
        self.setAge(self.__age + 1)
        print(f'{self.getName()} tem {self.getAge()} anos.')

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getGender(self):
        return self.__gender

    def setName(self, nome):
        self.__name = nome

    def setAge(self, idade):
        self.__age = idade

    def setGender(self, sexo):
        self.__gender = sexo
    
    @abstractmethod
    def profile(self):
        pass


class Employee(Person):
    def __init__(self, name, age, gender, sector, working):
        super().__init__(name, age, gender)
        self.__sector = sector
        self.__working = working

    def getSector(self):
        return self.__sector

    def getWork(self):
        return self.__working

    def setSector(self, setor):
        self.__sector = setor

    def setWork(self, trabalhando):
        self.__working = trabalhando

    def profile(self):
        print(f'<<<<<<< PROFILE >>>>>>>\nName: {self.getName()}\nAge: {self.getAge()}\nGender: {self.getGender()}\nSector: {self.getSector()}\nWorking: {self.getWork()}\n')

    def changeWork(self):
        # mudar de emprego
        self.setWork(False)


e1 = Employee('Antonio Joaquim', 39, 'Masculino', 'Tecnologia da informação', True)
p1 = Person('Maria Nonata', 71, 'Femninino')

print(e1.profile())
print(p1.getName())