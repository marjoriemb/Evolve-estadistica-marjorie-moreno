# Respuestas — Práctica Final: Análisis y Modelado de Datos

> Para los ejercicios 1 y 2 se tomó el dataset sugerido en la guía de la práctica. 

---

## Ejercicio 1 — Análisis Estadístico Descriptivo
---
* Dataset: Student Performance 
* Fuente: UCI ML Repository
* URL: https://archive.ics.uci.edu/dataset/320/student+performance

Descripción:
* A) Resumen estructural

        Número de filas: 395
        Número de columnas: 33
        Tamaño en Memoria: 0.38 MB

        Tipos de Datos:
            Numéricos (int): 
                age, failures, famrel, freetime, goout, Dalc,
                Walc, health, absences, G1, G2, G3

            Categóricos (object):
                Medu, Fedu, Mjob, Fjob, reason, guardian, 
                traveltime, studytime

            Variables binarias:
                school, sex, address, famsize, Pstatus, schoolsup, famsup,
                paid, activities, nursery, higher, internet, romantic

* B) Estadísticos descriptivos de variables numéricas

      | Variable |  Media | mediana | moda |   std   | varianza | mínimo | máximo | Q 25% | Q 50% | Q 75% |
      |----------|--------|---------|------|---------|----------|--------|--------|-------|-------|-------|
      |   age    |  16.7  |    17   |  16  |  1.276  |  1.628   |   15   |   22   |   16  |   17  |   18  |
      | failures |   0.33 |     0   |   0  |  0.744  |  0.553   |    0   |    3   |    0  |    0  |    0  |
      | absences |   5.71 |     4   |   0  |  8.003  | 64.045   |    0   |   75   |    0  |    4  |    8  |
      |   G1     |  10.91 |    11   |  10  |  3.319  | 11.017   |    3   |   19   |    8  |   11  |   13  |
      |   G2     |  10.71 |    11   |   9  |  3.762  | 14.149   |    0   |   19   |    9  |   11  |   13  |
      |   G3     |  10.42 |    11   |  10  |  4.581  | 20.990   |    0   |   20   |    8  |   11  |   14  |


      Variable Objetivo
      | Rango intercuartílico (IQR) | Coeficiente de asimetría (skewness) | Curtosis |
      |            6                |                  -0.733             |   0.403  |

* D) Variables categóricas

      Entre las variables categóricas se muestra desbalance en:
      
      guardian   /* Casi el 70% de los estudiantes está al cuidado de las madres */
                Frec. Absoluta  Frec. Relativa (%) 
      mother               273            0.691139
      father                90            0.227848
      other                 32            0.081013

      traveltime  /* El 65% de los estudiantes vive a menos de 15min de la escuela */
                  Frec. Absoluta  Frec. Relativa (%)
      1                      257            0.650633
      2                      107            0.270886
      3                       23            0.058228
      4                        8            0.020253
      
      studytime  /* El 50% de los estudiantes estudia menos de 2H a la semana */
                 Frec. Absoluta  Frec. Relativa (%) 
      2                     198            0.501266
      1                     105            0.265823
      3                      65            0.164557
      4                      27            0.068354

      Dalc  /* Casi el 70% de los estudiantes vive en hogares con un muy    */
            /* bajo nivel de consumo de alcohol durante los días de estudio */ 
            Frec. Absoluta  Frec. Relativa (%)
      1                276            0.698734
      2                 75            0.189873
      3                 26            0.065823
      5                  9            0.022785
      4                  9            0.022785      

      school  /* El 88% de los estudiantes pertenecen a la escuela Gabriel Pereira */ 
              Frec. Absoluta  Frec. Relativa (%)
      GP                 349            0.883544
      MS                  46            0.116456      

      address  /* El 77% de los estudiantes viven en zona urbana */
              Frec. Absoluta  Frec. Relativa (%)
      U                  307            0.777215
      R                   88            0.222785

      famsize  /* El 71% de los estudiantes viven en familia de más de 3 miembros */
               Frec. Absoluta  Frec. Relativa (%)
      GT3                 281            0.711392
      LE3                 114            0.288608

      Pstatus  /* Casi el 90% de los estudiantes viven con sus dos padres*/
               Frec. Absoluta  Frec. Relativa (%)
      T                   354            0.896203
      A                    41            0.103797

      schoolsup /* Solo el 12% tiene soporte educativo extra */
                 Frec. Absoluta  Frec. Relativa (%)
      no                    344            0.870886
      yes                    51            0.129114

      nursery /* Casi el 80% asistió a guardería */  
               Frec. Absoluta  Frec. Relativa (%)
      yes                 314            0.794937
      no                   81            0.205063

      higher  /* Casi el 95% desea tomar estudios superiores */ 
              Frec. Absoluta  Frec. Relativa (%)
      yes                375            0.949367
      no                  20            0.050633

      internet  /* Casi el 84% tiene acceso a Internet en casa */ 
                Frec. Absoluta  Frec. Relativa (%)
      yes                  329            0.832911
      no                    66            0.167089

      En el contexto del problema, es importante tomar en consideración
      cómo pudieran afectar los casos atípicos (minoritarios) en la optención
      de la calificación con respecto a los dominantes.
