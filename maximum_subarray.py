"""
Ejercicio 3: Problema del Subarreglo Máximo
Algoritmos: Fuerza Bruta y Divide y Vencerás
Autor: Estudiante David Ramirez Velez CC 1152462417
"""

import time
import random
import matplotlib.pyplot as plt
import seaborn as sns


# ─────────────────────────────────────────────
# ALGORITMO DE FUERZA BRUTA  O(n^2)
# ─────────────────────────────────────────────
def max_subarray_brute_force(arr):
    n = len(arr)
    max_sum = float('-inf')
    best_left, best_right = 0, 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                best_left, best_right = i, j

    return best_left, best_right, max_sum


# ─────────────────────────────────────────────
# ALGORITMO DIVIDE Y VENCERÁS  O(n log n)
# ─────────────────────────────────────────────
def max_crossing_subarray(arr, low, mid, high):
    """Calcula el subarreglo máximo que cruza la mitad."""
    left_sum = float('-inf')
    total = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float('-inf')
    total = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        total += arr[j]
        if total > right_sum:
            right_sum = total
            max_right = j

    return max_left, max_right, left_sum + right_sum


def max_subarray_divide_conquer(arr, low, high):
    """Divide y Vencerás recursivo."""
    # Caso base: un solo elemento
    if low == high:
        return low, high, arr[low]

    mid = (low + high) // 2

    # Caso 1: subarreglo máximo en la mitad izquierda
    left_low, left_high, left_sum = max_subarray_divide_conquer(arr, low, mid)

    # Caso 2: subarreglo máximo en la mitad derecha
    right_low, right_high, right_sum = max_subarray_divide_conquer(arr, mid + 1, high)

    # Caso 3: subarreglo máximo cruza la mitad
    cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)

    # Comparación final: retornar el mayor
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


# ─────────────────────────────────────────────
# MEDICIÓN DE TIEMPOS
# ─────────────────────────────────────────────
def measure_time(func, arr, repetitions=10):
    times = []
    for _ in range(repetitions):
        start = time.perf_counter()
        func(arr, 0, len(arr) - 1) if func == max_subarray_divide_conquer else func(arr)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)


sizes = [10, 50, 100, 200, 500, 1000]
times_brute = []
times_dc = []

for n in sizes:
    arr = [random.randint(-100, 100) for _ in range(n)]
    times_brute.append(measure_time(max_subarray_brute_force, arr))
    times_dc.append(measure_time(max_subarray_divide_conquer, arr))

# ─────────────────────────────────────────────
# GRÁFICA COMPARATIVA
# ─────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="muted")
fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(sizes, times_brute, marker='o', linewidth=2, label='Fuerza Bruta  O(n²)', color='#E74C3C')
ax.plot(sizes, times_dc, marker='s', linewidth=2, label='Divide y Vencerás  O(n log n)', color='#2980B9')

ax.set_xlabel('Tamaño de entrada (n)', fontsize=12)
ax.set_ylabel('Tiempo promedio (segundos)', fontsize=12)
ax.set_title('Comparación: Subarreglo Máximo\nFuerza Bruta vs Divide y Vencerás', fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.set_yscale('log')
plt.tight_layout()
plt.savefig('/content/grafica_sorting.png', dpi=150)

print("Gráfica subarreglo guardada.")

# Verificación con el arreglo del estudiante
arr_estudiante = [1, -1, 5, -2, 4, -6, 2, -4, 1, -7]
low, high, total = max_subarray_divide_conquer(arr_estudiante, 0, len(arr_estudiante) - 1)
print(f"\nArreglo estudiante: {arr_estudiante}")
print(f"Subarreglo máximo: índices [{low}, {high}] → {arr_estudiante[low:high+1]}, suma = {total}")
