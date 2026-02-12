#include <iostream>
#include <iomanip>
#include "../ArchivosEncabezado/Cuenta.h"

using namespace std;

int main() {
    Cuenta cuenta1("Jane Green", 50.00);
    Cuenta cuenta2("John Blue", -7.53); 

    cout << fixed << setprecision(2);

    cout << "Saldo de " << cuenta1.getNombre() << ": $" << cuenta1.getSaldo() << endl;
    cout << "Saldo de " << cuenta2.getNombre() << ": $" << cuenta2.getSaldo() << endl;

    double monto;

    cout << "\nIngrese el monto del deposito para la cuenta1: ";
    cin >> monto;
    cout << "agregando " << monto << " al saldo de la cuenta1" << endl;
    cuenta1.depositar(monto);

    cout << "\nSaldo de " << cuenta1.getNombre() << ": $" << cuenta1.getSaldo() << endl;
    cout << "Saldo de " << cuenta2.getNombre() << ": $" << cuenta2.getSaldo() << endl;

    cout << "\nIngrese el monto del deposito para la cuenta2: ";
    cin >> monto;
    cout << "agregando " << monto << " al saldo de la cuenta2" << endl;
    cuenta2.depositar(monto);

    cout << "\nSaldo de " << cuenta1.getNombre() << ": $" << cuenta1.getSaldo() << endl;
    cout << "Saldo de " << cuenta2.getNombre() << ": $" << cuenta2.getSaldo() << endl;

    return 0;
}
