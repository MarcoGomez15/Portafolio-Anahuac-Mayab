#ifndef EMPLEADO_H
#define EMPLEADO_H

#include <iostream>
#include <string>

using namespace std;

class Empleado {
private:
    string primerNombre;
    string apellidoPaterno;
    string numeroSeguroSocial;

public:
    Empleado(const string& nombre, const string& apellido, const string& nss) 
        : primerNombre(nombre), apellidoPaterno(apellido), numeroSeguroSocial(nss) {}
    
    virtual ~Empleado() {}

    string getPrimerNombre() const { return primerNombre; }
    string getApellidoPaterno() const { return apellidoPaterno; }
    string getNumeroSeguroSocial() const { return numeroSeguroSocial; }

    virtual double ingresos() const = 0;

    virtual void imprimir() const {
        cout << getPrimerNombre() << " " << getApellidoPaterno()
             << "\nnumero de seguro social: " << getNumeroSeguroSocial();
    }
};

#endif
