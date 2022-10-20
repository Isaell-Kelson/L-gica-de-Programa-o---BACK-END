class Cachorro():   

    
    def __init__(self, nome, peso):
        self.__nome = nome
        self.__peso = peso

    def get_nome(self):
        return self.__nome

    def get_peso(self):
        return self.__peso

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_peso(self, novo_peso):
        self.__peso = novo_peso

c1 = Cachorro('Marley', 10)
print('O nome do seu cachorro é: ', c1.get_nome())
print('O peso do seu cachorro em Kg é: ', c1.get_peso())
print('')

c2 = str(input('Digite outro nome: '))
c1.set_nome(c2)
print('O novo nome do seu cachorro é: ', c1.get_nome())
c3 = str(input('Digite um novo peso: '))
c1.set_peso(c3)
print('O novo peso do seu cachorro é: ', c1.get_peso())