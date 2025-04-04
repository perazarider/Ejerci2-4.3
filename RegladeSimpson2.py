import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        raise ValueError("El número de subintervalos (n) debe ser par.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Puntos del intervalo
    fx = f(x)  # Evaluamos la función en esos puntos
    
    # Regla de Simpson
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    
    return integral

# Parámetros del problema
C = 1e-6  # F
T = 5  # segundos

# Función a integrar (voltaje)
def voltaje(t):
    return 100 * np.exp(-2 * t)

# Solución analítica (para comparar)
solucion_analitica = C * 100 * (1 - np.exp(-2 * T)) / 2

# Valores de n para la regla de Simpson
n_valores = [6, 10, 20, 30]

# Resultados numéricos y errores
resultados = []
errores = []

for n in n_valores:
    resultado_num = C * simpson_rule(voltaje, 0, T, n)
    resultados.append(resultado_num)
    error = abs(resultado_num - solucion_analitica)
    errores.append(error)
    print(f"n = {n}: Carga = {resultado_num:.8f} C, Error = {error:.8f} C")

print(f"\nSolución analítica: {solucion_analitica:.8f} C")

# Gráfica de la función y la aproximación (con n = 30)
t_vals = np.linspace(0, T, 100)
V_vals = voltaje(t_vals)

plt.plot(t_vals, V_vals, label=r"$V(t) = 100e^{-2t}$", color="blue")
plt.fill_between(t_vals, V_vals, alpha=0.3, color="cyan", label="Área aproximada")
plt.scatter(np.linspace(0, T, 30 + 1), voltaje(np.linspace(0, T, 30 + 1)), color="red", label="Puntos de interpolación")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.legend()
plt.title("Carga en el capacitor (Regla de Simpson)")
plt.grid()

# Guardar la figura
plt.savefig("carga_capacitor_simpson.png")
plt.show()

# Gráfica del error en función de n
plt.plot(n_valores, errores, marker='o')
plt.xlabel("Número de subintervalos (n)")
plt.ylabel("Error (C)")
plt.title("Error en la aproximación de la carga")
plt.grid()

# Guardar la figura
plt.savefig("error_carga_capacitor.png")
plt.show()
