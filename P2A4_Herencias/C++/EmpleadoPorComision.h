#ifndef EMPLEADOPORCOMISION_H
#define EMPLEADOPORCOMISION_H

#include "Empleado.h"
#include <iomanip>

class EmpleadoPorComision : public Empleado {
private:
    double ventasBrutas;
    double tarifaComision;

public:
    EmpleadoPorComision(const string& nombre, const string& apellido, const string& nss, double ventas, double tarifa)
        : Empleado(nombre, apellido, nss) {
        setVentasBrutas(ventas);
        setTarifaComision(tarifa);
    }

    void setVentasBrutas(double ventas) {
        ventasBrutas = (ventas >= 0.0) ? ventas : 0.0;
    }

    double getVentasBrutas() const { return ventasBrutas; }

    void setTarifaComision(double tarifa) {
        tarifaComision = (tarifa > 0.0 && tarifa < 1.0) ? tarifa : 0.0;
    }

    double getTarifaComision() const { return tarifaComision; }

    virtual double ingresos() const override {
        return getTarifaComision() * getVentasBrutas();
    }

    virtual void imprimir() const override {
        cout << "empleado por comision: ";
        Empleado::imprimir();
        cout << "\nventas brutas: $" << fixed << setprecision(2) << getVentasBrutas() 
             << "; tarifa de comision: " << getTarifaComision();
    }
};

#endif
