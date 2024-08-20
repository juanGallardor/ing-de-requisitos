class Ejercicio2_10:

    '''-----------------------------------------------------
    atributos
    -----------------------------------------------------'''

    def __init__(self, valor, unidadOrigen="metros", unidadDestino="pulgadas"):
        self.__valor = valor
        self.__unidadOrigen = unidadOrigen
        self.__unidadDestino = unidadDestino
        self.__conversion = self.obtener_factor_conversion()

    '''----------------------------------------
    metodos
    ----------------------------------------'''


    def obtener_factor_conversion(self):
        if self.__unidadOrigen == "metros" and self.__unidadDestino == "pulgadas":
            return 39.37
        else:
            return "valores erroneos"

    def convertir(self):
        resultado = self.__valor * self.__conversion
        return resultado
