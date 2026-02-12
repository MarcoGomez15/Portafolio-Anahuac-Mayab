#include "../ArchivosEncabezado/Cuenta.h"
#include <iostream>

using namespace std;

Cuenta::Cuenta(string nombreCuenta, double saldoInicial)
    : nombre(nombreCuenta) {
    if (saldoInicial > 0.0) {
        saldo = saldoInicial;
    } else {
        saldo = 0.0;
    }
}

void Cuenta::depositar(double monto) {
    if (monto > 0.0) {
        saldo += monto;
    }
}

double Cuenta::getSaldo() const {
    return saldo;
}

void Cuenta::setNombre(string nombreCuenta) {
    nombre = nombreCuenta;
}

string Cuenta::getNombre() const {
    return nombre;
}
