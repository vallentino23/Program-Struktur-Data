from collections import deque  # Menggunakan deque untuk efisiensi antrian

# Memisahkan antrian pasien darurat dan pasien biasa
antrian_darurat = deque()  # Deque untuk antrian pasien darurat
antrian_normal = deque()  # Deque untuk antrian pasien normal

def input_angka(pesan):
    """Memastikan input adalah angka positif."""
    while True:
        try:
            nilai = int(input(pesan))
            if nilai > 0:
                return nilai
            else:
                print("❌ Masukkan angka positif!")
        except ValueError:
            print("❌ Input tidak valid. Harap masukkan angka!")

def input_jenis_kelamin():
    """Memastikan input jenis kelamin hanya 'L' atau 'P'."""
    while True:
        jk = input("Masukkan Jenis Kelamin (L/P): ").strip().upper()
        if jk in ["L", "P"]:
            return jk
        print("❌ Jenis kelamin harus 'L' atau 'P'!")

def tambah_pasien():
    """Menambahkan pasien ke dalam daftar antrian."""
    nama = input("Masukkan Nama Pasien: ")
    usia = input_angka("Masukkan Usia Pasien: ")
    jenis_kelamin = input_jenis_kelamin()
    keluhan = input("Masukkan Keluhan: ")
    kontak = input("Masukkan Nomor HP/Kontak: ").strip()
    while not kontak:
        print("❌ Nomor HP/Kontak tidak boleh kosong!")
        kontak = input("Masukkan Nomor HP/Kontak: ").strip()
    prioritas = input("Apakah darurat? (y/n): ").strip().lower() == "y"

    pasien = {
        "Nama": nama,  # Dictionary untuk menyimpan informasi pasien
        "Usia": usia,
        "Jenis Kelamin": jenis_kelamin,
        "Keluhan": keluhan,
        "Kontak": kontak,
        "Prioritas": prioritas
    }

    if prioritas:
        antrian_darurat.append(pasien)  # Deque, menambahkan pasien ke antrian darurat
    else:
        antrian_normal.append(pasien)  # Deque, menambahkan pasien ke antrian normal
    
    print(f"\n Pasien {nama} berhasil ditambahkan ke antrian!\n")

def layani_pasien():
    """Melayani pasien dengan prioritas darurat lebih dahulu."""
    if antrian_darurat:
        pasien = antrian_darurat.popleft()  # Deque, mengambil pasien dari depan antrian darurat
        print(f"\n Melayani pasien DARURAT: {pasien['Nama']}\n")
    elif antrian_normal:
        pasien = antrian_normal.popleft()  # Deque, mengambil pasien dari depan antrian normal
        print(f"\n Melayani pasien NORMAL: {pasien['Nama']}\n")
    else:
        print("\n❌ Tidak ada pasien dalam antrian.\n")

def tampilkan_antrian():  # Dictionary digunakan di dalam fungsi ini
    """Menampilkan daftar pasien dalam antrian darurat dan normal."""
    def tampilkan_daftar(antrian, jenis):
        if antrian:
            print(f"\n{jenis} Antrian:")
            for i, pasien in enumerate(antrian, start=1):  # List: Enumerate digunakan untuk mendapatkan indeks dan elemen
                print(f"{i}. {pasien['Nama']} (Usia: {pasien['Usia']}, {pasien['Jenis Kelamin']}) - Keluhan: {pasien['Keluhan']}, Kontak: {pasien['Kontak']}")
        else:
            print(f"\n {jenis} Antrian kosong.")
    
    print("\n Daftar Antrian Pasien:")
    tampilkan_daftar(antrian_darurat, "🚨 DARURAT")
    tampilkan_daftar(antrian_normal, "✅ NORMAL")
    print()

def batalkan_pasien():
    """Membatalkan pasien berdasarkan nama dari antrian."""
    nama_pasien = input("Masukkan Nama Pasien yang ingin dibatalkan: ")
    for antrian, jenis in [(antrian_darurat, "darurat"), (antrian_normal, "normal")]:
        for pasien in antrian:
            if pasien["Nama"].lower() == nama_pasien.lower():
                antrian.remove(pasien)
                print(f"\n Pasien {pasien['Nama']} telah dibatalkan dari antrian {jenis}.\n")
                return
    print("\n❌ Nama Pasien tidak ditemukan dalam antrian.\n")

# Menu utama program
while True:
    print("\n=== Sistem Antrian Rumah Sakit ===")
    print("1. Tambah Pasien")
    print("2. Layani Pasien")
    print("3. Tampilkan Antrian")
    print("4. Batalkan Pasien")
    print("5. Keluar")
    
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pasien()
    elif pilihan == "2":
        layani_pasien()
    elif pilihan == "3":
        tampilkan_antrian()
    elif pilihan == "4":
        batalkan_pasien()
    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("❌ Pilihan tidak valid. Coba lagi.")
