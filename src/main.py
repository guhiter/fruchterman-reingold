import sys, pygame, math, time
import os.path
from data import Grafos, Dibujar, config

PATH = os.path.abspath(os.path.dirname(__file__))


BACKGROUND_COLOR = 0, 0, 0
CONSTANT = 0.3

def main():
	SCREEN_SIZE = config.ANCHO, config.ALTO
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)
	pygame.display.set_caption("Fruchterman-Reingold")
	#G = Grafos.leerGrafo(PATH + "/input")
	G = Grafos.crearManta(8)
	G = Grafos.crearGrafo(G, 400,400)
	t = config.TEMP
	k = CONSTANT * math.sqrt((config.ANCHO*config.ALTO)/len(G[0]))
	key_down = False
	key_up = False
	
	while True:
		screen.fill((255,255,255))
		Dibujar.dibujarGrafo(screen,G)
		Dibujar.dibujarTexto(screen, "k: " + str(k), config.ALTO - 10, 7)
		t = Grafos.iteracionFruchterman(G,k,t,config.ALTO,config.ANCHO)
		pygame.display.flip()
		time.sleep(0.01)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()
				if event.key == pygame.K_UP:
					key_up = True
				if event.key == pygame.K_DOWN:
					key_down = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					key_up = False
				if event.key == pygame.K_DOWN:
					key_down = False

		if key_up:
			k += 1

		if key_down:
			k = max(1, k-1)


if __name__ == "__main__":
	main()
