#include "Animales.h"
#include <iostream>
#include <string>

using namespace std;

Mamifero::Mamifero(string n, double p){
    this->nombre = n;
    this->peso = p;
}
void Mamifero::setNombre(string n){
    this->nombre = n;
}
string Mamifero::getNombre(){
    return this->nombre;
}
string Mamifero::toString(){
    return "Mamifero\n [" + nombre + ", " + to_string(peso) + " kg]";
}


// ------------ CLASE GATO -------------

Gato::Gato(string n, double p, int b) : Mamifero(n, p){
    this->nBigotes = b;
}

string Gato::toString(){
    return "Gato\n " + Mamifero::toString() + "\n " + to_string(nBigotes) + " bigotes";
}

// ------------ CLASE VACA -------------

Vaca::Vaca(string n, double p, double l) : Mamifero(n, p){
    this->litrosLeche = l;
}

void Vaca::calcularCantidadComida(){
    cout << peso * 0.03 << " kg de alimento" << endl;
}

string Vaca::toString(){
    return "Vaca\n " + Mamifero::toString() + "\n " + to_string(litrosLeche) + " litros de leche";
}

// ------------ CLASE BALLENA -------------

Ballena::Ballena(string n, double p) : Mamifero(n, p){
}

string Ballena::toString(){
    return "Ballena\n " + Mamifero::toString();
}