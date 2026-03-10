class Persona:
    def __init__(self, nombre="", apellido="", genero="", edad=0):
        self._nombre = nombre
        self._apellido = apellido
        self._genero = genero
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        self._genero = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    def printPersona(self):
        print(f"Nombre: {self._nombre}")
        print(f"Apellido: {self._apellido}")
        print(f"Género: {self._genero}")
        print(f"Edad: {self._edad}")

class Paciente(Persona):
    def __init__(self, nombre="", apellido="", genero="", edad=0, altura=0.0, peso=0.0):
        super().__init__(nombre, apellido, genero, edad)
        self._altura = altura
        self._peso = peso

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = valor

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        self._peso = valor

    def printPaciente(self):
        self.printPersona()
        print(f"Altura: {self._altura} m")
        print(f"Peso: {self._peso} kg")

    def imc(self):
        if self._altura > 0:
            return self._peso / (self._altura * self._altura)
        return 0.0

class Medico(Persona):
    def __init__(self, nombre="", apellido="", genero="", edad=0, especialidad="", cedulaProfesional=0):
        super().__init__(nombre, apellido, genero, edad)
        self._especialidad = especialidad
        self._cedulaProfesional = cedulaProfesional

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        self._especialidad = valor

    @property
    def cedulaProfesional(self):
        return self._cedulaProfesional

    @cedulaProfesional.setter
    def cedulaProfesional(self, valor):
        self._cedulaProfesional = valor

    def printMedico(self):
        self.printPersona()
        print(f"Especialidad: {self._especialidad}")
        print(f"Cédula Profesional: {self._cedulaProfesional}")

class PacienteExterno(Paciente):
    def __init__(self, nombre="", apellido="", genero="", edad=0, altura=0.0, peso=0.0, noConsultorio=0, horario="", fecha=""):
        super().__init__(nombre, apellido, genero, edad, altura, peso)
        self._noConsultorio = noConsultorio
        self._horario = horario
        self._fecha = fecha

    @property
    def noConsultorio(self):
        return self._noConsultorio

    @noConsultorio.setter
    def noConsultorio(self, valor):
        self._noConsultorio = valor

    @property
    def horario(self):
        return self._horario

    @horario.setter
    def horario(self, valor):
        self._horario = valor

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    def printPacienteExterno(self):
        self.printPaciente()
        print(f"No. Consultorio: {self._noConsultorio}")
        print(f"Horario: {self._horario}")
        print(f"Fecha: {self._fecha}")

    def examenFisico(self):
        print(f"Realizando examen físico al paciente externo {self._nombre} {self._apellido}...")

class PacienteHospitalizado(Paciente):
    def __init__(self, nombre="", apellido="", genero="", edad=0, altura=0.0, peso=0.0, habitacion=0, tipoCirugia=""):
        super().__init__(nombre, apellido, genero, edad, altura, peso)
        self._habitacion = habitacion
        self._tipoCirugia = tipoCirugia

    @property
    def habitacion(self):
        return self._habitacion

    @habitacion.setter
    def habitacion(self, valor):
        self._habitacion = valor

    @property
    def tipoCirugia(self):
        return self._tipoCirugia

    @tipoCirugia.setter
    def tipoCirugia(self, valor):
        self._tipoCirugia = valor

    def printPacienteHospitalizado(self):
        self.printPaciente()
        print(f"Habitación: {self._habitacion}")
        print(f"Tipo de Cirugía: {self._tipoCirugia}")

    def indicaciones(self):
        print(f"Brindando indicaciones médicas post-operatorias para el paciente hospitalizado {self._nombre} {self._apellido}...")
