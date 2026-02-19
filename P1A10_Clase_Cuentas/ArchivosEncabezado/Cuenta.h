#pragma once
#include <string>
using namespace std;

class Cuenta {
public:
    Cuenta(string nombreCuenta, double saldoInicial);
    void depositar(double monto);
    double getSaldo() const;
    void setNombre(string nombreCuenta);
    string getNombre() const;
private:
    string nombre;
    double saldo;
};