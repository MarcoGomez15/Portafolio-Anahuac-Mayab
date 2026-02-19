package P1A11_Termometro.Java;

public class Termometro {

    //Atributo privado
    private double temperatura;
    
    //Constructor por defecto
    public Termometro() {
        this.temperatura = Math.random() * 100;
    }

    //Constructor parametrizado
    public Termometro(double temperatura){
        this.temperatura = temperatura;
    }

    //Metodos
    public double getTemperatura(){
        return this.temperatura;
    }

    public double getTemperaturaFahrenheit(){
        return (this.temperatura * 9/5) + 32;
    }

    public double getTemperaturaKelvin(){
        return this.temperatura + 273.15;
    }

    public void mostrarTemperaturas(){
        System.out.printf("Temperatura en Celsius: %.2f%n", this.temperatura);
        System.out.printf("Temperatura en Fahrenheit: %.2f%n", this.getTemperaturaFahrenheit());
        System.out.printf("Temperatura en Kelvin: %.2f%n", this.getTemperaturaKelvin());
    }
}