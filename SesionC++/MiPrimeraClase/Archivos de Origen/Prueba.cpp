#include "../Archivos de Encabezado/MiPrimeraClase.h"
#include <iostream>
using namespace std;

int main() {

  // Para acceder a los atributos y metodos de la clase Usuario
  // Se requiere crear un objeto (Instancia de clase)

  // Declaracion de un objeto
  // nombreClase nombreObjeto();
  Usuario maestra;
  Usuario alumno("Tom", "Cruise", 64);

  // Asignar valores a los atributos
  maestra.setNombre("Lizbeth");
  maestra.setApellidos("Hernandez Olan");
  maestra.setEdad(42);

  // LLamada (invocacion) de metodos
  maestra.iniciarSesion();
  maestra.cerrarSesion();
  maestra.hacerReporte();

  cout << endl;

  alumno.iniciarSesion();
  alumno.cerrarSesion();
  alumno.hacerReporte();

  return 0;
}