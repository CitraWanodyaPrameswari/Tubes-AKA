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
        
        # Input manual harga saham
print("Masukkan daftar harga saham (pisahkan dengan spasi):")
input_data = input()  # Misal: "15000 12000 18000 10000 20000 17000"
harga_saham = list(map(int, input_data.split()))  # Mengubah input menjadi list angka

# Mengurutkan menggunakan Merge Sort
print("\nPengurutan Harga Saham dengan Merge Sort:")
merge_sort(harga_saham)
print("Hasil:", harga_saham)

# Reset data dan Mengurutkan menggunakan Selection Sort
harga_saham = list(map(int, input_data.split()))  # Reset data
print("\nPengurutan Harga Saham dengan Selection Sort:")
selection_sort(harga_saham)
print("Hasil:", harga_saham)

# Input data harga saham
# harga_saham = [15000, 12000, 18000, 10000, 20000, 17000]

# Mengurutkan menggunakan Merge Sort
# print("Pengurutan Harga Saham dengan Merge Sort:")
# merge_sort(harga_saham)
# print("Hasil:", harga_saham)

# # Mengurutkan menggunakan Selection Sort
# # harga_saham = [15000, 12000, 18000, 10000, 20000, 17000]  # Reset data
# print("\nPengurutan Harga Saham dengan Selection Sort:")
# selection_sort(harga_saham)
# print("Hasil:", harga_saham)