# Busqueda en Amplitud - Breadth First Search
from Nodos import Nodo


def busqueda_BPA_solucion(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # expandir nodos hijo
            estado_nodo = nodo_actual.get_estado()

            # for i in range(8):
            #     hijo = [estado_nodo[i + 1], estado_nodo[i]]
            #     print(hijo)

            # operador 1
            hijo = [estado_nodo[1], estado_nodo[0], estado_nodo[2],
                    estado_nodo[3], estado_nodo[4], estado_nodo[5],
                    estado_nodo[6], estado_nodo[7]]
            hijo_1 = Nodo(hijo)
            if not hijo_1.en_lista(nodos_visitados) and not hijo_1.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_1)

            # operador 2
            hijo = [estado_nodo[0], estado_nodo[2], estado_nodo[1],
                    estado_nodo[3], estado_nodo[4], estado_nodo[5],
                    estado_nodo[6], estado_nodo[7]]
            hijo_2 = Nodo(hijo)
            if not hijo_2.en_lista(nodos_visitados) and not hijo_2.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_2)

            # operador 3
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3],
                    estado_nodo[2], estado_nodo[4], estado_nodo[5],
                    estado_nodo[6], estado_nodo[7]]
            hijo_3 = Nodo(hijo)
            if not hijo_3.en_lista(nodos_visitados) and not hijo_3.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_3)

            # operador 4
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2],
                    estado_nodo[4], estado_nodo[3], estado_nodo[5],
                    estado_nodo[6], estado_nodo[7]]
            hijo_4 = Nodo(hijo)
            if not hijo_4.en_lista(nodos_visitados) and not hijo_4.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_4)

            # operador 5
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2],
                    estado_nodo[3], estado_nodo[5], estado_nodo[4],
                    estado_nodo[6], estado_nodo[7]]
            hijo_5 = Nodo(hijo)
            if not hijo_5.en_lista(nodos_visitados) and not hijo_5.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_5)

            # operador 6
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2],
                    estado_nodo[3], estado_nodo[4], estado_nodo[6],
                    estado_nodo[5], estado_nodo[7]]
            hijo_6 = Nodo(hijo)
            if not hijo_6.en_lista(nodos_visitados) and not hijo_6.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_6)

            # operador 7
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2],
                    estado_nodo[3], estado_nodo[4], estado_nodo[5],
                    estado_nodo[7], estado_nodo[6]]
            hijo_7 = Nodo(hijo)
            if not hijo_7.en_lista(nodos_visitados) and not hijo_7.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_7)

            nodo_actual.set_hijo(
                [hijo_1, hijo_2, hijo_3, hijo_4, hijo_5, hijo_6, hijo_7])


if __name__ == "__main__":
    estado_inicial = [1, 2, 6, 5, 4, 3, 8, 7]
    solucion = [1, 2, 3, 4, 5, 6, 7, 8]
    nodo_solucion = busqueda_BPA_solucion(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
