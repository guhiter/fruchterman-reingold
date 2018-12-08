import sys, pygame, math, time
import os.path
from data import Grafos, Dibujar, config, Clases
from argparse import ArgumentParser

PATH = os.path.abspath(os.path.dirname(__file__))
PATH_INPUT = PATH + "/grafos/"

def getParser():
	parser = ArgumentParser()

	parser.add_argument('-d', '--debug', action='store_true', help='Modo debug, (muestra informacion en pantalla', default=False)
	parser.add_argument('-o', '--output', action='store_true', help='Guarda el grafo como se ve en la ventana como una imagen, cuando se apreta la tecla Esc', default=False)
	parser.add_argument('-i', '--iter', type=int, help='Cantidad de iteraciones a realizar', default=0)

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-f', '--file', help='Nombre del archivo bajo src/grafos/ a importar')
	group.add_argument('-k', '--complete', type=int, metavar='K', help='Genera un grafo completo de K vertices')
	group.add_argument('-m', '--manta', type=int, metavar='M', help='Genera una manta de K vertices')
	group.add_argument('-b', '--bipartite', nargs=2, type=int, metavar=('A','B'), help="Genera un grafo bipartito completo con una componente de A vertices y la otra de B vertices")

	return parser

def main():
	SCREEN_SIZE = config.ANCHO, config.ALTO
	pygame.init()

	parser = getParser()

	args = parser.parse_args()

	screen = pygame.display.set_mode(SCREEN_SIZE)
	pygame.display.set_caption("Fruchterman-Reingold")

	if args.file != None:
		G = Grafos.leerGrafo(PATH_INPUT + args.file)

	elif args.manta != None:
		G = Grafos.crearManta(args.manta)

	elif args.complete != None:
		G = Grafos.crearCompleto(args.complete)

	elif args.bipartite != None:
		G = Grafos.crearBipartito(args.bipartite[0], args.bipartite[1])

	else:
		print 
		ArgumentParser.print_help(parser)
		return	

	G = Grafos.crearGrafo(G, 300,300)
	t = config.TEMP
	#t = (config.ANCHO*config.ALTO)/10
	k = int(config.CONSTANT * math.sqrt((config.ANCHO*config.ALTO)/len(G[0])))
	#k = math.sqrt((config.ANCHO*config.ALTO)/len(G[0]))

	iterN = args.iter
	infinite = False
	if iterN == 0:
		infinite = True

	key_down = False
	key_up = False
	
	while True:
		screen.fill((config.BACKGROUND_COLOR))
		Dibujar.dibujarGrafo(screen,G)
		if args.debug:
			Dibujar.dibujarTexto(screen, "k: " + str(k), 10, 7)
			Dibujar.dibujarTexto(screen, "t: " + str(t), 10, 18)
			if not infinite:
				Dibujar.dibujarTexto(screen, "Iteracion: " + str(iterN), 10, 29)
			for v in G[0]:
				print("{0}\t desplazamiento:\t {1}".format(v.nombre, str(v.desp)))
			print ("-----------------------------------------------")

		if infinite or iterN > 0:
			t = Grafos.iteracionFruchterman(G,k,t,config.ALTO,config.ANCHO)
			iterN -= 1

		if t < 1:
			t = 1

		pygame.display.flip()
		#time.sleep(0.01)
		time.sleep(config.SLEEP_TIME)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.image.save(screen, "output.png")
					sys.exit()
				if event.key == pygame.K_UP:
					key_up = True
					t = t * config.TEMPERATURE_INCREASE_ON_KEYDOWN
				if event.key == pygame.K_DOWN:
					key_down = True
					t = t * config.TEMPERATURE_INCREASE_ON_KEYDOWN


			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					key_up = False
				if event.key == pygame.K_DOWN:
					key_down = False

		if key_up:
			k += 1
			t = t * config.TEMPERATURE_INCREASE_ON_KEYHOLD

		if key_down:
			k = max(1, k-1)
			t = t * config.TEMPERATURE_INCREASE_ON_KEYHOLD


if __name__ == "__main__":
	main()
