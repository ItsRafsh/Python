# pertemuan 2

# sepatu = 120000
# diskon = 100*(12/100)
# total_diskon = diskon * 1000
# print("dapat potongan",total_diskon)
# harga_final = sepatu - total_diskon
# print("total nya: ",int(harga_final))


# ini yg beneer
# sepatu = 120000
# diskon = 12
# totalnya = sepatu - (sepatu*diskon/100)

# bitcoin = 950000000
# drop = 40
# total = bitcoin - (bitcoin*drop/100)
# print(f"{total:,}")

# bitcoin = 1600000000
# drop = 40
# total = bitcoin - (bitcoin*drop/100)
# print(int(total))








# pertemuan 4

# data = {
#     104 : {'nama' : "Rafa",
#         'ortu' : {'ayah' : 'geldrd','ibu' : 'tutise'}}
# }
# print(data[104]['ortu']['ayah'])









# pertemuan 5

# pi = 22/7
# v = float(input("masukan r : "))
# t = float(input("masukin tinggi: "))
# hasil = pi * (v**2) * t

# print(f"totalnya = {hasil}")








# pertemuan 6

# cowo = ['agus','lapter','ngishinm','adus']
# warna = ['merah','kuning','oren','biru']

# print(cowo)
# print(warna)
# print("----------- silahkan pilih ----------- \n")
# orang = input("nama orangnya: ")
# orgbaju = input('warna maju nya: ')

# if orang in cowo:
#     print(f"{orang} wahh")
#     if orgbaju in warna:
#         print(f'kamu {orgbaju} flag')
#     else:
#         print('red flag')
# else:
#     print('green flag')













# pertemuan 8

# buatan bagus
# n = 5
# hasil = 1
# for i in range(n,0,-1):
#     hasil *= i
#     print(f"Nilai i: {i}")
#     print(f"nilai faktorial: {hasil}\n")
# print(f"hasil total semuanya: {hasil}")

# hasil = 1
# for i in range(1,4+1):
#     hasil *= i

# print(hasil)











# pertemuan 11
# try:
#     num = int(input("masukjan nilai: "))
#     hasil = 10/num
# except ZeroDivisionError:
#     print('jangan masukin angka 0')
# except ValueError:
#     print('jangan masukan string')
# else:
#     print(f'hasilnya adalah: {hasil}')

# data = [10,5,0,'a',None]

# for item in data:
#     try:
#         hasil = 10/item
#         print(hasil)
#     except Exception as e:
#         print(f'error: {e}')




# def persegi(S):
#     return f"hasilnya: {S * S}"


# print('calculator bangun datar dan bangun ruang')
# print("""pilih kategori :
# 1. bangun datar
# 2. bangun ruang""")
# try:
#     pilihan = int(input("silahkan pilih: "))
# except ValueError:
#     print("kmu masukin string")

# if pilihan == 1:
#     print('\n--- silahkan pilih bangun datar ---')
#     print('1.persegi\n2.persegi panjang\n3.segitiga\n4.jajar genjang')
#     milih = int(input('pilih 1-4: '))

#     if milih == 1:
#         try:
#             S = float(input('masukan sisi: '))
#         except ValueError:
#             print('salah huruf kmnu, kalkulasi salah')
#         except ArithmeticError:
#             print('salah huruf kmnu, kalkulasi salah')
#         except NameError:
#             print('salah huruf kmnu, kalkulasi salah')
#         else:
#             print(f"hasilnya: {S * S}")

#     elif milih == 2:
#         panjang = float(input('masukan panjang: '))
#         lebar = float(input('masukan lebar: '))
#         print(f"hasilnya: {panjang * lebar}")

#     elif milih == 3:
#         alas = float(input('masukan alas: '))
#         tinggi = float(input('masukan tinggi: '))
#         print(f"hasilnya: {1/2*alas*tinggi}")
        
#     elif milih == 4:
#         alas = float(input('masukan alas: '))
#         tinggi = float(input('masukan tinggi: '))
#         print(f"hasilnya: {alas*tinggi}")

