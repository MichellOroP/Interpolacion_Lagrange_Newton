
def validar_datos(x, y):
    if x is None or y is None:
        raise ValueError("Los arreglos no pueden ser nulos.")

    if len(x) == 0 or len(y) == 0:
        raise ValueError("Los arreglos no pueden estar vacios.")

    if len(x) != len(y):
        raise ValueError("Los arreglos deben tener el mismo tamaño.")

    if len(set(x)) != len(x):
        raise ValueError("Los valores de x no pueden repetirse.")


def interpolacion_lagrange(x, y, x_eval):
    """
    Calcula la interpolacion polinomial de Lagrange.

    x: nodos de interpolacion
    y: valores de la funcion
    x_eval: punto donde se evalua el polinomio
    """
    validar_datos(x, y)

    n = len(x)
    resultado = 0.0

    for i in range(n):
        termino = y[i]

        for j in range(n):
            if i != j:
                termino *= (x_eval - x[j]) / (x[i] - x[j])

        resultado += termino

    return resultado
