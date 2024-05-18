class Pessoa():
    def __init__(self, nome: str, idade: int, peso: float, estado: False):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.estado = estado

    def comer(self, alimento):
        #Só posso comer se não estiver comendo,andando,falando.
        if self.estado == False:
            print(f'{self.nome} está comendo. {alimento}')
            self.estado = True
        else:
            print(f'{self.nome} não pode comer. Verifique se ele(a) ja esta comendo,andando, ou falando.')

    def pararDeComer(self):
        #Só posso parar de comer se estiver comendo.
        if self.estado == True:
            print(f'{self.nome} parou de comer.')
            self.estado = False
        else:
            print(f'{self.nome} Não pode parar de comer pois ele não esta comendo nada.')

    def andar(self):
        #Só posso andar se não estiver andando,comendo,falando.
        if self.estado == False:
            print(f'{self.nome} está andando')
            self.estado = True
        else:
            print(f'{self.nome} não pode andar. Verifique se ele(a) ja está andando,comendo ou falando')

    def pararDeAndar(self):
        #Só posso parar de andar se estiver andando
        if self.estado == True:
            print(f'{self.nome} parou de andar.')
            self.estado = False
        else:
            print(f'{self.nome} Não pode parar de andar pois ele ja está parado.')

    def falar(self,frase):
        #Só posso falar se não estiver falando,comendo,andando.
        if self.estado == False:
            print(f'{self.nome} está falando. {frase}')
            self.estado = True
        else:
            print(f'{self.nome} não pode falar. Verifique se ele(a) ja está falando,comendo ou andando')

    def pararDeFalar(self):
        #Só posso parar de falar se estiver falando
        if self.estado == True:
            print(f'{self.nome} parou de falar.')
            self.estado = False
        else:
            print(f'{self.nome} Não pode parar de falar pois ele ja está calado.')







