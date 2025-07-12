import os
class DataMahasiswa:
    def __init__(self, file_name="data_mahasiswa.txt"):
        self.file_name = file_name 
    def simpan_data(self):
        nama = input("Masukkan nama lengkap: ")
        nim = input("Masukkan NIM: ")
        with open(self.file_name,'a') as pile:
            pile.write(f"Nama Lengkap : {nama} NIM: {nim}\n")
        print(f"Data {nama} dengan NIM {nim} berhasil disimpan.")
data_mahasiswa = DataMahasiswa("data_mahasiswa.txt")

class BacaData:
    def __init__(self, file_name="data_mahasiswa.txt"):
        self.file_name = file_name
    def baca_data(self):
        with open(self.file_name, 'r') as file:
            data = file.readlines()
        for baris in data:
            if "Nama Lengkap :" in baris and "NIM:" in baris:
                bagian = baris.split("NIM:")
                nama = bagian[0].replace("nama:", "").strip()
                nim = bagian[1].strip()
                print(f"  {nama}   NIM: {nim}")
            else:
                print("Format data tidak valid")
membaca = BacaData("data_mahasiswa.txt")

class Kehadiran:
    def __init__(self, file_hadir="kehadiran.txt"):
        self.file_hadir = file_hadir

    def simpan_kehadiran(self):
        nama = input("Masukkan nama: ")
        status = input("Berikan status (Hadir/Tidak Hadir): ")
        with open(self.file_hadir,'a') as absen:
            absen.write(f"{nama} - {status}\n")
        print(f"Nama '{nama}' status {status} berhasil disimpan.")

    def tampilkan_kehadiran(self):
        print("\nDaftar Kehadiran:")
        with open(self.file_hadir,'r') as file:
            data = file.readlines()
        if not data:
            print("Belum ada data kehadiran.")
        else:
            for baris in data:
                print(baris.strip())

    def cek_hadir_ga(self):
        nama = input("Masukkan nama: ")
        if self.cek_nama(nama):
            print("Nama sudah di daftar.")
        else:
            print("nama belum ada")
        
        print("\nDaftar Kehadiran:")
        with open(self.file_hadir, 'r') as file:
            data = file.readlines()
        if not data:
            print("Belum ada data kehadiran.")
        else:
            for baris in data:
                print(baris.strip())
    def cek_nama(self, nama):
        with open(self.file_hadir, 'r') as file:
            data = file.readlines()

        for baris in data:
            if nama in baris:
                return True
        return False
hadir = Kehadiran("kehadiran.txt")

class FileManager:
    def __init__(self):
        pass
    def hapus_file(self, file_name):
        try:
            if (file_name):
                konfirmasi = input(f"Apa kau yakin mau menghapus file {file_name} (y/n): ")
                if konfirmasi == "y":
                    os.remove(file_name)
                    print(f"file {file_name} berhasil dihapus.")
                else:
                    print(f"file {file_name} tidak di temukan.")
            else:
                print(f"Penghapusan file {file_name} dibatalkan.")
        except Exception:
            print("filenya sudah di gada bro")
menghapus = FileManager()

while  True:
    print("\n","-"*30)
    print("1. Menambahkan nama & nim")
    print("2. Membaca Data")
    print("3. Absensi Mahasiswa")
    print("4. Cek Absen Mahasiswa")
    print("5. Menghapus File")
    print("6. keluar")
    pilihan = input("pilih dgn sesuai 1-6: ")

    if pilihan == "1":
        data_mahasiswa.simpan_data()
    elif pilihan == "2":
        membaca.baca_data()
    elif pilihan == "3":
        hadir.simpan_kehadiran()
        hadir.tampilkan_kehadiran()
    elif pilihan == "4":
        hadir.cek_hadir_ga()
    elif pilihan == "5":
        x = input("pilih file data_mahasiswa.txt / kehadiran.txt(a/b): ")
        if x == "a":
            menghapus.hapus_file("data_mahasiswa.txt")
        elif x == "b":
            menghapus.hapus_file("kehadiran.txt")
    elif pilihan == "6":
        GET_OUT = input('mau keluar kah (y/n): ')
        if GET_OUT == "y":
            break
    else:
        print('MASUKIN YG BENER DONG!!!')





















# ------- INI HANYA SAMPLE DARI AI UNTUK DI TELA'AH SAJA ----------
# ------- MUNGKIN BEBERAPA ADA YG SAMA


# file 1
# class DataMahasiswa:
#     def __init__(self, file_name="data_mahasiswa.txt"):
#         self.file_name = file_name 

#     def simpan_data(self):
#         nama = input("Masukkan nama lengkap: ")
#         nim = input("Masukkan NIM: ")
#         with open(self.file_name,'a') as pile:
#             pile.write(f"nama:{nama} NIM: {nim}\n")
#         print(f"Data {nama} dengan NIM {nim} berhasil disimpan.")
# data_mahasiswa = DataMahasiswa("data_mahasiswa.txt")



