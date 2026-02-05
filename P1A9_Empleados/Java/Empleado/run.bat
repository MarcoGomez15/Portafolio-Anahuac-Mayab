@echo off
echo Compilando...
javac Empleado.java testEmpleado.java
if %errorlevel% neq 0 (
    echo Error de compilacion.
    pause
    exit /b
)

echo Ejecutando...
echo ---------------------------------------------------
java testEmpleado
echo ---------------------------------------------------
pause
