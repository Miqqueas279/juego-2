import pygame
import random
import pickle

pygame.init()

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

ANCHO, ALTURA = 1200, 800
pantalla = pygame.display.set_mode((ANCHO, ALTURA))
pygame.display.set_caption('Juego RPG')

fuente = pygame.font.SysFont('Arial', 24)

class Personaje:
    def __init__(self, nombre, vida_inicial, vida_max, mana, velocidad, defensa_inicial, defensa_final, dano_inicial, dano_final, tipo_arma, monedas):
        self.nombre = nombre
        self.vida = vida_inicial
        self.vida_max = vida_max
        self.mana = mana
        self.velocidad = velocidad
        self.defensa = defensa_inicial
        self.dano_inicial = dano_inicial
        self.dano_final = dano_final
        self.defensa_final = defensa_final
        self.tipo_arma = tipo_arma
        self.monedas = monedas
        self.nivel = 1
        self.experiencia = 0
        self.pociones_vida = 3
        self.pociones_mana = 3

    def atacar(self):
        return random.randint(self.dano_inicial, self.dano_final)

    def defender(self, dano):
        return max(0, dano - self.defensa)

    def curar(self, cantidad):
        self.vida = min(self.vida + cantidad, self.vida_max)

    def subir_nivel(self):
        self.nivel += 1
        self.vida_max += 50
        self.vida = self.vida_max
        self.mana += 20
        self.dano_inicial += 5
        self.dano_final += 10
        self.experiencia = 0
        self.pociones_vida += 1
        self.pociones_mana += 1

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        if self.experiencia >= 100:
            self.subir_nivel()

class Guerrero(Personaje):
    def __init__(self):
        super().__init__('Guerrero', 150, 350, 20, 20, 150, 300, 25, 75, "Espada", random.randint(1, 5))

class Arquero(Personaje):
    def __init__(self):
        super().__init__('Arquero', 50, 150, 35, 100, 75, 150, 25, 75, "Arco", random.randint(1, 5))
        self.flechas = 20

    def recargar_flechas(self):
        if self.mana >= 10:
            self.flechas = min(self.flechas + 10, 120)
            self.mana -= 10
            return True
        return False

class Mago(Personaje):
    def __init__(self):
        super().__init__('Mago', 100, 250, 500, 75, 100, 200, 25, 75, "Mele", random.randint(1, 5))

class Esqueleto(Personaje):
    def __init__(self):
        super().__init__('Esqueleto', 50, 50, 0, 10, 10, 50, 5, 10, random.choice(["Espada", "Arco"]), random.randint(1, 5))

class Goblin(Personaje):
    def __init__(self):
        super().__init__('Goblin', 60, 60, 0, 10, 10, 60, 5, 15, random.choice(["Espada", "Arco"]), random.randint(1, 5))

class Trol(Personaje):
    def __init__(self):
        super().__init__('Trol', 120, 120, 0, 15, 15, 80, 10, 25, "Espada", random.randint(5, 10))

class Fantasma(Personaje):
    def __init__(self):
        super().__init__('Fantasma', 40, 40, 0, 20, 5, 30, 1, 5, "Mele", 1)

class Zombie(Personaje):
    def __init__(self):
        super().__init__('Zombie', 50, 50, 0, 10, 5, 40, 1, 7, "Mele", random.randint(1, 3))

class Bandido(Personaje):
    def __init__(self):
        super().__init__('Bandido', 80, 80, 0, 10, 10, 70, 5, 15, random.choice(["Espada", "Arco"]), random.randint(5, 10))

class Vaca(Personaje):
    def __init__(self):
        super().__init__('Vaca', 80, 80, 0, 0, 0, 10, 0, 0, "Nada", 0)

class Gallina(Personaje):
    def __init__(self):
        super().__init__('Gallina', 40, 40, 0, 0, 0, 5, 0, 0, "Nada", 0)

class Jabali(Personaje):
    def __init__(self):
        super().__init__('Jabali', 60, 60, 0, 10, 5, 50, 1, 10, "Mele", 0)

def dibujar_texto(texto, x, y, color=BLANCO):
    superficie_texto = fuente.render(texto, True, color)
    pantalla.blit(superficie_texto, (x, y))

def menu_inicio():
    while True:
        pantalla.fill(NEGRO)
        dibujar_texto("Bienvenido al juego RPG", 500, 50, BLANCO)
        dibujar_texto("1. Jugar", 550, 150, BLANCO)
        dibujar_texto("2. Cargar Partida", 550, 200, BLANCO)
        dibujar_texto("3. Salir", 550, 250, BLANCO)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return 'jugar'
                elif evento.key == pygame.K_2:
                    return 'cargar'
                elif evento.key == pygame.K_3:
                    pygame.quit()
                    exit()

