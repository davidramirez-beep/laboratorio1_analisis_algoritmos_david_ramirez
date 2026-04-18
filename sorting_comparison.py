"""
Ejercicio 4: Comparación Merge Sort vs Insertion Sort
Autor: Estudiante David Ramirez Velez CC 1152462417
"""

import time
import random
import matplotlib.pyplot as plt
import seaborn as sns


# ─────────────────────────────────────────────
# MERGE SORT  O(n log n)
# ─────────────────────────────────────────────
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ─────────────────────────────────────────────
# INSERTION SORT  O(n²)
# ─────────────────────────────────────────────
def insertion_sort(arr):
    arr = arr[:]  # no modificar original
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ─────────────────────────────────────────────
# MEDICIÓN DE TIEMPOS
# ─────────────────────────────────────────────
def measure_sort_time(func, arr, repetitions=10):
    times = []
    for _ in range(repetitions):
        arr_copy = arr[:]
        start = time.perf_counter()
        func(arr_copy)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)


sizes = [10, 50, 100, 500, 1000, 5000]
times_merge = []
times_insertion = []

for n in sizes:
    arr = [random.randint(-1000, 1000) for _ in range(n)]
    times_merge.append(measure_sort_time(merge_sort, arr))
    times_insertion.append(measure_sort_time(insertion_sort, arr))

# ─────────────────────────────────────────────
# GRÁFICA COMPARATIVA
# ─────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="muted")
fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(sizes, times_merge, marker='s', linewidth=2, label='Merge Sort  O(n log n)', color='#27AE60')
ax.plot(sizes, times_insertion, marker='o', linewidth=2, label='Insertion Sort  O(n²)', color='#E67E22')

ax.set_xlabel('Tamaño de entrada (n)', fontsize=12)
ax.set_ylabel('Tiempo promedio (segundos)', fontsize=12)
ax.set_title('Comparación: Merge Sort vs Insertion Sort', fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.set_yscale('log')
plt.tight_layout()
plt.savefig('/content/grafica_sorting.png', dpi=150)

print("Gráfica sorting guardada.")

# Verificación con el arreglo del estudiante
arr_estudiante = [1, 1, 5, 2, 4, 6, 2, 4, 1, 7]
print(f"\nArreglo original:  {arr_estudiante}")
print(f"Merge Sort:        {merge_sort(arr_estudiante[:])}")
print(f"Insertion Sort:    {insertion_sort(arr_estudiante[:])}")
