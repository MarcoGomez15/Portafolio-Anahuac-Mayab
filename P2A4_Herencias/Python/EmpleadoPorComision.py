from Empleado import Empleado

class EmpleadoPorComision(Empleado):
    def __init__(self, nombre, apellido, nss, ventas, tarifa):
        super().__init__(nombre, apellido, nss)
        self.ventas_brutas = ventas
        self.tarifa_comision = tarifa

    @property
    def ventas_brutas(self):
        return self._ventas_brutas

    @ventas_brutas.setter
    def ventas_brutas(self, ventas):
        self._ventas_brutas = ventas if ventas >= 0.0 else 0.0

    @property
    def tarifa_comision(self):
        return self._tarifa_comision

    @tarifa_comision.setter
    def tarifa_comision(self, tarifa):
        self._tarifa_comision = tarifa if 0.0 < tarifa < 1.0 else 0.0

    def ingresos(self):
        return self.tarifa_comision * self.ventas_brutas

    def __str__(self):
        return f"empleado por comision: {super().__str__()}\nventas brutas: ${self.ventas_brutas:,.2f}; tarifa de comision: {self.tarifa_comision:.2f}"
