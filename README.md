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
usage: python main.py [-h] [-d] [-f FILE | -k K | -m M |-b A B]

optional arguments:
  -h, --help               show this help message and exit
  -d, --debug              Modo debug, (muestra informacion en pantalla)
  -o, --output             Guarda el grafo como se ve en la ventana como una imagen, cuando se apreta la tecla Esc
  -f FILE, --file FILE     Nombre del archivo bajo src/grafos/ a importar
  -k K, --complete K       Genera un grafo completo de K vertices
  -m M, --manta M          Genera una manta de K vertices
  -b A B, --bipartite A B  Genera un grafo bipartito completo con una componente de A vertices y la otra de B vertices
```