# elif pilihan == 2:
#     print('\n--- silahkan pilih bangun ruang ---')
#     print('1.kubus\n2.balok')
#     milih_lagi = int(input('pilih 1-2: '))

#     if milih_lagi == 1:
#         sisi = float(input('masukan sisi: '))
#         print(f"hasilnya kubus: {sisi**3}")

#     elif milih_lagi == 2:
#         panjang = float(input('masukan panjang: '))
#         lebar = float(input('masukan lebar: '))
#         tinggi = float(input('masukan tinggi: '))
#         print(f"hasilnya balok: {panjang * lebar * tinggi}")

#     else:
#         print("pilihanyya cuma 1 dan 2 broo")











# pertemuan 15
'''
class Mahasiswa:
atribut:    nama, nim, jurusan
fungsi:     panggilan, ID, Prodi

class Kucing:
atribut:    nama, suara
fungsi:     panggilan, jenisSuara, berlari

class pintu:
atribut:    jenis, bentuk
fungsi:     cara membuka, fitur

class buah
atribut:    nama,rasa,asal
fungsi:     rasanya dimakan, tumbuh dimana, warna

class motor
atribut:    jenis,merek,asal
fungsi:     berjalan, menyala, suara knalpot

'''








# petermuan 16
# class AkunBank:
#     def __init__(self,nama,saldo):
#         self.nama = nama
#         self.__saldo = saldo
    
#     def saldo(self):
#         print(f"saldo kau: {self.__saldo}")

# rafa = AkunBank('Rafa',1000000)
# # print(rafa.__saldo)       ini ga bisa di akses
# rafa.saldo()

# class Mobil:
#     def __init__(self,merk,warna,tahun):
#         self.merk = merk
#         self.warna = warna
#         self.tahun = tahun
#         self.menyala = False

#     def mesin_menyala(self):
#         if self.menyala == False:
#             print(f"mobil {self.merk} menyala")
#         else:
#             print(f"mobil {self.merk} sudah menyala bos")

# punyaLu = Mobil('honda','putih',2020)
# # punyaLu.mesin_menyala()

# class Mahasiswa:
#     def __init__(self,nama,nim,prodi,gender,akt):
#         self.nama = nama
#         self.nim = nim
#         self.prodi = prodi
#         self.gender = gender
#         self.angkatan = akt

#     def tampilkan(self):
#         print(f"\nnama: {self.nama}\nNIM: {self.nim}\nJurusan: {self.prodi}\nGender: {self.gender}\nAngkatan: {self.angkatan}\n")

#     def mahasiswaAktif(self):
#         if self.angkatan == 2024:
#             print(f"{self.nama} ternyata orang yg aktif\n")
#         else:
#             print(f"kamu angkatan {self.angkatan}, lagi sibuk skripsi?\n")
    
#     def ayamGeprek(self):
#         if self.gender == "cewek" or self.gender == "perempuan":
#             print(f"setiap pulang {self.nama} selalu beli ayam geprek\n")
#         else:
#             print(f"kau {self.nama} paling lagi rapat\n")

# bagus = Mahasiswa('Naon',9789,'ilmu komputer','cowok','2023')
# bagus.tampilkan()
# bagus.mahasiswaAktif()
# bagus.ayamGeprek()








# pertemuan 17

# class Pengguna:
#     def __init__(self,nama,id_anggota):
#         self.nama = nama
#         self.idAnggota = id_anggota
    
#     def info(self):
#         print(f"Nama: {self.nama}\nID: {self.idAnggota}")

#     def hak_akses(self):
#         print('admin adalah kunci utama kelass')

# class Admin(Pengguna):
#     def __init__(self, nama, id_anggota, jabatan):
#         super().__init__(nama, id_anggota)
#         self.jabatan = jabatan
    
#     def info(self):     #disebut juga polymorphism
#         super().info()
#         print(f'jabatan: {self.jabatan}')
    
