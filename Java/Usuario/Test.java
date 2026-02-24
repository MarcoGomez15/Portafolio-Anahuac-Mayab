package Java.Usuario;
import javax.swing.JOptionPane; //Ventanas graficas para recibir/mostrar datos

public class Test {

    public static void main(String[] args) {
        //nombreClase nombreObjeto = new nombreClase();
        Usuario maestra = new Usuario();
        String no = JOptionPane.showInputDialog(null, "Introduce el nombre", "Objeto maestra", 1);
        String ap = JOptionPane.showInputDialog(null, "Introduce el apellido", "Objeto maestra", 1);
        int ed = Integer.parseInt(JOptionPane.showInputDialog(null, "Introduce la edad", "Objeto maestra", 1));

        //Asignar valores a los atributos
        maestra.nombre = no;
        maestra.apellido = ap;
        maestra.edad = ed;

        //Llamada (invocacion) de metodos
        JOptionPane.showMessageDialog(null, maestra.iniciarSesion());
        JOptionPane.showMessageDialog(null, maestra.hacerReporte());
        JOptionPane.showMessageDialog(null, maestra.cerrarSesion());

        Usuario alumno = new Usuario("Tom","Cruise",64);

        JOptionPane.showMessageDialog(null, alumno.iniciarSesion());
        JOptionPane.showMessageDialog(null, alumno.hacerReporte());
        JOptionPane.showMessageDialog(null, alumno.cerrarSesion());

        //Asignar valores a los atributos
        //maestra.nombre = "";
        //maestra.apellido = "";
        //maestra.edad = 0;
        
        

        //Llamada (invocacion) de metodos
        //maestra.iniciarSesion();
        //maestra.hacerReporte();
        //maestra.cerrarSesion();
        
        System.out.println("");
        
        //alumno.iniciarSesion();
        //alumno.hacerReporte();
        //alumno.cerrarSesion();
        
    }
}