---

**Pregunta 1.1** — ¿De qué fuente proviene el dataset y cuál es la variable objetivo (target)? ¿Por qué tiene sentido hacer regresión sobre ella?

> El dataset seleccionado fue: _UCI ML Repository: Student Performance Dataset_, sugerido como parte de las orientaciones de la práctica. 
> En particular el archivo relacionado con el curso de Matemáticas.

> _Variable objetivo (target)_: G3, asociada con la calificación final del estudiante en el curso de Matemáticas. 

**Pregunta 1.2** — ¿Qué distribución tienen las principales variables numéricas y has encontrado outliers? Indica en qué variables y qué has decidido hacer con ellos.

> Las variables age, failures y absences tienen, al parecer, una distribución gamma.
> 
> Para la detección de outliers se empleó el Método IQR, porque los datos no siguen una distribución normal.
> Se detectaron algunos outliers, pero por la naturaleza de los datos se decide dejarlos porque son casos
> atípicos pero válidos. 
> 
> Por ejemplo, un estudiante de 22 años, que repitió en tres ocasiones.
> O estudiantes con más de 20 ausencias, pero es que las ausencias son muy relevantes
> y deben estar directamente relacionadas con la calificación obtenida.

**Pregunta 1.3** — ¿Qué tres variables numéricas tienen mayor correlación (en valor absoluto) con la variable objetivo? Indica los coeficientes.

> Las variables que están más correlacionadas con la variable objetivo son los resultados en el segundo período G2 (0.9),
> los obtenidos en el primer período G1 (0.8) y el número de veces que ha fallado en aprobar la asignatura con anterioridad (0.36).
> Cómo puede verse hay una fuerte relación entre los resultados en el segundo período y la evaluación final. Quizás sería más
> interesante analizar cómo influyen el resto de variables en los resultados en los períodos evaluativos.

**Pregunta 1.4** — ¿Hay valores nulos en el dataset? ¿Qué porcentaje representan y cómo los has tratado?

> No hay valores nulos en el dataset.

---

## Ejercicio 2 — Inferencia con Scikit-Learn

---
**Preprocesamiento**  
Se empleó **one-hot encoding** para codificar las variables categóricas, el cual crea variables binarias independientes 
para cada nivel de una categoría porque de esta forma se evita imponer un orden numérico entre niveles. 
`LabelEncoder` asigna enteros (0,1,2,...) a las categorías y por tanto introduce una relación ordinal artificial 
que la regresión lineal interpretaría de forma incorrecta entre niveles. 
Para variables nominales como `Mjob` o `Medu` (cuando se tratan como categorías), las dummies preservan la 
no-ordinalidad y permiten estimar un coeficiente separado por nivel, manteniendo interpretabilidad y 
evitando sesgos por ordenación arbitraria.

Se eliminó del análisis las variables `G1` y `G2` para estudiar cómo influyen las variables que describen el contexto
del estudiante en la obtensión de los resultados, ignorando así su evolución académica durante el curso.

Se escala `age`, `failures` y `absences` porque son variables numéricas con unidades y rangos distintos; 
la estandarización (media 0, desviación 1) facilita la convergencia numérica y permite comparar magnitudes 
de coeficientes en términos de desviaciones estándar. Las columnas binarias (0/1) resultantes del One-Hot Encoding 
ya están en una escala comparable y su interpretación como indicadores se mantiene sin escalado; 
escalar variables binarias puede complicar la interpretación de coeficientes y no es necesario para la 
estabilidad del modelo en este contexto.

**Análisis**

    Variables más influyentes
        Variable      Coeficiente
        -------------------------
        higher_yes      1.750880
             sex_M      1.495911
           failures    -1.361698
        famsup_yes     -1.256432
       Mjob_health      1.122322
      Mjob_teacher     -1.108470
      romantic_yes     -1.016167
    guardian_other      0.965251
      Fjob_teacher      0.939985
     schoolsup_yes     -0.915470

---

**Pregunta 2.1** — Indica los valores de MAE, RMSE y R² de la regresión lineal sobre el test set. ¿El modelo funciona bien? ¿Por qué?

- **MAE: 3.395**  
- **RMSE: 4.196**  
- **R²: 0.141**

No es un buen modelo para emplearlo como predictor de la variable objetivo.
Un MAE de 3.395 nos indica que tenemos un fallo en la predicción de más de 3 puntos.
Tenemos evidencia de un "Underfitting" (Subajuste), un valor de R² = 0.141, que es 
un valor bajo nos dice el modelo está sufriendo de sesgo alto. 

