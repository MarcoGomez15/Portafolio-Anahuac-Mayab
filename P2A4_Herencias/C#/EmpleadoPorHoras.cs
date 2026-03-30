using System;

public class EmpleadoPorHoras : Empleado
{
    private double sueldo;
    private double horas;

    public EmpleadoPorHoras(string nombre, string apellido, string nss, double sueldoPorHoras, double horasTrabajadas)
        : base(nombre, apellido, nss)
    {
        Sueldo = sueldoPorHoras;
        Horas = horasTrabajadas;
    }

    public double Sueldo
    {
        get { return sueldo; }
        set { sueldo = (value >= 0.0) ? value : 0.0; }
    }

    public double Horas
    {
        get { return horas; }
        set { horas = (value >= 0.0 && value <= 168.0) ? value : 0.0; }
    }

    public override double Ingresos()
    {
        if (Horas <= 40)
            return Sueldo * Horas;
        else
            return 40 * Sueldo + (Horas - 40) * Sueldo * 1.5;
    }

    public override string ToString()
    {
        return $"empleado por horas: {base.ToString()}\nsueldo por hora: {Sueldo:C}; horas trabajadas: {Horas:F2}";
    }
}
