from Empleado import Empleado

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, apellido, nss, sueldo_por_horas, horas_trabajadas):
        super().__init__(nombre, apellido, nss)
        self.sueldo = sueldo_por_horas
        self.horas = horas_trabajadas

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo_por_horas):
        self._sueldo = sueldo_por_horas if sueldo_por_horas >= 0.0 else 0.0

    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, horas_trabajadas):
        if 0.0 <= horas_trabajadas <= 168.0:
            self._horas = horas_trabajadas
        else:
            self._horas = 0.0

    def ingresos(self):
        if self.horas <= 40:
            return self.sueldo * self.horas
        else:
            return 40 * self.sueldo + (self.horas - 40) * self.sueldo * 1.5

    def __str__(self):
        return f"empleado por horas: {super().__str__()}\nsueldo por hora: ${self.sueldo:,.2f}; horas trabajadas: {self.horas:.2f}"
