#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include "../ArchivosE/Termometro.h" 

using namespace std;

// Constructor por defecto: temperatura aleatoria entre 0 y 100
Termometro::Termometro() {
    // Inicializar la semilla aleatoria (en un programa real, esto debería hacerse una sola vez en main, 
    // pero para este ejemplo autocontenido lo hacemos aquí con cuidado o usamos un generador moderno)
    // Para simplificar y seguir el estilo académico:
    double aleatorio = (double)rand() / RAND_MAX; // 0.0 a 1.0
    temperatura = aleatorio * 100.0;
}

// Constructor parametrizado
Termometro::Termometro(double temp) {
    temperatura = temp;
}

double Termometro::TemperaturaC() {
    return temperatura;
}

double Termometro::TemperaturaF() {
    return (temperatura * 9.0 / 5.0) + 32.0;
}

double Termometro::TemperaturaK() {
    return temperatura + 273.15;
}

void Termometro::MostrarTemperaturas() {
    cout << fixed << setprecision(2);
    cout << "Temperatura en Celsius:    " << TemperaturaC() << " °C" << endl;
    cout << "Temperatura en Fahrenheit: " << TemperaturaF() << " °F" << endl;
    cout << "Temperatura en Kelvin:     " << TemperaturaK() << " K" << endl;
}
