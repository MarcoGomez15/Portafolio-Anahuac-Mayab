#pragma once

class Termometro {
private:
    double temperatura;

public:
    // Constructor por defecto (aleatorio)
    Termometro();

    // Constructor parametrizado
    Termometro(double temp);

    // Métodos para obtener temperaturas
    double TemperaturaC();
    double TemperaturaF();
    double TemperaturaK();

    // Método para mostrar las temperaturas
    void MostrarTemperaturas();
};
