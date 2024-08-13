class Ejercicio2_7:

    '''-----------------------------------------
    Atributos
    -----------------------------------------'''

def __init__(self, litrosProducto, precioPorGalon):
    self.__litrosProducto = litrosProducto
    self.__precioPorGalon = precioPorGalon
    self.__litrosPorGalon = 3.785

    '''------------------------------------
    metodos
    ------------------------------------'''

    def convertirAGalones(self):
        return self.__litrosProducto/self.__litrosPorGalon
    
    def calcularPago(self):
        galones = self.convertirAGalones
        return galones + self.__precioPorGalon