#     def hak_akses(self):
#         print('admin adalah raja')

# userharis = Pengguna('Haris',10000)
# rafa = Admin('Rafa',4233423,'ketum dpr')

# rafa.info()
# userharis.hak_akses()
# rafa.hak_akses()









# pertemuan 19              
# --------------------------------- SYSTEM CRUD DATA MAHASISWA ---------------------------------
# masih ada yg error. perbaiki sendiri

# class DatabaseMahasiswa:
#     def __init__(self,namaFile,nimFile):
#         self.nama_file = namaFile
#         self.nim_file = nimFile

#         file1 = open(self.nama_file,'a')
#         file2 = open(self.nim_file,'a')
#         file1.close()
#         file2.close()



#     def add_mhs(self,nama,nim):
#         with open(self.nim_file,'r')as nimfile:
#             nim_list = nimfile.readlines()
#         for yg_ada in nim_list:
#             if nim == yg_ada.strip():
#                 print(f'Error: mahasiswa dengan nim {nim} sudah ada')
#                 return
#         with open(self.nama_file,'a') as namafile, open(self.nim_file,'a')as nimfile:
#             namafile.write(nama+'\n')
#             nimfile.write(nim+'\n')
#         print(f'Mahasiswa {nama} NIM {nim} sudah di tambah!.')



#     def show_all(self):
#         with open(self.nama_file,'r') as namafile:
#             nama = namafile.readlines()
#         with open(self.nim_file,'r') as nimfile:
#             nim = nimfile.readlines()

#         if len(nama) == 0:
#             print('gada data di sini')
#         else:
#             print('\ndata mahasiswa:')
#             print(f'{'No.':<5}{'Nama':<20}{'NIM':<15}')
#             print('-'*40)
#             for i in range(len(nama)):
#                 print(f'{i+1:<5}{nama[i].strip():<20}{nim[i].strip():<15}')

#         # with open(self.nama_file,'r') as namafi, open(self.nim_file,'r') as nimfi:
#         #     nama = namafi.readlines()
#         #     nim = nimfi.readlines()             #ini punya 01abdan
#         # print('No\tNama\t\tNIM')
#         # print('-'*30)
#         # for i in range(len(nama)):
#         #     print(f'{i+1}.\t{nama[i].strip()}\t\t{nim[i].strip()}')
    




# # pertemuan 20


#     def delete_student(self,nim):
#         students = self.student_to_dictionary()
#         new_students = []

#         for student in students:
#             if student['NIM'] != nim:
#                 new_students.append(student)
#         if len(new_students) < len(students):
#             self.save_students(new_students)
#             print('siswa berhasil di hapus')
#         else:
#             print('student with specified NIM not found')



#     def student_to_dictionary(self):
#         with open(self.nama_file,'r') as namafile:
#             namalist = namafile.readlines()
#         with open(self.nim_file,'r') as nimfile:
#             nimlist = nimfile.readlines()

#         students = []
#         for i in range(len(namalist)):
#             student = {'Nama': namalist[i].strip(), 'NIM': nimlist[i].strip()}
#             students.append(student)
#         return students



#     def search_student_by_nim(self,nim):
#         with open(self.nama_file,'r') as namafile:
#             namalist = namafile.readlines()
#         with open(self.nim_file,'r') as nimfile:
#             nimlist = nimfile.readlines()
#         for i in range(len(nimlist)):
#             if nimlist[i].strip() == nim:
#                 print(f'Student Found: Nama: {namalist[i].strip()}, NIM: {nimlist[i].strip()}')
#                 return {'Nama': namalist[i].strip(), 'NIM': nimlist[i].strip()}
#         print('Student with specified NIM not found.')
#         return None



#     def save_students(self,students):
#         with open(self.nama_file,'w') as nama_file:
#             for student in students:
#                 nama_file.write(student['Nama'+'\n'])
#         with open(self.nim_file,'w') as nim_file:
#             for student in students:
#                 nim_file.write(student['NIM'] + '\n')



