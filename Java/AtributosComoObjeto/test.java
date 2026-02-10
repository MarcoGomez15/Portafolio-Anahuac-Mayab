package Java.AtributosComoObjeto;

public class test {
    public static void main(String args[]){
        Autor obj = new Autor("Rasta","Mexicana");
        Libro obj2 = new Libro("Como programar en java",2026,obj);
        System.out.println(obj2);
    }
}
