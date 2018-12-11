import Clases, random, Vector, config

def leerGrafo(path):
	fObj = open(path, "r")
	grafo = fObj.read()
	grafo = grafo.split()

	G = [[],[]]
	n = int(grafo[0])

	for i in range(1,n+1):
		G[0].append(grafo[i])

	for i in range(n+1, len(grafo),2):
		G[1].append([grafo[i],grafo[i+1]])

	return G

def crearGrafo(G, deltaX, deltaY):
	grafo = [[],[]]
	D = {}
	i = 0

	for v in G[0]:
		D[v] = i
		i += 1
		grafo[0].append(Clases.Nodo(v, (0,230,0), config.RADIO, random.randint(0, deltaX)+config.ANCHO/2, random.randint(0, deltaY)+config.ALTO/2))

	for e in G[1]:
		grafo[1].append(Clases.Arista((0,0,0), grafo[0][D[e[0]]], grafo[0][D[e[1]]], 2))

	return grafo

def crearManta(n):
	V = [str(i) for i in range(1,n**2+1)]
	E = []
	for v in V:
		if (int(v)%n) != 0:
			E.append([v,str(int(v)+1)])
		if int(v) <= (n**2 - n):
			E.append([v,str(int(v)+n)])
	return [V,E]

def crearCompleto(n):
	V = [str(i) for i in range(n)]
	E = []
	for i in range(n):
		for j in range(i,n):
			E.append([str(i),str(j)])
	return [V,E]

def crearBipartito(a,b):
	V = [str(i) for i in range(1,a+b+1)]
	E = []
	for i in range(1, a+1):
		for j in range(a+1,a+b+1):
			E.append([str(i),str(j)])
	print E
	return [V,E]


def fa(x,k):
	return (x)/k

def fr(x,k):
	return (k)/x

def iteracionFruchterman(G,k,t,L,W):
	V = G[0]
	E = G[1]

	for v in V:
		v.desp = [0,0]

	for i, v in enumerate(V):
		#*Calculamos Repulsiones
		for u in V[:i]+V[i+1:]:
			dif = Vector.resta(u.pos, v.pos)
			mod = Vector.mod(dif)
			if mod < 2E-23:
				mod = 2E-23
			v.desp = Vector.resta(v.desp, Vector.mult(fr(mod, k), Vector.mult(1/mod,dif)))
			u.desp = Vector.suma(u.desp, Vector.mult(fr(mod, k), Vector.mult(1/mod,dif)))
	
		#*Calculamos atraccion gravitatoria	
		dif = Vector.resta([config.ANCHO/2, config.ALTO/2], v.pos)
		mod = Vector.mod(dif)
		if mod < 2E-23:
			mod = 2E-23
		v.desp = Vector.suma(v.desp, Vector.mult(fa(mod,k), Vector.mult(1/mod,dif)))
	
	#*Calculamos Atracciones
	for e in E:
		dif = Vector.resta(e.a.pos, e.b.pos)
		mod = Vector.mod(dif)
		if mod < 2E-23:
			mod = 2E-23
		e.a.desp = Vector.resta(e.a.desp, Vector.mult(fa(mod,k), Vector.mult(1/mod,dif)))
		e.b.desp = Vector.suma(e.b.desp, Vector.mult(fa(mod,k), Vector.mult(1/mod,dif)))

	#*
	for v in V:
		modulo = Vector.mod(v.desp)
		v.pos = Vector.suma(v.pos, v.desp)

		v.pos[0] = min(W,max(0,v.pos[0]))
		v.pos[1] = min(L,max(0,v.pos[1]))

	return t * config.FACTOR_TEMP