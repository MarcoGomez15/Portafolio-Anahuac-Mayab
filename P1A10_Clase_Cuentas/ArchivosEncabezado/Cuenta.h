#ifndef CUENTA_H
#define CUENTA_H

#include <string>

class Cuenta {
public:
    Cuenta(std::string nombreCuenta, double saldoInicial);
    void depositar(double monto);
    double getSaldo() const;
    void setNombre(std::string nombreCuenta);
    std::string getNombre() const;
private:
    std::string nombre;
    double saldo;
};

#endif