# Graficador de Grafos utilizando fuerzas con algoritmo Fruchterman Reingold

### Dependencias

Para instalar las dependencias manualmente en caso de que el virtualenv no funcione:

```sh
$ pip install pygame
```

### Ejecucion

Para ejecutarlo debemos hacer:

```sh
$ source bin/activate
$ python src/main.py
```

### Config
Se pueden modificar valores en el archivo src/data/config.py

### Grafos por archivo
Para abrir grafos por archivo con su respectiva opcion sobre la linea de comandos, es necesario colocarlos en src/data

### Linea de comandos

```sh
usage: python main.py [-h] [-d] [-f FILE | -k K | -b A B]

optional arguments:
  -h, --help               show this help message and exit
  -d, --debug              modo debug
  -f FILE, --file FILE     carga el grafo desde un archivo
  -k K, --complete K       genera un grafo completo con K vertices
  -b A B, --bipartite A B  genera un grafo bipartito completo con A y B vertices cada componente
```
