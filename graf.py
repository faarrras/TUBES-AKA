import matplotlib.pyplot as plt
import time
import random

# Fungsi Iteratif untuk Mengurutkan Harga
def sortPricesIterative(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Fungsi Rekursif untuk Mengurutkan Harga
def sortPricesRecursive(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return sortPricesRecursive(left) + [pivot] + sortPricesRecursive(right)

# Ukuran data untuk pengujian
data_sizes = [10, 100, 500, 1000, 2000, 5000]
iterative_times = []
recursive_times = []

# Pengujian waktu untuk setiap ukuran data
for size in data_sizes:
    test_data = [random.randint(1, 10000) for _ in range(size)]

    # Iterative
    start_time = time.time()
    sortPricesIterative(test_data.copy())
    iterative_times.append(time.time() - start_time)

    # Recursive
    start_time = time.time()
    sortPricesRecursive(test_data.copy())
    recursive_times.append(time.time() - start_time)

# Membuat grafik perbandingan
plt.figure(figsize=(10, 6))
plt.plot(data_sizes, iterative_times, label='Iterative', marker='o')
plt.plot(data_sizes, recursive_times, label='Recursive', marker='o')

plt.title('Comparison of Iterative vs Recursive Sorting Algorithms')
plt.xlabel('Input Size (number of elements)')
plt.ylabel('Time Taken (seconds)')
plt.legend()
plt.grid(True)
plt.show()

