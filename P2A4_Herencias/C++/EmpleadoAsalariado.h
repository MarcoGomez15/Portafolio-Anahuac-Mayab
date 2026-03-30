#ifndef EMPLEADOASALARIADO_H
#define EMPLEADOASALARIADO_H

#include "Empleado.h"
#include <iomanip>

class EmpleadoAsalariado : public Empleado {
private:
    double salarioSemanal;

public:
    EmpleadoAsalariado(const string& nombre, const string& apellido, const string& nss, double salario)
        : Empleado(nombre, apellido, nss) {
        setSalarioSemanal(salario);
    }

    void setSalarioSemanal(double salario) {
        salarioSemanal = (salario >= 0.0) ? salario : 0.0;
    }

    double getSalarioSemanal() const { return salarioSemanal; }

    virtual double ingresos() const override {
        return getSalarioSemanal();
    }

    virtual void imprimir() const override {
        cout << "empleado asalariado: ";
        Empleado::imprimir();
        cout << "\nsalario semanal: $" << fixed << setprecision(2) << getSalarioSemanal();
    }
};

#endif
