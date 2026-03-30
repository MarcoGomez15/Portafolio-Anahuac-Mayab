#include <iostream>
#include <vector>
#include <typeinfo>
#include "EmpleadoAsalariado.h"
#include "EmpleadoPorHoras.h"
#include "EmpleadoPorComision.h"
#include "EmpleadoBaseMasComision.h"
#include "TrabajadorPiezas.h"

using namespace std;

int main() {
    EmpleadoAsalariado e1("John", "Smith", "111-11-1111", 800.00);
    EmpleadoPorHoras e2("Karen", "Price", "222-22-2222", 16.75, 40);
    EmpleadoPorComision e3("Sue", "Jones", "333-33-3333", 10000, 0.06);
    EmpleadoBaseMasComision e4("Bob", "Lewis", "444-44-4444", 5000, 0.04, 300);
    TrabajadorPiezas e5("Jane", "Doe", "555-55-5555", 2.50, 200);

    cout << "Empleados procesados por separado:\n\n";

    e1.imprimir(); cout << "\ningresos: $" << fixed << setprecision(2) << e1.ingresos() << "\n\n";
    e2.imprimir(); cout << "\ningresos: $" << fixed << setprecision(2) << e2.ingresos() << "\n\n";
    e3.imprimir(); cout << "\ningresos: $" << fixed << setprecision(2) << e3.ingresos() << "\n\n";
    e4.imprimir(); cout << "\ningresos: $" << fixed << setprecision(2) << e4.ingresos() << "\n\n";
    e5.imprimir(); cout << "\ningresos: $" << fixed << setprecision(2) << e5.ingresos() << "\n\n";

    vector<Empleado*> empleados(5);
    empleados[0] = &e1;
    empleados[1] = &e2;
    empleados[2] = &e3;
    empleados[3] = &e4;
    empleados[4] = &e5;

    cout << "Empleados procesados en forma polimorfica:\n\n";

    for (size_t i = 0; i < empleados.size(); ++i) {
        empleados[i]->imprimir();
        
        EmpleadoBaseMasComision* derivedPtr = dynamic_cast<EmpleadoBaseMasComision*>(empleados[i]);
        if (derivedPtr != nullptr) {
            double oldBaseSalary = derivedPtr->getSalarioBase();
            derivedPtr->setSalarioBase(oldBaseSalary * 1.10);
            cout << "\nnuevo salario base con 10% de aumento es: $" << fixed << setprecision(2) << derivedPtr->getSalarioBase();
        }
        
        cout << "\ningresos $" << fixed << setprecision(2) << empleados[i]->ingresos() << "\n\n";
    }

    for (size_t i = 0; i < empleados.size(); ++i) {
        string tname = typeid(*empleados[i]).name();
        string proper_name;
        for (char c : tname) {
            if (!isdigit(c)) proper_name += c;
        }
        cout << "El empleado " << i << " es un " << proper_name << "\n";
    }

    return 0;
}
