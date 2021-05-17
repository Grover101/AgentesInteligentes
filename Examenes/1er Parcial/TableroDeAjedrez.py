import random


class Problema_Genetico(object):
    # Constructor
    def __init__(self, genes, fun_decodificar, fun_cruzar, fun_mutar, fun_fitness, longitud_individuos):
        self.genes = genes
        self.fun_decodificar = fun_decodificar
        self.fun_cruzar = fun_cruzar
        self.fun_mutar = fun_mutar
        self.fun_fitness = fun_fitness
        self.longitud_individuos = longitud_individuos

    def decodificar(self, genotipo):
        # Devuelve el fenotipo a partir del genotipo
        fenotipo = self.fun_decodificar(genotipo)
        return fenotipo

    def cruzar(self, cromosoma1, cromosoma2):
        # Devuelve el cruce de un par de cromosomas
        cruce = self.fun_cruzar(cromosoma1, cromosoma2)
        return cruce

    def mutar(self, cromosoma, prob):
        # Devuelve el cromosoma mutado
        mutante = self.fun_mutar(cromosoma, prob)
        return mutante

    def fitness(self, cromosoma):
        # Función de valoración
        valoracion = self.fun_fitness(cromosoma)
        return valoracion
    # Función interpreta lista de 0's y 1's como número natural:


def fun_cruzar(cromosoma1, cromosoma2):
    # Cruza los cromosomas por la mitad
    l1 = len(cromosoma1)
    cruce1 = cromosoma1[0:int(l1 / 2)] + cromosoma2[int(l1 / 2):l1]
    cruce2 = cromosoma2[0:int(l1 / 2)] + cromosoma1[int(l1 / 2):l1]
    return [cruce1, cruce2]


def fun_mutar(cromosoma, prob):
    # Elige un elemento al azar del cromosoma y lo modifica con una probabilidad igual a prob
    l = len(cromosoma)
    p = random.randint(0, l - 1)
    if prob >= random.uniform(0, 1):
        cromosoma[p] = (cromosoma[p] + 1) % 2
    return cromosoma


def poblacion_inicial(problema_genetico, tamano_poblacion):
    # crea un lista de un tamanio de poblacion de lista de genes aleatorios de un tamaño de numero de individuos
    l = []
    for i in range(tamano_poblacion):
        l.append([random.choice(problema_genetico.genes)
                  for i in range(problema_genetico.longitud_individuos)])
    return l


def cruza_padres(problema_genetico, padres):
    l = []
    l1 = len(padres)
    while padres != []:
        l.extend(problema_genetico.cruzar(padres[0], padres[1]))
        padres.pop(0)
        padres.pop(0)
    return l


def muta_individuos(problema_genetico, poblacion, prob):
    return [problema_genetico.mutar(individuo, prob) for individuo in poblacion]


def seleccion_por_torneo(problema_genetico, poblacion, n, k, opt):
    # Selección por torneo de n individuos de una población.
    # k es el nº de participantes
    # y opt la función max o min.
    seleccionados = []
    for i in range(n):
        participantes = random.sample(poblacion, k)
        seleccionado = opt(participantes, key=problema_genetico.fitness)
        seleccionados.append(seleccionado)
    return seleccionados


def nueva_generacion_t(problema_genetico, k, opt, poblacion, n_padres, n_directos, prob_mutar):
    padres2 = seleccion_por_torneo(
        problema_genetico, poblacion, n_directos, k, opt)
    padres1 = seleccion_por_torneo(
        problema_genetico, poblacion, n_padres, k, opt)
    cruces = cruza_padres(problema_genetico, padres1)
    generacion = padres2 + cruces
    resultado_mutaciones = muta_individuos(
        problema_genetico, generacion, prob_mutar)
    return resultado_mutaciones


def algoritmo_genetico_t(problema_genetico, k, opt, ngen, size, prop_cruces, prob_mutar):
    poblacion = poblacion_inicial(problema_genetico, size)
    print("Poblacion Inicial")
    print(poblacion)
    print("")
    n_padres = round(size * prop_cruces)
    n_padres = int(n_padres if n_padres % 2 == 0 else n_padres - 1)
    n_directos = size - n_padres
    for _ in range(ngen):
        poblacion = nueva_generacion_t(
            problema_genetico, k, opt, poblacion, n_padres, n_directos, prob_mutar)
        print("Nueva población")
        print(poblacion)
        print("")
        for ind in poblacion:
            if(problema_genetico.fitness(ind) == 0):
                print("la solucion es:")
                # tablero = [ind[6*i: 6*(i+1)] for i in range(4)]
                # print(tablero)
                print(ind)
                break
    mejor_cr = opt(poblacion, key=problema_genetico.fitness)
    mejor = problema_genetico.decodificar(mejor_cr)
    return (mejor, problema_genetico.fitness(mejor_cr))


def decodifica_tablero(cromosoma, n_objetos):
    l = []
    # print(cromosoma)
    for i in range(len(n_objetos)):
        if cromosoma[i] == n_objetos[i]:
            l.append(1)
        else:
            l.append(0)
    return l


def fitness_tablero(cromosoma, n_objetos):
    objetos_tablero = decodifica_tablero(cromosoma, n_objetos)
    valor = 48
    for i in range(len(n_objetos)):
        # if cromosoma[i] == n_objetos[i]:
        if objetos_tablero[i] == n_objetos[i]:
            valor -= 1
    return valor


# valor_obj = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0,
#              0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
valor_obj = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1,
             1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1]


def decodifica_tablero_1(cromosoma):
    v = decodifica_tablero(cromosoma, valor_obj)
    return v


def fitness_tablero_1(cromosoma):
    v = fitness_tablero(cromosoma, valor_obj)
    return v


m1g = Problema_Genetico([0, 1], decodifica_tablero_1,
                        fun_cruzar, fun_mutar, fitness_tablero_1, 48)
tableroAjedres, fitness = (algoritmo_genetico_t(
    m1g, 48, min, 100, 48, 0.8, 0.05))

print('Tablero Generado:', [tableroAjedres[6*i: 6*(i+1)] for i in range(4)])
print("Fitness: ", fitness)
