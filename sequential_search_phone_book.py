#Amanda Rismawati
#101019005
#Membantu john untuk menemukan nomor telepon jane menggunakan sequential search

def sequential_search_phone_book(BukuTelpon, nama) :
    for entry in BukuTelpon :
        if entry[0] == nama :
            return entry[1]
    return None 

#daftar nama dan nomor telepon
BukuTelpon = [
    ["John Doe", "081234567890"],
    ["Jane Smith", "089876543210"],
    ["Michael Johnson", "087811223344"],
    ["Emily Davis", "082122232425"] 
] 

#mencari nomor telpon Jane 
nama = "Jane Smith"

#Mencari nomor telepon 
NomorTelpon = sequential_search_phone_book(BukuTelpon, nama)

#Menampilkan Hasil
if NomorTelpon :
    print(f"Nomor Telepon Jane : ", NomorTelpon)
else :
    print("Nomor telepon tidak ditemukan.")

