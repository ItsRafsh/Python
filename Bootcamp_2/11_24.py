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











# pertemuan 12

# cara memanggil diluar folder. fungsi r itu row
# def tulis(nama):
#     with open(nama,'a') as file:
#         file.write('woii cutyy')
# tulis(r'BagusCamp\contoh.txt')



# with open(r'BagusCamp\contoh.txt','a') as file:
#     file.write("""
# Yth. Ranaon
# kamu teh kumaha uey
# sala mencari
# """)



# with open(r'BagusCamp\game.txt','r+') as file:
#     isi = file.readlines()
#     print(f'pemain sebelumnya: {isi[0]}',end='')
#     print(f'jumlah percobaan: {isi[1]}')

#     nama = input('masukin naamlu: ')
#     jumlaNyoba = 0
#     angka = 10
#     benar = False
#     while not benar:
#         tebak = int(input('masukan tebakanmu: '))
#         jumlaNyoba = jumlaNyoba + 1
#         if tebak > angka :
#             print('tebakan mu lebih besar')
#         elif tebak < angka:
#             print('tebakan mu lebih kecil')
#         else:
#             print('bener brooo')
#             benar = True
# file = open(r'BagusCamp\game.txt','r+')
# file.write(f"{nama} \n{jumlaNyoba}")
# file.close()










# pertemuan 13
# import math
# print(math.sqrt(25))                #selalu akar pangkat 2
# hasil = math.sin(math.radians(72))
# print(f"{hasil:.2f}")

# import module as m
# m.sapa('rafa')

# import random
# # def ini masukin ke module.py
# def pwGenerator():
#     lower = 'abcdefghijklmnopqrstuvwxyz'
#     upper = lower.upper()
#     digit = '0123456789'
#     symbol = '{:"<>?|+_)(~!@#$%^&*)}'

#     all_char = lower + upper + digit +symbol
#     # pw = "".join(random.sample(all_char,8))
#     # print(pw)

#     length = random.randint(8,16)
#     password = random.choices(all_char, k=length)
#     hasil = ''.join(password)
#     # return hasil
#     print(hasil)

# pwGenerator()









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

# bagus = Mahasiswa('Bagus',9789,'ilmu komputer','cowok','2023')
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




# import math

# class Calculator:
#     def __init__(self):
#         pass

#     def penjumlahan(self,angka1,angka2):
#         self.angka1 = angka1
#         self.angka2 = angka2
#         print(self.angka1 + self.angka2)

#     def pengurangan(self,angka1,angka2):
#         self.angka1 = angka1
#         self.angka2 = angka2
#         print(self.angka1 - self.angka2)
        
#     def perkalian(self,angka1,angka2):
#         self.angka1 = angka1
#         self.angka2 = angka2
#         print(self.angka1 * self.angka2)

#     def pembagian(self,angka1,angka2):
#         self.angka1 = angka1
#         self.angka2 = angka2
#         print(self.angka1 / self.angka2)



# class Scientific(Calculator):
#     def __init__(self):
#         super().__init__()

#     def penjumlahan_sin(self,derajat1,derajat2):
#         self.radiant1 = math.radians(derajat1)
#         self.radiant2 = math.radians(derajat2)
#         self.hasil = self.penjumlahan(math.sin(self.radiant1), math.sin(self.radiant2))
#         print(f"hasil sin{derajat1} + sin{derajat2} = {self.hasil}")
    
#     def penjumlahan_cos(self,derajat1,derajat2):
#         self.radiant1 = math.radians(derajat1)
#         self.radiant2 = math.radians(derajat2)
#         self.hasil = self.penjumlahan(math.cos(self.radiant1), math.cos(self.radiant2))
#         print(f"hasil cos{derajat1} + cos{derajat2} = {self.hasil}")

#     def penjumlahan_tan(self,derajat1,derajat2):
#         self.radiant1 = math.radians(derajat1)
#         self.radiant2 = math.radians(derajat2)
#         self.hasil = self.penjumlahan(math.tan(self.radiant1), math.tan(self.radiant2))
#         print(f"hasil tan{derajat1} + tan{derajat2} = {self.hasil}")

# rafa = Scientific()
# rafa.penjumlahan_sin(1,2)











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












# pertemuan 21
# setiap spasi artinya beda kolom
# import pandas as pd

# # ------------------- ini merupakan car-sales.csv ------------------- 
# data = pd.read_csv('car-sales.csv')
# data.loc[9,'colour'] = 'Yellow'
# data.tail()
# # data.iloc[7]

