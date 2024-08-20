class Ejercicio3_1:

    '''----------------------------------
    atributos
    ----------------------------------'''

    def __init__ (self, valor1, valor2):
        self.__valor1 = valor1
        self.__valor2 = valor2
        self.__mayor = self.determinar_mayor()

    '''-------------------------------------------
    metodos
    -------------------------------------------'''

    def determinar_mayor(self):
        if self.__valor1 > self.__valor2:
            return self.__valor1
        elif self.__valor2 > self.__valor1:
            return self.__valor2
        else:
            return "Los valores son iguales"

    def obtener_mayor(self):
        return self.__mayor
