
from interpolacion_lagrange import validar_datos


def diferencias_divididas(x, y):
    """
    Construye la tabla de diferencias divididas de Newton.
    """
    validar_datos(x, y)

    n = len(x)
    tabla = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        tabla[i][0] = float(y[i])

    for j in range(1, n):
        for i in range(n - j):
            numerador = tabla[i + 1][j - 1] - tabla[i][j - 1]
            denominador = x[i + j] - x[i]

            tabla[i][j] = numerador / denominador

    return tabla


def interpolacion_newton(x, y, x_eval):
    """
    Evalua el polinomio interpolante de Newton.
    """
    tabla = diferencias_divididas(x, y)
    n = len(x)

    resultado = tabla[0][n - 1]

    for i in range(n - 2, -1, -1):
        resultado = resultado * (x_eval - x[i]) + tabla[0][i]

    return resultado


def mostrar_tabla_newton(x, tabla):
    """
    Muestra la matriz de diferencias divididas.
    """
    n = len(x)

    print("\nMATRIZ DE DIFERENCIAS DIVIDIDAS DE NEWTON")
    print("-" * (16 * (n + 1)))

    encabezados = ["x"] + [f"Orden {j}" for j in range(n)]
    print("".join(f"{h:>16}" for h in encabezados))

    for i in range(n):
        print(f"{x[i]:>16.6f}", end="")

        for j in range(n):
            if i + j < n:
                print(f"{tabla[i][j]:>16.6f}", end="")
            else:
                print(f"{'':>16}", end="")

        print()

    print("-" * (16 * (n + 1)))
