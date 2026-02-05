#include "../Archivos_Encabezado/empleado.h"
using namespace std;

//Definir los constructores
empleado::empleado(){
    this->nombre = "";
    this->anioDeContratacion = 0;
    this->salario = 0.0;
}

empleado::empleado(string n, int a, double e){
    this->nombre = n;
    this->anioDeContratacion = a;
    this->salario = e;
}

//Getters y setters
string empleado::getNombre(){
    return this->nombre;
}

int empleado::getAnioDeContratacion(){
    return this->anioDeContratacion;
}

double empleado::getSalario(){
    return this->salario;
}

void empleado::setNombre(string n){
    this->nombre = n;
}

void empleado::setAnioDeContratacion(int a){
    this->anioDeContratacion = a;
}

void empleado::setSalario(double e){
    this->salario = e;
}

//Metodos

double empleado::calcularSalario(){
    return this->salario;
}

string empleado::toString(){
    return "Nombre: " + this->nombre + "\nAnio de contratacion: " + to_string(this->anioDeContratacion) + "\nSalario:" + to_string(this->salario);
}
