# Wine Quality Red and White
1. Título: Calidad del vino
2. Fuentes
   Creado por: Paulo Cortez (Univ. Minho), Antonio Cerdeira, Fernando Almeida, Telmo Matos y Jose Reis (CVRVV) @ 2009
3. Uso pasado:
  P. Cortez, A. Cerdeira, F. Almeida, T. Matos y J. Reis.
  Modelar las preferencias del vino mediante la extracción de datos a partir de las propiedades fisicoquímicas.
  En Decision Support Systems, Elsevier, 47 (4): 547-553. ISSN: 0167-9236.
  En la referencia anterior, se crearon dos conjuntos de datos, utilizando muestras de vino tinto y blanco.
  Las entradas incluyen pruebas objetivas (por ejemplo, valores de PH) y la salida se basa en datos sensoriales
  (mediana de al menos 3 evaluaciones realizadas por expertos en vino). Cada experto calificó la calidad del vino
  entre 0 (muy malo) y 10 (muy excelente). Se aplicaron varios métodos de minería de datos al modelo
  estos conjuntos de datos bajo un enfoque de regresión. El modelo de máquina de vectores de soporte logró el
  Mejores resultados. Se calcularon varias métricas: MAD, matriz de confusión para una tolerancia de error fija (T),
  etc. Además, trazamos la importancia relativa de las variables de entrada (medidas por una sensibilidad
  procedimiento de análisis).
4. Información relevante:
   Los dos conjuntos de datos están relacionados con variantes rojas y blancas del vino portugués "Vinho Verde".
   Para más detalles, consulte: http://www.vinhoverde.pt/en/ o la referencia [Cortez et al., 2009].
   Debido a problemas de privacidad y logística, solo las variables fisicoquímicas (entradas) y sensoriales (salida)
   están disponibles (por ejemplo, no hay datos sobre tipos de uva, marca de vino, precio de venta del vino, etc.).
   Estos conjuntos de datos pueden verse como tareas de clasificación o regresión.
   Las clases están ordenadas y no equilibradas (por ejemplo, hay más vinos normales que
   excelentes o pobres). Se pueden utilizar algoritmos de detección de valores atípicos para detectar los pocos
   o vinos pobres. Además, no estamos seguros de si todas las variables de entrada son relevantes. Entonces
   Podría ser interesante probar los métodos de selección de características.
5. Número de instancias: vino tinto - 1599; vino blanco - 4898.
6. Número de atributos: 11 + atributo de salida
   Nota: varios de los atributos pueden estar correlacionados, por lo que tiene sentido aplicar algún tipo de
   selección de características.
7. Información sobre atributos:
   Variables de entrada (basadas en pruebas fisicoquímicas):
   1 - acidez fija
   2 - acidez volátil
   3 - ácido cítrico
   4 - azúcar residual
   5 - cloruros
   6 - dióxido de azufre libre
   7 - dióxido de azufre total
   8 - densidad
   9 - pH
   10 - sulfatos
   11 - alcohol
   Variable de salida (basada en datos sensoriales):
   12 - calidad (puntuación entre 0 y 10)
8. Valores de atributos perdidos: Ninguno