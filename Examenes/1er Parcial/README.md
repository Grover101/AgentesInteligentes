# Primer Parcial

---

## Ejercicios:

- **Elaborar un agente que resuelva un rompecabezas de 3X5 (utilice un algoritmo que permita resolverlo en menos de 1 minuto).**

  ###### Forma de Resolverlo

  ***

  Para la resolucion de este ejercicio hace uso del [algoritmo A\* (a_start)](https://es.wikipedia.org/wiki/Algoritmo_de_b%C3%BAsqueda_A*), tambien se uso la Heuristica Manhattan y basandose en el 8 puzzle relizado en clase se realizo el rompecabezas de 3 x 5 de la siguiente forma:

  ###### Inicio

  ***

  | 1   | 3   | 6   |
  | --- | --- | --- |
  | 4   | 0   | 2   |
  | 7   | 5   | 9   |
  | 10  | 8   | 11  |
  | 13  | 14  | 12  |

  ###### Final

  ***

  | 1   | 2   | 3   |
  | --- | --- | --- |
  | 4   | 5   | 6   |
  | 7   | 8   | 9   |
  | 10  | 11  | 12  |
  | 13  | 14  | 0   |

  [Solucion al Ejercicio](https://github.com/Grover101/InteligenciaArtificial/blob/main/Examenes/1er%20Parcial/Rompecabezas3x5.py)

- **Modificar el juego 3 en raya, para que se aplique la misma lógica, pero en un tablero de 4x4 (gana el primero que logra enlazar 3 marcas similares, horizontales, verticales o diagonales).**

  ###### Forma de Resolverlo

  ***

  Para la resolucion de este ejercicio se hace uso de la tecnica de busqueda [Poda alfa-beta](https://es.wikipedia.org/wiki/Poda_alfa-beta), basandose en la clasico 3 en raya, tomando en cuenta las opciones para ganar:
  **Tablero**
  | 13 | 14 | 15 | 16 |
  | ------ | ------ | ------ | ------ |
  | 9 | 10 | 11 | 12 |
  | 5 | 6 | 7 | 8 |
  | 1 | 2 | 3 | 4 |

  **Casos para ganar:**

  ```
  HORIZONTALES            VERTICALES              DIAGONALES
  [1, 2, 3]               [13, 9, 5]              [14, 11, 8]
  [2, 3, 4]               [9, 5, 1]               [13, 10, 7]
  [5, 6, 7]               [14, 10, 6]             [10, 7, 4]
  [6, 7, 8]               [10, 6, 2]              [9, 6, 3]
  [9, 10, 11]             [15, 11, 7]             [15, 10, 5]
  [10, 11, 12]            [11, 7, 3]              [16, 11, 6]
  [13, 14, 15]            [16, 12, 8]             [11, 6, 1]
  [14, 15, 16]            [12, 8, 4]              [12, 7, 2]
  ```

  [Solucion al Ejercicio](https://github.com/Grover101/InteligenciaArtificial/blob/main/Examenes/1er%20Parcial/4enRaya.py)

- **Elabore un algoritmo genético que encuentre la mejor manera de colocar 12 bloques de color blanco y 12 bloques de color negro, ubicados para conformar un tablero de ajedrez:**
  `1 = X, 0 = O `
  | 1 | 0 | 1 | 0 | 1 | 0 |
  | ------ | ------ | ------ | ------ | ------ | ------ |
  | 0 | 1 | 0 | 1 | 0 | 1 |
  | 1 | 0 | 1 | 0 | 1 | 0 |
  | 0 | 1 | 0 | 1 | 0 | 1 |

  **Es decir no pueden existir dos bloques continuos, horizontalmente o verticalmente.**

  ###### Forma de Resolverlo

  ***

  Para la resolucion de este ejercicio se hace uso de [Algoritmos Geneticos](https://es.wikipedia.org/wiki/Algoritmo_gen%C3%A9tico), donde se usara `1,0` para los genes, realizara `n=100` generaciones, con probabilidad de cruce `0.8`, probabilidad de mutacion `0.05` y el valor objetivo sera:

  ```
  valor_obj = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0,  0, 1, 0, 1, 0, 1,
           1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0,  0, 1, 0, 1, 0, 1, ]
  ```

  [Solucion al Ejercicio](https://github.com/Grover101/InteligenciaArtificial/blob/main/Examenes/1er%20Parcial/TableroDeAjedrez.py)

  ###### NOTA:

  Para cada problema, el estudiante debe elegir a su criterio el tipo de algoritmo a emplear. El código fuente de los problemas resueltos debe ser subido además de una explicación puntual del porque de la utilización de un determinado algoritmo y del enfoque asumido para resolver el problema en un archivo de texto adicional para cada problema.
