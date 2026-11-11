# Interpolacion_Lagrange_Newton
Implementación en Python de los métodos de interpolación de Lagrange y Newton, con análisis comparativo.


# Interpolación de Lagrange vs. Newton

## Descripción

Proyecto de la Unidad 5 de la asignatura Métodos Numéricos del Instituto Tecnológico Superior de Xalapa.

Se implementan en Python dos métodos de interpolación polinomial:

- Interpolación de Lagrange.
- Diferencias Divididas de Newton.

El objetivo es evaluar ambos métodos utilizando los mismos datos, comparar sus resultados y analizar sus características matemáticas y computacionales.

## Objetivos

- Implementar el método de interpolación de Lagrange.
- Implementar el método de diferencias divididas de Newton.
- Construir y visualizar la matriz de diferencias divididas.
- Evaluar ambos métodos en un mismo punto.
- Comparar los resultados y calcular la diferencia absoluta.

## Tecnologías utilizadas

- Lenguaje: Python 3.10 o superior.
- Editor recomendado: Visual Studio Code.
- Control de versiones: Git y GitHub.
- Bibliotecas externas: No se requieren.

## Estructura del proyecto

```text
Interpolacion_Lagrange_Newton/
|
|-- interpolacion_lagrange.py
|-- interpolacion_newton.py
|-- main.py
|-- README.md
```

## Descripción de los archivos

### interpolacion_lagrange.py

Implementa el método de Lagrange mediante el cálculo de los polinomios base. Incluye validaciones para evitar arreglos vacíos, tamaños incompatibles y nodos repetidos.

### interpolacion_newton.py

Implementa el método de Newton mediante una tabla de diferencias divididas. Permite calcular el polinomio interpolante y mostrar la matriz en consola.

### main.py

Ejecuta ambos métodos utilizando los mismos datos y muestra los resultados, la matriz de Newton y la diferencia absoluta.

## Datos de prueba

Se utiliza la función:

f(x) = x²

| x | f(x) |
|---|------|
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 4 | 16 |

Punto de evaluación:

x = 2.5

## Resultados esperados

| Método | Resultado |
|--------|-----------|
| Lagrange | 6.250000 |
| Newton | 6.250000 |

Diferencia absoluta esperada: 0.000000

Ambos métodos representan el mismo polinomio interpolante, aunque sus procedimientos de construcción son diferentes.

## Instrucciones de ejecución

1. Descargar o clonar este repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Verificar que Python esté instalado.
4. Abrir una terminal en la carpeta del proyecto.
5. Ejecutar:

```bash
python main.py
```

El programa mostrará los datos de entrada, los resultados de Lagrange y Newton, la matriz de diferencias divididas y el análisis comparativo.

## Análisis de complejidad

La implementación directa de Lagrange tiene una complejidad temporal O(n²).

La construcción de la tabla de diferencias divididas de Newton tiene una complejidad temporal O(n²).

Una vez calculados los coeficientes, el polinomio de Newton puede evaluarse en O(n) utilizando la forma anidada.

## Conclusión

Los métodos de Lagrange y Newton permiten construir un polinomio que pasa por un conjunto de puntos conocidos.

Aunque ambos producen resultados matemáticamente equivalentes, Newton facilita la incorporación de nuevos nodos cuando se conservan las diferencias divididas previamente calculadas.

Este proyecto permite comprender su implementación, funcionamiento y diferencias computacionales.

## Asignatura

Métodos Numéricos - Unidad 5

Instituto Tecnológico Superior de Xalapa

Ingeniería en Sistemas Computacionales
