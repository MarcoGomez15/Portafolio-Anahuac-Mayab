from ClaseUsuario import Usuario

# Creación del objeto
# nombreObjeto = nombreClase()
maestra = Usuario()
alumno = Usuario("Tom", "Cruise", 64)

# Asignar valores a los atributos
maestra.apellidos = "Hernandez Olan"
maestra.nombre = "Lizbeth"
maestra.edad = 42

# Llamada (invocación) de métodos
maestra.iniciarSesion()
maestra.cerrarSesion()
maestra.hacerReporte()

print()

alumno.iniciarSesion()
alumno.cerrarSesion()
alumno.hacerReporte()