using System;

public class Test {
    public static void Main(string[] args) {
        Autor obj = new Autor("Rasta","Mexicana");
        
        Libro obj2 = new Libro("Como programar en java",2026,obj);
        Console.WriteLine(obj2);
    }
}