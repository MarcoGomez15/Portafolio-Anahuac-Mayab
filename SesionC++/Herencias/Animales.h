#pragma once
#include <iostream>
#include <string>

using namespace std;

class Mamifero {
private:
    string nombre;
protected:
    double peso;
public:
    Mamifero(string n, double p);
    void setNombre(string);
    string getNombre();
    string toString();
};

class Gato : public Mamifero {
private:
    int nBigotes;
public:
   Gato(string, double, int);
   string toString();
};

class Vaca : public Mamifero {
private:
    double litrosLeche;
public:
    Vaca(string, double, double);
    void calcularCantidadComida();
    string toString();
};

class Ballena : public Mamifero {
public:
    Ballena(string, double);
    string toString();
};
