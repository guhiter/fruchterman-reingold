import pygame, Clases
from pygame import gfxdraw

def dibujarNodo(screen, nodo):
	pygame.draw.circle(screen, nodo.color, (nodo.pos[0], nodo.pos[1]), nodo.radio)

def dibujarArista(screen, arista):
	pygame.gfxdraw.line(screen, arista.a.pos[0], arista.a.pos[1], arista.b.pos[0], arista.b.pos[1], arista.color)

def dibujarNombre(screen, nodo):
	fuente = pygame.font.SysFont('comicsansms', 20)
	screen.blit(fuente.render(nodo.nombre, True, (155,155,0)), (nodo.pos[0]+(nodo.radio/2), nodo.pos[1]+(nodo.radio/2)))

def dibujarTexto(screen, text, x, y):
	fuente = pygame.font.SysFont('comicsansms', 20)
	screen.blit(fuente.render(text, True, (0,0,0)), (x, y))

def dibujarGrafo(screen, G):
	aristas = G[1]
	nodos = G[0]

	for arista in aristas:
		dibujarArista(screen, arista)

	for nodo in nodos:
		dibujarNodo(screen,nodo)
		dibujarNombre(screen,nodo)