# data.head()

# # ngefilter sebuah dataFrame 
# data[(data['Doors'] == 4) & (data['Colour'] == 'White')]

# data['Price'] = data['Price'].str.replace('$','')
# # data['Price'] = data['Price'].str.replace(',','').astype(float)

# data.head()

# # data['Fuel Consumsiption (1)'] = (data['Odometer (KM)'])

# data['Price (Rp)'] = (data['Price'] * 16275)
# # data['Price (Rp)'] = 'Rp. ' + (data['Price'] * 16275).astype(str)   kalo mau tampilkan Rp
# data.head()

# avg = data['Price'].mean()
# max = data['Price'].max()
# min = data['Price'].min()
# median = data['price'].median()
# std_dev = data['Price'].std()
# print(f'{avg}, {max}, {std_dev:.2f}')

# data.drop(columns=['Price (Rp)'], inplace=True)

# data.head()
# # cara save data nya
# # data.to_csv('new-car-sales.csv')



# ------------------- ini merupakan jual-motor.csv ------------------- 

# data_motor =pd.read_csv('jual-motor.csv')
# data_motor.head()

# data_motor['Kapasitas Mesin'] = data_motor['Kapasitas Mesin'].str.replace('cc', '')
# data_motor['Harga (Rp)'] = data_motor['Harga (Rp)'].str.replace(',', '') #.astype(float)
# # data_motor['Harga (Rp)'] = data_motor['Harga (Rp)'].str.replace('Rp.', '').astype(int) ini ga dipake
# data_motor.head()

# data_motor['Sisa Umur'] = (10 - (2025 - data_motor['Tahun'])).astype(str) + 'Tahun'
# data_motor.head()













# pertemuan 22
# import requests
# respon = requests.get(url='http://api.open-notify.org/iss-now.json')
# print(respon)
#1xx = artinya hold on     2xx = success       3xx = pergi lu      4xx = masalah ada di pengguna    5xx = masalah ada di server
# print(respon.status_code) #buat cek klo API ada yg error

# data = respon.json()
# # print(data)
# lat = data['iss_position']['latitude']
# long = data['iss_position']['longitude']
# position = (lat, long)
# print(f'POSISI data ISS:\t{position}')


# my_lat = -1.909870
# my_long = 116.194321
# my_format = 0
# my_timzone = 'Asia/Hong_Kong'
# # day = 


# parameters = {
#     'lat':my_lat,
#     'lng':my_long,
#     'tzid':my_timzone
    
# }
# respon = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
# respon.raise_for_status()
# data = respon.json()

# zone = data['tzid']
# sunrise = data['results']['sunrise']
# sunset = data['results']['sunset']


# print(f'Sunset at {sunset} in gatau {sunrise}')
# print(data)













# pertemuan 23
# import tkinter as tk

# def on_click():
#     label2.config(text=f'Halo {entry.get()}')

# root = tk.Tk()
# root.title('Basic Calculator')
# root.geometry('600x200')
# # label
# label = tk.Label(root, text='Masukan Nama:')
# # .pack()
# label.pack(pady=10)
# # entry
# entry = tk.Entry(root)
# entry.pack(pady=10)
# # button
# button = tk.Button(root, text='Kirim', command=on_click)
# button.pack(pady=10)

# label2 = tk.Label(root, text='')
# label2.pack(pady=10)
# root.mainloop()


# tugas penjumlahan --------------
# def jumlah1():
#     angka1 = float(entry1.get())
#     angka2 = float(entry2.get())
#     jumlah = angka1+angka2
#     kirim.config(text=f'Hasilnya: {jumlah}')

# ini membuat kalkulator
# root = tk.Tk()   #screenName='Kalkulator'    menamai display yg kita buat
# root.title('Calculator Penjumlahan')
# root.geometry('500x200')

# angka1 = tk.Label(root, text='Angka 1: ')
# angka1.place(x=50,y=20) #x itu lebar kekanan. y itu vertikal kebawah

# entry1 = tk.Entry(root)
# entry1.place(x=120,y=20)

# # ----------------
# angka2 = tk.Label(root, text='Angka 2: ')
# angka2.place(x=50,y=60)

# entry2 = tk.Entry(root)
# entry2.place(x=120,y=60)


# button3 = tk.Button(root, text='Kirim',command=jumlah1)
# button3.place(x=50,y=100)

# kirim = tk.Label(root,text='')
# kirim.place(x=50,y=120)

# root.mainloop()












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