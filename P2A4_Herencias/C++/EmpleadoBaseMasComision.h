#ifndef EMPLEADOBASEMASCOMISION_H
#define EMPLEADOBASEMASCOMISION_H

#include "EmpleadoPorComision.h"
#include <iomanip>

class EmpleadoBaseMasComision : public EmpleadoPorComision {
private:
    double salarioBase;

public:
    EmpleadoBaseMasComision(const string& nombre, const string& apellido, const string& nss, double ventas, double tarifa, double salario)
        : EmpleadoPorComision(nombre, apellido, nss, ventas, tarifa) {
        setSalarioBase(salario);
    }

    void setSalarioBase(double salario) {
        salarioBase = (salario >= 0.0) ? salario : 0.0;
    }

    double getSalarioBase() const { return salarioBase; }

    virtual double ingresos() const override {
        return getSalarioBase() + EmpleadoPorComision::ingresos();
    }

    virtual void imprimir() const override {
        cout << "con salario base ";
        EmpleadoPorComision::imprimir();
        cout << "; salario base: $" << fixed << setprecision(2) << getSalarioBase();
    }
};

#endif
