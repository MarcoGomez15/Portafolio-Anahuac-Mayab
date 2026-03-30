#ifndef TRABAJADORPIEZAS_H
#define TRABAJADORPIEZAS_H

#include "Empleado.h"
#include <iomanip>

class TrabajadorPiezas : public Empleado {
private:
    double salario;
    int piezas;

public:
    TrabajadorPiezas(const string& nombre, const string& apellido, const string& nss, double salarioBase, int piezasProd)
        : Empleado(nombre, apellido, nss) {
        setSalario(salarioBase);
        setPiezas(piezasProd);
    }

    void setSalario(double salarioBase) {
        salario = (salarioBase >= 0.0) ? salarioBase : 0.0;
    }

    double getSalario() const { return salario; }

    void setPiezas(int piezasProd) {
        piezas = (piezasProd >= 0) ? piezasProd : 0;
    }

    int getPiezas() const { return piezas; }

    virtual double ingresos() const override {
        return getSalario() * getPiezas();
    }

    virtual void imprimir() const override {
        cout << "trabajador por piezas: ";
        Empleado::imprimir();
        cout << "\nsalario por pieza: $" << fixed << setprecision(2) << getSalario() 
             << "; piezas producidas: " << getPiezas();
    }
};

#endif
