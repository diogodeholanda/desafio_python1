class Biciclieta:
    def __init__ (self, cor, modelo, ano, valor):#método construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print ("plim plim...")
    
    def parar(self):
        print ("parando a bicicleta...")
        print ("Bicicleta parada!")

    def correr(self):
        print ("Vrummmm...")


b1 = Biciclieta ("vermelha", "caloi", 2022, 600)#instância da classe
b1.buzinar()
b1.correr()
b1.parar()


