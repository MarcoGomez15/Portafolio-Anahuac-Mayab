#include <iostream>
#include <ctime>
#include <cstdlib>
#include "../ArchivosE/Termometro.h"

using namespace std;

int main() {
    // Inicializar semilla para números aleatorios una vez al inicio
    srand(time(0));

    // 1. Crear instancia con constructor por defecto (aleatorio)
    cout << "--- Termómetro con valor aleatorio ---" << endl;
    Termometro t1;
    t1.MostrarTemperaturas();

    cout << endl;

    // 2. Pedir temperatura al usuario
    double tempUsuario;
    cout << "Introduce una temperatura en Celsius: ";
    if (cin >> tempUsuario) {
        // 3. Crear instancia con constructor parametrizado
        cout << "\n--- Termómetro con valor del usuario ---" << endl;
        Termometro t2(tempUsuario);
        t2.MostrarTemperaturas();
    } else {
        cout << "Entrada no válida. Se esperaba un número." << endl;
    }

    return 0;
}
