#Amanda Rismawati
#10109005
#Mencari definisi kata yang diinginkan 

def binary_search_dictionary(Kamus, target) :
    left = 0
    right = len(Kamus) - 1

    while left <= right :
        mid = (left + right) // 2
        if Kamus[mid][0] == target :
            return Kamus[mid][1]
        elif Kamus[mid][0] < target :
            left = mid + 1
        else :
            right = mid - 1

    return "Kata ini pada Kamus tidak ditemukan!"

Kamus = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

target = input("Masukan kata yang ingin di cari pada Kamus : ")
definisi = binary_search_dictionary(Kamus, target)

print(f"Definisi kata {target} : {definisi}")