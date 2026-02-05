#include "../Archivos_Encabezado/empleado.h"
#include <iostream>
using namespace std;

int main(){
    empleado e1;
    empleado e2("Juan", 2022, 1000);
    cout << "------------" << endl;
    cout << e1.toString() << endl;
    cout << "------------" << endl;
    cout << e2.toString() << endl;
    cout << "------------" << endl;

    //Solicitar datos al usuario
    string nombre;
    int anioDeContratacion;
    double salario;

    cout << "Ingrese el nombre: ";
    getline(cin, nombre);

    cout << "Ingrese el anio de contratacion: ";
    cin >> anioDeContratacion;

    cout << "Ingrese el salario: ";
    cin >> salario;

    cout << "------------" << endl;
    empleado e3(nombre, anioDeContratacion, salario);
    cout << e3.toString() << endl;
    cout << "------------" << endl;

    return 0;
}
