#include "../ArchivosDeEncabezado/Biblioteca.h"
#include <iostream>
using namespace std;

int main(){
    Autor obj = Autor("Rasta","Mexicana");
    Libro obj2 = Libro("Como programar en java",2026,obj);
    cout << obj2.toString() << endl;
    return 0;
}