# Si lo pongo en False el programa imprime sin colores
usar_color = True

REINICIO = "\033[0m"
NEGRITA = "\033[1m"

# Colores que uso en los textos, en rgb
NARANJA = [232, 93, 4]
GRIS = [150, 148, 150]
VERDE = [46, 194, 126]
ROJO = [224, 27, 36]


# Pinta el texto del color que le paso en rgb
def texto_color(texto, rgb, negrita):
    if usar_color == False:
        return texto

    inicio = ""
    if negrita == True:
        inicio = NEGRITA

    codigo = f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
    return inicio + codigo + texto + REINICIO


# Pinta un pedazo de texto con color de letra y de fondo, así dibujo las bandas
def bloque(texto, rgb_frente, rgb_fondo):
    if usar_color == False:
        return texto

    codigo = ""
    if rgb_fondo != None:
        codigo = codigo + f"\033[48;2;{rgb_fondo[0]};{rgb_fondo[1]};{rgb_fondo[2]}m"
    if rgb_frente != None:
        codigo = codigo + f"\033[38;2;{rgb_frente[0]};{rgb_frente[1]};{rgb_frente[2]}m"

    if codigo == "":
        return texto
    return codigo + texto + REINICIO


# Arma el título del programa con una línea arriba y otra abajo
def titulo(texto, ancho):
    linea = texto_color("=" * ancho, NARANJA, False)
    centro = texto_color("  " + texto, NARANJA, True)
    return linea + "\n" + centro + "\n" + linea


# Título que sale al entrar a cada opción del menú
def subtitulo(texto, ancho):
    linea = texto_color("-" * ancho, GRIS, False)
    return "\n" + texto_color(texto, NARANJA, True) + "\n" + linea


# Mensaje en rojo para cuando el usuario escribe algo mal
def aviso(texto):
    return texto_color("  [!] " + texto, ROJO, True)


# Mensaje en verde para cuando algo sale bien
def exito(texto):
    return texto_color(texto, VERDE, True)
