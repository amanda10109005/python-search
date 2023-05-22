#Amanda Rismawati
#101019005
#Temukan bilangan prima dalam daftar bilangan 

def is_prime(n):
    if n <= 1 :
        return False 
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0:
            return False
    return True

def sequential_search_prime(daftar_bilanganku) :
    bilanganku = []
    for daftar in daftar_bilanganku :
        if is_prime(daftar) :
            bilanganku.append(daftar)
    return bilanganku

daftar_bilanganku = [7, 10, 13, 6, 17, 22, 19]
bilangan_prima = sequential_search_prime(daftar_bilanganku)

print("Bilangan prima yang ditemukan : ", bilangan_prima)