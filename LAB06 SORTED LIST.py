# NAMA = Tristan Fiqri Ara Darmawan
# NPM = 2606888534
# KELAS = DDP-B 

import random

anggota = []
nama_unik = set()
TUGAS = ("Menyapu", "Mengepel", "Merapikan")
petugas = {}
cadangan = []

print("=== PEMBAGIAN PIKET DEK DEPE ===")
print("1. Tambah anggota")
print("2. Simulasi piket")
print("3. Rekap")
print("4. Selesai")

while True:
    menu = (input("Pilih menu: "))
    
    if menu == "1":
        nama = input("Nama anggota: ").strip().lower()
        
        if nama in nama_unik:
            print("Anggota sudah terdaftar.")
        else:
            anggota.append(nama)
            nama_unik.add(nama)
            print(f"Anggota {nama} ditambahkan")
    
    elif menu == "2":
        k = int(input("Jumlah petugas: "))
        ruang = int(input("Nomor ruang:"))
        
        if 1 <= k <= len(anggota):
            cadangan = anggota.copy()
            petugas.clear()
            print(f"Hasil simulasi ruang {ruang}:")
            
            for i in range(k):
                indeks = random.randrange(len(cadangan))
                nama = anggota.pop(indeks)
                tugas = TUGAS[i % len(TUGAS)]
                petugas[nama] = tugas
                print(f"{i + 1}. {nama} -> {tugas}")
                
        else:
            print("Jumlah petugas tidak valid.")
    
    elif menu == "3":
        print(f"Total anggota unik: {len(nama_unik)}")
        if anggota:
            print("Anggota: " + ", ".join(anggota))
        else:
            print("Anggota: -")
        
        if not petugas:
            print("Belum ada hasil simulasi")
        else:
            print("PEtugas simulasi terakhir: ")
            for nama, tugas in petugas.items():
                print(f"{nama} -> {tugas}")
                
    elif menu == "4":
        print("Simulasi paket selesai. Sampai jumpa!")
        break
    
    else:
        print("Menu tidak valid.")
                













