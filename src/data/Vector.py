from math import sqrt

def suma(a,b):
	return [a[0]+b[0],a[1]+b[1]]

def resta(a,b):
	return [a[0]-b[0], a[1]-b[1]]

def mod(a):
	return sqrt(a[0]**2 + a[1]**2)

def mult(x,a):
	return [x*a[0], x*a[1]]