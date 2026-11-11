
from interpolacion_lagrange import interpolacion_lagrange
from interpolacion_newton import (
    interpolacion_newton,
    diferencias_divididas,
    mostrar_tabla_newton
)


def main():
    print("=" * 65)
    print("INTERPOLACION DE LAGRANGE VS NEWTON")
    print("METODOS NUMERICOS - UNIDAD 5")
    print("=" * 65)

    # Datos de prueba
    x = [1.0, 2.0, 3.0, 4.0]
    y = [1.0, 4.0, 9.0, 16.0]
    x_eval = 2.5

    print("\nDATOS DE ENTRADA")
    print("-" * 65)

    for i in range(len(x)):
        print(f"  x[{i}] = {x[i]:.4f} | y[{i}] = {y[i]:.4f}")

    print(f"\nPunto de evaluacion: x = {x_eval}")

    # Metodo de Lagrange
    resultado_lagrange = interpolacion_lagrange(x, y, x_eval)

    print("\nMETODO DE LAGRANGE")
    print("-" * 65)
    print(f"Resultado: P({x_eval}) = {resultado_lagrange:.10f}")

    # Metodo de Newton
    tabla = diferencias_divididas(x, y)
    resultado_newton = interpolacion_newton(x, y, x_eval)

    print("\nMETODO DE NEWTON")
    print("-" * 65)
    mostrar_tabla_newton(x, tabla)
    print(f"\nResultado: P({x_eval}) = {resultado_newton:.10f}")

    # Analisis comparativo
    diferencia = abs(resultado_lagrange - resultado_newton)

    print("\nANALISIS COMPARATIVO")
    print("-" * 65)
    print(f"Lagrange: {resultado_lagrange:.10f}")
    print(f"Newton:   {resultado_newton:.10f}")
    print(f"Diferencia absoluta: {diferencia:.12f}")

    if diferencia < 1e-10:
        print("CONCLUSION: Ambos metodos coinciden")
        print("dentro de la tolerancia numerica.")
    else:
        print("CONCLUSION: Existe una diferencia numerica.")

    print("\n" + "=" * 65)
    print("EJECUCION FINALIZADA")
    print("=" * 65)


if __name__ == "__main__":
    main()