Quizás pueda ser explicado por el hecho de que el rendimiento escolar depende de 
factores que no están en el dataset, por ejemplo pueden existir elementos más
importantes para predecir un resultado como pueden ser la motivación, la calidad 
de los profesores o incluso el estado emocional el día del examen.
---

## Ejercicio 3 — Regresión Lineal Múltiple en NumPy

---
Añade aqui tu descripción y analisis:

---

**Pregunta 3.1** — Explica en tus propias palabras qué hace la fórmula β = (XᵀX)⁻¹ Xᵀy y por qué es necesario añadir una columna de unos a la matriz X.

> β = (XᵀX)⁻¹ Xᵀy es la solución que minimiza el error cuadrático medio en regresión lineal, obtenida al proyectar los datos observados sobre el espacio de las variables predictoras.

> La columna de unos permite estimar un término independiente (intercepto), evitando forzar al modelo a pasar por el origen y capturando mejor la tendencia general de los datos.

**Pregunta 3.2** — Copia aquí los cuatro coeficientes ajustados por tu función y compáralos con los valores de referencia del enunciado.

| Parametro | Valor real | Valor ajustado |
|-----------|-----------|----------------|
| β₀        | 5.0       |   4.86499486   |
| β₁        | 2.0       |   2.0636177    |
| β₂        | -1.0      |  -1.11703839   |
| β₃        | 0.5       |   0.43851694   |

> Los valores se acercan bastante a los valores de referencia.

**Pregunta 3.3** — ¿Qué valores de MAE, RMSE y R² has obtenido? ¿Se aproximan a los de referencia?

    MAE  = 1.1665
    RMSE = 1.4612
    R²   = 0.6897

    Los valores de MAE y RMSE se ajustan bastante a los valores de referencia. 
    El R² se aleja un poquito más del valor de referencia. 

**Pregunta 3.4* — Compara los resultados con la reacción logística anterior para tu dataset y comprueba si el resultado es parecido. Explica qué ha sucedido. 

> _Escribe aquí tu respuesta_

---

## Ejercicio 4 — Series Temporales
---
Añade aqui tu descripción y analisis:

---

**Pregunta 4.1** — ¿La serie presenta tendencia? Descríbela brevemente (tipo, dirección, magnitud aproximada).

> La serie muestra una tendencia lineal ascendente muy robusta y clara a lo largo de todo el periodo. 
> La dirección es positiva, con una pendiente de 0.05 unidades diarias, lo que se traduce en un 
> crecimiento anual aproximado de 18.26 unidades. En el gráfico de descomposición (ej4_descomposicion.png), 
> el panel de tendencia captura esta progresión de forma casi perfecta, aunque presenta ligeras ondulaciones 
> debidas a que el componente cíclico de largo plazo se "filtra" parcialmente en la estimación de la tendencia.

**Pregunta 4.2** — ¿Hay estacionalidad? Indica el periodo aproximado en días y la amplitud del patrón estacional.

> Existe una estacionalidad anual definida con un periodo de 365 días. El patrón estacional es complejo 
> (no es una sinusoide simple) porque combina una amplitud principal de 15 y una secundaria de 6, lo que 
> genera dos picos y dos valles por año. La amplitud típica "pico a valle" del patrón es de aproximadamente 
> 32-34 unidades, lo que representa una fluctuación significativa respecto al valor medio de la serie.

**Pregunta 4.3** — ¿Se aprecian ciclos de largo plazo en la serie? ¿Cómo los diferencias de la tendencia?

> Se aprecia un ciclo de largo plazo con un periodo aproximado de 4 años (1461 días). La diferencia 
> fundamental es que la tendencia representa un cambio secular monótono (crecimiento), mientras que 
> el ciclo es una oscilación de baja frecuencia que regresa a la línea base. En la visualización de 
> la serie original, este ciclo se manifiesta como una "joroba" o curvatura suave que abarca varios 
> años, diferenciándose de la estacionalidad anual por su duración mucho más extensa.

**Pregunta 4.4** — ¿El residuo se ajusta a un ruido ideal? Indica la media, la desviación típica y el resultado del test de normalidad (p-value) para justificar tu respuesta.

> El residuo se aproxima a un ruido ideal, pero con matices. Presenta una media de 0.003 (prácticamente nula) 
> y una desviación típica de 3.486, muy cercana al valor teórico de 3.5. El test de normalidad Jarque-Bera 
> arroja un p-valor de 0.449, por lo que no se rechaza la hipótesis de normalidad. Sin embargo, 
> el ACF/PACF muestra que el residuo no es 100% ruido blanco, ya que conserva algo de autocorrelación en 
> lags largos debido a que la descomposición anual no aisló completamente el ciclo de 4 años.

---

*Fin del documento de respuestas*