# class BacaData:
#     def __init__(self, file_name="data_mahasiswa.txt"):
#         self.file_name = file_name

#     def baca_data(self):
#         with open(self.file_name, 'r') as file:
#             data = file.readlines()
#         for baris in data:
#             if "nama:" in baris and "NIM:" in baris:
#                 bagian = baris.split("NIM:")
#                 nama = bagian[0].replace("nama:", "").strip()
#                 nim = bagian[1].strip()
#                 print(f"Nama: {nama} NIM: {nim}")
#             else:
#                 print("Format data tidak valid")
# membaca = BacaData("data_mahasiswa.txt")

# class Kehadiran:
#     def __init__(self, file_hadir="kehadiran.txt"):
#         self.file_hadir = file_hadir
#     def simpan_kehadiran(self):
#         nama = input("Masukkan nama: ")
#         if self.cek_nama(nama):
#             print("Nama sudah di daftar.")
#             return
#         status = input("Masukkan status (Hadir/Tidak Hadir): ")

#         with open(self.file_name, 'a') as file:
#             file.write(f"{nama} - {status}\n")
#         print(f"Kehadiran {nama} dengan status {status} berhasil disimpan.")
#     def tampilkan_kehadiran(self):
#         print("\nDaftar Kehadiran:")
#         with open(self.file_name, 'r') as file:
#             data = file.readlines()

#         if not data:
#             print("Belum ada data kehadiran.")
#         else:
#             for baris in data:
#                 print(baris.strip())
#     def cek_nama(self, nama):
#         with open(self.file_name, 'r') as file:
#             data = file.readlines()

#         for baris in data:
#             if nama in baris:
#                 return True
#         return False
# hadir = Kehadiran("kehadiran.txt")




#    FILE 2

# class DataMahasiswa:
#     def __init__(self, file_name="data_mahasiswa.txt"):
#         self.file_name = file_name 

#     def simpan_data(self):
#         nama = input("Masukkan nama lengkap: ")
#         nim = input("Masukkan NIM: ")
        
#         with open(self.file_name,'a') as pile:
#             pile.write(f"nama:{nama} NIM: {nim}\n")
#         print(f"Data {nama} dengan NIM {nim} berhasil disimpan.")
# data_mahasiswa = DataMahasiswa("data_mahasiswa.txt")







#   FILE 3

# class DataMahasiswa:
#     def __init__(self, file_name="data_mahasiswa.txt"):
#         self.file_name = file_name

#     def simpan_data(self, nama, nim):
#         with open(self.file_name, "a") as file:
#             file.write(f"{nama},{nim}\n")
#         print("Data berhasil disimpan.")

# # Membuat objek kelas DataMahasiswa
# mahasiswa = DataMahasiswa()

# # Input data mahasiswa
# nama = input("Masukkan nama mahasiswa: ")
# nim = input("Masukkan NIM mahasiswa: ")

# # Simpan data
# mahasiswa.simpan_data(nama, nim)

# # import os

# class BacaData:
#     def __init__(self, file_name="data_mahasiswa.txt"):
#         self.file_name = file_name

#     def baca_data(self):
#         if (self.file_name):
#             with open(self.file_name, "r") as file:
#                 data = file.readlines()
#                 if data:
#                     for baris in data:
#                         nama, nim = baris.split(",")
#                         print(f"Nama Lengkap: {nama} NIM: {nim}",end="")
#                 else:
#                     print("File kosong.")
#         else:
#             print("File tidak ada.")

# # Contoh penggunaan
# bacadata = BacaData()
# bacadata.baca_data()






# class Kehadiran:
#     def __init__(self, file_name="kehadiran.txt"):
#         self.file_name = file_name

#     def simpan_kehadiran(self, nama, status):
#         # Menyimpan data ke dalam file kehadiran.txt
#         with open(self.file_name, "a") as file:
#             file.write(f"{nama} - {status}\n")
#         print("Data kehadiran berhasil disimpan.")

#     def tampilkan_kehadiran(self):
#         # Membaca dan menampilkan data kehadiran
#         try:
#             with open(self.file_name, "r") as file:
#                 data = file.readlines()
#                 if data:
#                     for baris in data:
#                         print(baris.strip())
#                 else:
#                     print("Belum ada data kehadiran.")
#         except FileNotFoundError:
#             print("File kehadiran belum dibuat.")

# # Contoh penggunaan
# kehadiran = Kehadiran()

# # Input data kehadiran
# nama = input("Masukkan nama: ")
# status = input("Masukkan status (hadir/tidak hadir): ")

# # Simpan kehadiran
# kehadiran.simpan_kehadiran(nama, status)

# # Tampilkan daftar kehadiran
# kehadiran.tampilkan_kehadiran()
