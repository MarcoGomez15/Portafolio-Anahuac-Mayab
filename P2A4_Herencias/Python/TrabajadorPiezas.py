from Empleado import Empleado

class TrabajadorPiezas(Empleado):
    def __init__(self, nombre, apellido, nss, salario, piezas):
        super().__init__(nombre, apellido, nss)
        self.salario = salario
        self.piezas = piezas

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario if salario >= 0.0 else 0.0

    @property
    def piezas(self):
        return self._piezas

    @piezas.setter
    def piezas(self, piezas):
        self._piezas = piezas if piezas >= 0 else 0

    def ingresos(self):
        return self.salario * self.piezas

    def __str__(self):
        return f"trabajador por piezas: {super().__str__()}\nsalario por pieza: ${self.salario:,.2f}; piezas producidas: {self.piezas}"
