import random

class Termometro:
    def __init__(self, temperatura=None):
        # Si temperatura es None, es el constructor por defecto (aleatorio 0-100)
        if temperatura is None:
            self.__temperatura = random.uniform(0, 100)
        # Si tiene valor, es el constructor parametrizado
        else:
            self.__temperatura = float(temperatura)

    def TemperaturaC(self):
        return self.__temperatura

    def TemperaturaF(self):
        return (self.__temperatura * 9/5) + 32

    def TemperaturaK(self):
        return self.__temperatura + 273.15

    def mostrarTemperaturas(self):
        print(f"Temperatura en Celsius:    {self.TemperaturaC():.2f} °C")
        print(f"Temperatura en Fahrenheit: {self.TemperaturaF():.2f} °F")
        print(f"Temperatura en Kelvin:     {self.TemperaturaK():.2f} K")