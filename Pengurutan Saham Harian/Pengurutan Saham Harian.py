# Fungsi Merge Sort (Rekursif)
import time
import random

# Fungsi Merge Sort (Rekursif)
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

# Fungsi Selection Sort (Iteratif)
def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
        
        
# input data harga saham
# harga_saham = [15000, 12000, 18000, 10000, 20000, 17000]
# Membuat dataset besar (10.000 elemen)
harga_saham = random.sample(range(1000, 100000), 10000)  # 10.000 elemen acak


# Mengurutkan menggunakan Merge Sort
print("Pengurutan Harga Saham dengan Merge Sort:")
merge_sort(harga_saham)
print("Hasil:", harga_saham)

# Mengurutkan menggunakan Selection Sort
# harga_saham = [15000, 12000, 18000, 10000, 20000, 17000]  # Reset data
print("\nPengurutan Harga Saham dengan Selection Sort:")
selection_sort(harga_saham)
print("Hasil:", harga_saham)

print()

# Mengukur waktu eksekusi Merge Sort
merge_sort_data = harga_saham.copy()
start_time = time.perf_counter()
merge_sort(merge_sort_data)
merge_sort_time = time.perf_counter() - start_time
print("Waktu eksekusi Merge Sort:", merge_sort_time, "detik")

# Mengukur waktu eksekusi Selection Sort
selection_sort_data = harga_saham.copy()
start_time = time.perf_counter()
selection_sort(selection_sort_data)
selection_sort_time = time.perf_counter() - start_time
print("Waktu eksekusi Selection Sort:", selection_sort_time, "detik")
