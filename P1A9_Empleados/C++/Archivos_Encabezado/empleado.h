#pragma once

#include <string>
using namespace std;

class empleado{
 // Declaraciones de mis atributos privados
private:
 string nombre;
 int anioDeContratacion;
 double salario;

public:
 // Declaraciones de constructores
 empleado();
 empleado(string n, int a, double e);

 // Declarar setter y getters
 void setNombre(string n);
 string getNombre();
 void setAnioDeContratacion(int a);
 int getAnioDeContratacion();
 void setSalario(double e);
 double getSalario(); 

 //Declaracion de metodos(funciones)

 double calcularSalario();
 string toString();
};