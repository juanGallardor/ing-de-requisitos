class Ejercicio2_11:

    '''----------------------------------
    atributos
    ----------------------------------'''

    def __init__ (self, largo, ancho, altura, costoPorMetroCubico):
        self.__largo = largo
        self.__ancho = ancho
        self.__altura = altura
        self.__costoPorMetroCubico = costoPorMetroCubico

    '''----------------------------------------
    metodos
    ----------------------------------------'''

    def calcular_volumen(self):
        return self.__largo * self.__ancho * self.__altura

    def calcular_pago(self):
        volumen = self.calcular_volumen()
        return volumen * self.__costoPorMetroCubico