#     def update_student(self,old_nim, new_nama=None, new_nim=None):
#         students = self.student_to_dictionary()
#         updated = False

#         for student in students:
#             if student['NIM'] == old_nim:
#                 if new_nama:
#                     student['Nama'] = new_nama
#                 if new_nim:
#                     student['NIM'] = new_nim
#                 updated = True
#                 break
#         if updated:
#             self.save_students(students)
#             print('student updated successfully')
#         else:
#             print('student with specified NIM not found.')



# rafa = DatabaseMahasiswa('Mahasiswa.txt','NIM.txt')
# rafa.add_mhs('Rafa','2332')
# rafa.show_all()

# --------------------------------- SYSTEM CRUD DATA MAHASISWA ---------------------------------







# pertemuan 24
# lanjutan kalkulator   CALCULATOR yg perfrct di file GUI_CALCULATOR.py
import tkinter as tk
calculation = ''

def input_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)
def clear():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')
def calculate():
    global calculation
    result = str(eval(calculation))
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, result)
    calculation = result


def parenthesis_click():
    global calculation
    open_count = calculation.count('(')
    close_count = calculation.count(')')
    if open_count > close_count:
        calculation += ')'
    else:
        calculation += '('


root = tk.Tk()
root.geometry('300x520')
root.title('Basic Calculator')
root.resizable(False,False)

# text field
text_result = tk.Text(root, height=2, width=16, font=('Arial','24'))
text_result.grid(columnspan=5)

# komponen calculation
bersih = tk.Button(root, text='C', width=5, height=3, font=('Arial','14'), command=clear)
bersih.grid(row=1,column=1)

kurung = tk.Button(root, text='()', width=5, height=3, font=('Arial','14'), command=parenthesis_click)
kurung.grid(row=1,column=2)

pangkat = tk.Button(root, text='^', width=5, height=3, font=('Arial','14')) #ommand=pass)
pangkat.grid(row=1,column=3)

bagi = tk.Button(root, text='/', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation('/'))
bagi.grid(row=1,column=4)


# komponen button 1
tombol1 = tk.Button(root, text='1', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation(1))
tombol1.grid(row=2,column=1)

tombol2 = tk.Button(root, text='2', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation(2))
tombol2.grid(row=2,column=2)

tombol3 = tk.Button(root, text='3', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation(3))
tombol3.grid(row=2,column=3)

tombolmul = tk.Button(root, text='+', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation('+'))
tombolmul.grid(row=2,column=4)


# komponen button 2
tombol4 = tk.Button(root, text='4', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation(4))
tombol4.grid(row=3,column=1)

tombol5 = tk.Button(root, text='5', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation(5))
tombol5.grid(row=3,column=2)

tombol6 = tk.Button(root, text='6', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation(6))
tombol6.grid(row=3,column=3)

tombolmulx = tk.Button(root, text='x', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation('*'))
tombolmulx.grid(row=3,column=4)


# komponen button 3
tombol7 = tk.Button(root, text='7', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation(7))
tombol7.grid(row=4,column=1)

tombol8 = tk.Button(root, text='8', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation(8))
tombol8.grid(row=4,column=2)

tombol9 = tk.Button(root, text='9', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation(9))
tombol9.grid(row=4,column=3)

tombol_mines = tk.Button(root, text='-', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation('-'))
tombol_mines.grid(row=4,column=4)


# komponen finishing
tombol0 = tk.Button(root, text='0', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation(0))
tombol0.grid(row=5,column=2)

tomboldot = tk.Button(root, text='.', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation('.'))
tomboldot.grid(row=5,column=1)


# tombol9 = tk.Button(root, text='9', width=5, height=3, font=('Arial','14'), command=lambda: input_to_calculation(9))
# tombol9.grid(row=4,column=3)

tombolequal = tk.Button(root, text='=', width=12, height=3, font=('Arial','14'), command=calculate)
tombolequal.grid(row=5,column=3, columnspan=2)

root.mainloop()
