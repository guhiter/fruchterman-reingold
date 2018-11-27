class Nodo:
	#nombre = ""
	#color = (0,200,0)
	#radio = 0

	def __init__(self,nombre,color,r,x,y):
		self.nombre = nombre
		self.color = color
		self.radio = r
		self.pos = [x,y]
		self.desp = [0,0]

class Arista:

	def __init__(self,color,a,b, g):
		self.color = color
		self.a = a
		self.b = b
		self.g = g