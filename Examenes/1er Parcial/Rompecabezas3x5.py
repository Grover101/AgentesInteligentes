import time

solucion = ['1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '10', '11', '12',
            '13', '14', '0']
inicio = ['1', '2', '3',
          '4', '5', '6',
          '7', '0', '9',
          '10', '8', '11',
          '13', '14', '12']
# inicio = ['1', '2', '3',
#       '4', '5', '6',
#       '7', '8', '9',
#       '10', '12', '0',
#       '13', '11', '14']
# inicio = ['1', '3', '6',
#           '4', '0', '2',
#           '7', '5', '9',
#           '10', '8', '11',
#           '13', '14', '12']
# inicio = ['1', '3', '6',
#       '4', '0', '2',
#       '7', '5', '9',
#       '10', '8', '14',
#       '13', '11', '12']

equivalente = {'L': "Izquierda", 'R': "Derecha", 'U': "Arriba", 'D': "Abajo"}


class Tablero:
    def __init__(self, estados):
        self.ancho = 3
        self.alto = 5
        self.estados = estados

    def ejecutar_accion(self, accion):
        # Relaiza los mivimientos en el tablero segun los limites del tablero.
        nuevos_estados = self.estados[:]
        indice_vacio = nuevos_estados.index('0')
        if accion == 'L':
            if indice_vacio % self.ancho > 0:
                nuevos_estados[indice_vacio -
                               1], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[indice_vacio - 1]
        if accion == 'R':
            if indice_vacio % self.ancho < (self.ancho - 1):
                nuevos_estados[indice_vacio +
                               1], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[indice_vacio + 1]
        if accion == 'U':
            if indice_vacio - self.ancho >= 0:
                nuevos_estados[indice_vacio - self.ancho], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[
                    indice_vacio - self.ancho]
        if accion == 'D':
            if indice_vacio + self.ancho < self.ancho * self.alto:
                nuevos_estados[indice_vacio + self.ancho], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[
                    indice_vacio + self.ancho]
        return Tablero(nuevos_estados)


class Nodo:
    def __init__(self, estado, padre, accion):
        self.estado = estado
        self.padre = padre
        self.accion = accion

    def __repr__(self):
        return str(self.estado.estados)

    def __eq__(self, otro):
        return self.estado.estados == otro.estado.estados

    def __hash__(self):
        return hash(self.estado)


def get_hijos(padre_Nodo):
    # por cada padre ejecuta una accion y crea sus hijos ya sea por L,R,U,D
    # retornando los hijos de un padre
    hijos = []
    accions = ['L', 'R', 'U', 'D']
    for accion in accions:
        hijo_estado = padre_Nodo.estado.ejecutar_accion(accion)
        hijo_Nodo = Nodo(hijo_estado, padre_Nodo, accion)
        hijos.append(hijo_Nodo)
    return hijos


def gcalc(Nodo):
    # devuelve el costo del estado acutal que entodo caso seria el nivel de profundidad
    # se encuentra cierto nodo, esta funcion es G(n)
    contador = 0
    while Nodo.padre is not None:
        Nodo = Nodo.padre
        contador += 1
    return contador


def hamming(estados):
    # esta heuristica es simple de entender cuenta las posiciones erroneas en el tablero
    # mientras menor sea la cantidad de posiciones erroneas mejor el nodo a seguir
    pos_erroneas = 0
    objetivo_estados = ['1', '2', '3', '4', '5', '6', '7',
                        '8', '9', '10', '11', '12', '13', '14', '0']
    for i in objetivo_estados:
        if objetivo_estados.index(i) - estados.index(i) != 0 and i != 0:
            pos_erroneas += 1
    return pos_erroneas


def manhattan(estados):
    # esta heuristica es una de las ideales para resolver este problema
    # cuenta las posicion de donde se encuentra hasta donde debería llegar
    contador = 0
    for i in range(0, 14):
        # i+1 es por que el rango empieza en 0 y necesitamos saber de las demas posiciones pero no la de 0
        index = estados.index(str(i + 1))
        # %3 es para las columnas
        # /5 es para las filas
        contador += (abs((i / 5) - (index / 5)) + abs((i % 3) - (index % 3)))
    return contador


def find_path(Nodo):
    # Devuelve la ruta y los estados de regreos a al entrada del nodo o nodo raiz
    path = []
    estado = []
    while (Nodo.padre is not None):
        path.append(Nodo.accion)
        estado.append(Nodo.estado.estados)
        Nodo = Nodo.padre
    path.reverse()
    estado.reverse()
    return (path, estado)


def mostraTabla(estados, movimientos):
    # mostrar los estados o tableros de la solucion de foma entendible y el movimiento correspondiente para cada estado
    for estado, movimiento in zip(estados, movimientos):
        print("Movimiento:", equivalente[movimiento])
        for j in range(1, len(estado)+1):
            if(int(estado[j-1]) <= 9):
                print(' '+estado[j-1], end=' ')
            else:
                print(estado[j-1], end=' ')
            if(j % 3 == 0):
                print("")
        print("")


def astar(estado_inicial, estado_objetivo, heuristica):
    # Algoritmo de Busqueda A*
    start_time = time.time()
    frontera = list()
    contador = 0
    visitado = dict()
    frontera.append(estado_inicial)
    visitado[estado_inicial.estado] = estado_inicial
    while frontera:
        # recorre la lista frontera hasta que este vacia o encuentre la solucion
        minim = []
        holder = []
        for x in frontera:
            if heuristica == 0:
                # Esta es la F = h + g
                minim.append(hamming(x.estado.estados)+gcalc(x))
            elif heuristica == 1:
                # Esta es la F = h + g
                minim.append(manhattan(x.estado.estados) + gcalc(x))
            holder.append(x)
        # se obtine la F = h + g minima de toda la lista de minim
        m = min(minim)
        estado_inicial = holder[minim.index(m)]

        if estado_inicial.estado.estados == estado_objetivo:
            # solucion encontrada, entonces muestra los estados desde estado inicial y el tiempo
            # que le toma en resolverlo
            end_time = time.time()
            movimiento, tabla = find_path(estado_inicial)
            print("\nCaso Inicial:")
            for j in range(1, len(inicio)+1):
                if(int(inicio[j-1]) <= 9):
                    print(' '+inicio[j-1], end=' ')
                else:
                    print(inicio[j-1], end=' ')
                if(j % 3 == 0):
                    print("")

            print("\nSolucion:")
            mostraTabla(tabla, movimiento)
            print("Numero de nodos expandidos: " + str(contador))
            print("Tiempo empleado: " + str(round((end_time - start_time), 3)))
            break

        # esta parte elimna los estados repetidos
        frontera.pop(frontera.index(estado_inicial))
        # caso contrario de no encontrar la solucion expande los hijos
        for hijo in get_hijos(estado_inicial):
            contador += 1
            s = hijo.estado
            if s not in visitado or gcalc(hijo) < gcalc(visitado[s]):
                visitado[s] = hijo
                frontera.append(hijo)


def main():
    heuristica = input(
        "Introduzca la heuristica 'H' o 'M' (H es Hamming y M es Manhattan): ")
    if heuristica == 'H':
        heuristica = 0
    elif heuristica == 'M':
        heuristica = 1

    root = Nodo(Tablero(inicio), None, None)
    astar(root, solucion, heuristica)


if __name__ == '__main__':
    main()
