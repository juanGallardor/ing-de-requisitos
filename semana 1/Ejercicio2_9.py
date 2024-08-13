class Ejercicio2_9:
    
    '''-------------------------------
    atributos
    -------------------------------'''

    def __init__(self, horasTrabajadas, PagoPorHora):
        self.__horasTrabajadas = horasTrabajadas
        self.__pagoPorHora = PagoPorHora

    '''-------------------------------
    metodos
    -------------------------------'''

    def calcularSueldoSemanal(self):
        return self.__horasTrabajadas + self.__pagoPorHora

