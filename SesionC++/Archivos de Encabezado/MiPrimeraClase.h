#pragma once

// Contiene las declaraciones de las clases
#include <string>
using namespace std;

class Usuario {
  // Declaraciones de atributos privado
private:
  string nombre;
  string apellidos;
  int edad;

public:
  // Declaracion de constructores
  Usuario();
  Usuario(string n, string a, int e);

  // Declarar setter y getter
  void setNombre(string n);
  string getNombre();
  void setApellidos(string a);
  string getApellidos();
  void setEdad(int e);
  int getEdad();

  // Declaracion de metodos (funciones)
  void iniciarSesion();
  void cerrarSesion();
  void hacerReporte();
};
