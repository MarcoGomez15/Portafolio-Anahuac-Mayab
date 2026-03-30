from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, apellido, nss):
        self._primer_nombre = nombre
        self._apellido_paterno = apellido
        self._numero_seguro_social = nss

    @property
    def primer_nombre(self):
        return self._primer_nombre

    @property
    def apellido_paterno(self):
        return self._apellido_paterno

    @property
    def numero_seguro_social(self):
        return self._numero_seguro_social

    @abstractmethod
    def ingresos(self):
        pass

    def __str__(self):
        return f"{self.primer_nombre} {self.apellido_paterno}\nnumero de seguro social: {self.numero_seguro_social}"
