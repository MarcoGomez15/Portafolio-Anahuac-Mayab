usar_color = True

REINICIO = "\033[0m"
NEGRITA = "\033[1m"

NARANJA = [232, 93, 4]
GRIS = [150, 148, 150]
VERDE = [46, 194, 126]
ROJO = [224, 27, 36]


def activar_color(valor):
    global usar_color
    usar_color = valor


def texto_color(texto, rgb, negrita=False):
    if usar_color == False:
        return texto
    inicio = ""
    if negrita == True:
        inicio = NEGRITA
    codigo = f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
    return inicio + codigo + texto + REINICIO


def bloque(texto, rgb_frente=None, rgb_fondo=None):
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


def titulo(texto, ancho):
    linea = texto_color("=" * ancho, NARANJA)
    centro = texto_color("  " + texto, NARANJA, True)
    return linea + "\n" + centro + "\n" + linea


def subtitulo(texto, ancho):
    linea = texto_color("-" * ancho, GRIS)
    return "\n" + texto_color(texto, NARANJA, True) + "\n" + linea


def aviso(texto):
    return texto_color("  [!] " + texto, ROJO, True)


def exito(texto):
    return texto_color(texto, VERDE, True)
