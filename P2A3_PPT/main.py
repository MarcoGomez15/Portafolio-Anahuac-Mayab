from jugador_automatico import JugadorAutomatico

class JuegoPPT:
    def __init__(self):
        self.jugador1 = JugadorAutomatico("jugador 1")
        self.jugador2 = JugadorAutomatico("jugador 2")

    def determinar_ganador(self, e1, e2):
        if e1 == e2:
            return "empate"
        elif (e1 == "piedra" and e2 == "tijera") or \
             (e1 == "tijera" and e2 == "papel") or \
             (e1 == "papel" and e2 == "piedra"):
            return self.jugador1.nombre
        else:
            return self.jugador2.nombre

    def iniciar(self):
        RESET = "\033[0m"
        BOLD = "\033[1m"
        CYAN = "\033[96m"
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        MAGENTA = "\033[95m"

        print(f"\n{CYAN}{BOLD}======================================================{RESET}")
        print(f"{CYAN}{BOLD}   🎮 Bienvenido al juego de piedra papel o tijera 🎮 {RESET}")
        print(f"{CYAN}{BOLD}======================================================{RESET}\n")
        
        e1 = self.jugador1.hacer_eleccion()
        e2 = self.jugador2.hacer_eleccion()
        
        print(f"{YELLOW}🤖 El {self.jugador1.nombre} ha usado:{RESET} {BOLD}{e1}{RESET} ")
        print(f"{YELLOW}🤖 El {self.jugador2.nombre} ha usado{RESET} {BOLD}{e2}{RESET} ")
        
        ganador = self.determinar_ganador(e1, e2)
        
        print(f"{GREEN}{BOLD}🌟=================== RESULTADO ===================🌟{RESET}")
        if ganador == "empate":
            print(f"{GREEN}{BOLD}                    empate                     {RESET}")
        else:
            print(f"{GREEN}{BOLD}             El ganador es: {ganador}.             {RESET}")
        print(f"{GREEN}{BOLD}🌟=================================================🌟{RESET}\n")
        
        print(f"{CYAN}--- Reglas del juego ---{RESET}")
        print("🪨  Piedra vence a Tijera")
        print("✂️  Tijera vence a Papel")
        print("📄  Papel vence a Piedra")
        print("🤝  Si ambos jugadores eligen la misma opción, será empate.\n")

if __name__ == "__main__":
    juego = JuegoPPT()
    juego.iniciar()
