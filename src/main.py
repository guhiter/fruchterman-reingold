import sys, pygame, math, time
import os.path
from data import Grafos, Dibujar, config
from argparse import ArgumentParser

PATH = os.path.abspath(os.path.dirname(__file__))
PATH_INPUT = PATH + "/grafos/"


BACKGROUND_COLOR = 0, 0, 0
CONSTANT = 0.3

def arguments():
	parser = ArgumentParser()

	parser.add_argument('-d', '--debug', action='store_true', help='Modo debug, (muestra informacion en pantalla', default=False)

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-f', '--file', type=open, help='Nombre del archivo bajo src/grafos/ a importar')
	group.add_argument('-k', '--complete', type=int, metavar='K', help='Genera un grafo completo de K vertices')
	group.add_argument('-m', '--manta', type=int, metavar='M', help='Genera una manta de K vertices')
	group.add_argument('-b', '--bipartite', nargs=2, type=int, metavar=('A','B'), help="Genera un grafo bipartito completo con una componente de A vertices y la otra de B vertices")

	return parser.parse_args()

def main():
	SCREEN_SIZE = config.ANCHO, config.ALTO
	pygame.init()

	args = arguments()

	screen = pygame.display.set_mode(SCREEN_SIZE)
	pygame.display.set_caption("Fruchterman-Reingold")

	if args.file != None:
		G = Grafos.leerGrafo(PATH_INPUT + args.file)

	if args.manta != None:
		G = Grafos.crearManta(args.manta)

	if args.complete != None:
		G = Grafos.crearCompleto(args.complete)

	if args.bipartite != None:
		G = Grafos.crearBipartito(args.bipartite[0], args.bipartite[1])
	

	G = Grafos.crearGrafo(G, 400,400)
	t = config.TEMP
	k = CONSTANT * math.sqrt((config.ANCHO*config.ALTO)/len(G[0]))
	key_down = False
	key_up = False
	
	while True:
		screen.fill((255,255,255))
		Dibujar.dibujarGrafo(screen,G)
		if args.debug:
			Dibujar.dibujarTexto(screen, "k: " + str(k), 10, 7)
			Dibujar.dibujarTexto(screen, "t: " + str(t), 10, 18)
		t = Grafos.iteracionFruchterman(G,k,t,config.ALTO,config.ANCHO)
		if t < 1:
			t = 1
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
					#t += 50
				if event.key == pygame.K_DOWN:
					key_down = True
					#t += 50


			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					key_up = False
				if event.key == pygame.K_DOWN:
					key_down = False

		if key_up:
			k += 1
			#t += 10

		if key_down:
			k = max(1, k-1)
			#t += 10


if __name__ == "__main__":
	main()
