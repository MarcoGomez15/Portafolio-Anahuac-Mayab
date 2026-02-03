#include "../Archivos de Encabezado/MiPrimeraClase.h"
#include <iostream>
using namespace std;

// Definir los constructores
Usuario::Usuario() {
  this->nombre = "";
  this->apellidos = "";
  this->edad = 0;
}

Usuario::Usuario(string n, string a, int e) {
  this->nombre = n;
  this->apellidos = a;
  this->edad = e;
}
// Definir los setter y getter
void Usuario::setNombre(string n) { this->nombre = n; }
string Usuario::getNombre() { return this->nombre; }
void Usuario::setApellidos(string a) { this->apellidos = a; }
string Usuario::getApellidos() { return this->apellidos; }
void Usuario::setEdad(int e) { this->edad = e; }
int Usuario::getEdad() { return this->edad; }

// Definir los metodos
void Usuario::iniciarSesion() {
  cout << "El usuario " << this->nombre << " esta iniciando sesion." << endl;
}
void Usuario::cerrarSesion() {
  cout << "El usuario " << this->nombre << " a cerrado la sesion." << endl;
}
void Usuario::hacerReporte() {
  cout << "Reporte de usuario" << endl;
  cout << "Nombre completo: " << this->nombre << " " << this->apellidos << endl;
  cout << "Edad: " << this->edad << endl;
}
