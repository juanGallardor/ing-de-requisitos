class Ejercicio2_5:

    '''-----------------------------------
    Atributos
    -----------------------------------'''

    A=" "
    B=" "
    C=" "

    '''---------------------------------
    METODOS
    ---------------------------------'''
    
    def CalcularAreaTotal(self):
        AreaTriangulo=(self.A * self.B)/2
        AreaRectangulo=self.A * self.C
        AreaTotal= AreaTriangulo + AreaRectangulo

        return AreaTotal