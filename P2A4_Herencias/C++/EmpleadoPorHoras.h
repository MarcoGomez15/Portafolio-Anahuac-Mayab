#ifndef EMPLEADOPORHORAS_H
#define EMPLEADOPORHORAS_H

#include "Empleado.h"
#include <iomanip>

class EmpleadoPorHoras : public Empleado {
private:
    double sueldo;
    double horas;

public:
    EmpleadoPorHoras(const string& nombre, const string& apellido, const string& nss, double sueldoPorHoras, double horasTrabajadas)
        : Empleado(nombre, apellido, nss) {
        setSueldo(sueldoPorHoras);
        setHoras(horasTrabajadas);
    }

    void setSueldo(double sueldoPorHoras) {
        sueldo = (sueldoPorHoras >= 0.0) ? sueldoPorHoras : 0.0;
    }

    double getSueldo() const { return sueldo; }

    void setHoras(double horasTrabajadas) {
        horas = (horasTrabajadas >= 0.0 && horasTrabajadas <= 168.0) ? horasTrabajadas : 0.0;
    }

    double getHoras() const { return horas; }

    virtual double ingresos() const override {
        if (horas <= 40)
            return sueldo * horas;
        else
            return 40 * sueldo + (horas - 40) * sueldo * 1.5;
    }

    virtual void imprimir() const override {
        cout << "empleado por horas: ";
        Empleado::imprimir();
        cout << "\nsueldo por hora: $" << fixed << setprecision(2) << getSueldo() 
             << "; horas trabajadas: " << getHoras();
    }
};

#endif