def elegir_clase():
    while True:
        pantalla.fill(NEGRO)
        dibujar_texto("Elige tu clase", 500, 50, BLANCO)
        dibujar_texto("1. Guerrero", 550, 150, BLANCO)
        dibujar_texto("2. Arquero", 550, 200, BLANCO)
        dibujar_texto("3. Mago", 550, 250, BLANCO)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return Guerrero()
                elif evento.key == pygame.K_2:
                    return Arquero()
                elif evento.key == pygame.K_3:
                    return Mago()

def combate(jugador):
    while jugador.vida > 0:
        enemigo = generar_enemigo()

        while enemigo.vida > 0 and jugador.vida > 0:
            pantalla.fill(NEGRO)
            dibujar_texto(f"{jugador.nombre} VS {enemigo.nombre}", 400, 50)
            dibujar_texto(f"Vida: {jugador.vida}", 50, 100)
            dibujar_texto(f"Mana: {jugador.mana}", 50, 150)
            dibujar_texto(f"Nivel: {jugador.nivel}", 50, 200)
            dibujar_texto(f"Vida del Enemigo: {enemigo.vida}/{enemigo.vida_max}", 900, 100)
            dibujar_texto("1. Atacar", 50, 400)
            dibujar_texto("2. Defender", 50, 450)
            dibujar_texto("3. Huir", 50, 500)
            dibujar_texto("4. Usar Mochila", 50, 550)
            dibujar_texto("P. Pausar y Guardar", 50, 600)
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        dano = jugador.atacar()
                        enemigo.vida -= max(0, dano)
                        dibujar_texto(f"{jugador.nombre} atacó y causó {dano} de daño", 250, 300)
                    elif evento.key == pygame.K_2:
                        dibujar_texto(f"{jugador.nombre} se defendió", 250, 300)
                    elif evento.key == pygame.K_3:
                        return 'huir'
                    elif evento.key == pygame.K_4:
                        mochila(jugador)

        if enemigo.vida <= 0:
            jugador.ganar_experiencia(50)
            jugador.monedas += enemigo.monedas
            dibujar_texto(f"¡Has derrotado a {enemigo.nombre} y ganado {enemigo.monedas} monedas!", 250, 300)
            pygame.display.flip()
            pygame.time.wait(2000)
        else:
            return 'perdido'

def generar_enemigo():
    enemigo = random.choice([Esqueleto(), Goblin(), Trol(), Fantasma(), Zombie(), Bandido(), Vaca(), Gallina(), Jabali()])
    return enemigo

def mochila(jugador):
    while True:
        pantalla.fill(NEGRO)
        dibujar_texto("Mochila", 500, 50, BLANCO)
        dibujar_texto(f"Pociones de Vida: {jugador.pociones_vida}", 550, 150, BLANCO)
        dibujar_texto(f"Pociones de Mana: {jugador.pociones_mana}", 550, 200, BLANCO)
        dibujar_texto("3. Cerrar mochila", 550, 350, BLANCO)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1 and jugador.pociones_vida > 0:
                    jugador.curar(50)
                    jugador.pociones_vida -= 1
                    return
                elif evento.key == pygame.K_2 and jugador.pociones_mana > 0:
                    jugador.mana += 50
                    jugador.pociones_mana -= 1
                    return
                elif evento.key == pygame.K_3:
                    return

def pausar(jugador):
    while True:
        pantalla.fill(NEGRO)
        dibujar_texto("Juego Pausado", 500, 50, BLANCO)
        dibujar_texto("1. Continuar", 550, 150, BLANCO)
        dibujar_texto("2. Guardar y Salir", 550, 200, BLANCO)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return
                elif evento.key == pygame.K_2:
                    guardar_partida(jugador)
                    pygame.quit()
                    exit()

def guardar_partida(jugador):
    with open("guardado.pkl", "wb") as f:
        pickle.dump(jugador, f)

def cargar_partida():
    try:
        with open("guardado.pkl", "rb") as f:
            jugador = pickle.load(f)
            return jugador
    except FileNotFoundError:
        return None

def main():
    opcion = menu_inicio()
    if opcion == 'jugar':
        jugador = elegir_clase()
        while True:
            resultado = combate(jugador)
            if resultado == 'huir':
                print("Has huido del combate y puedes continuar explorando.")
            elif resultado == 'perdido':
                print("Has perdido el combate. Volviendo al inicio...")
                opcion = menu_inicio()
                if opcion == 'jugar':
                    jugador = elegir_clase()
    elif opcion == 'cargar':
        jugador = cargar_partida()
        if jugador:
            while True:
                resultado = combate(jugador)
                if resultado == 'huir':
                    print("Has huido del combate y puedes continuar explorando.")
                elif resultado == 'perdido':
                    print("Has perdido el combate. Volviendo al inicio...")
                    opcion = menu_inicio()
                    if opcion == 'jugar':
                        jugador = elegir_clase()
        else:
            print("No se encontró ninguna partida guardada.")
            pygame.quit()
            exit()

if __name__ == "__main__":
    main()
