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











# pertemuan 7

# print('calculator bangun datar dan bangun ruang')
# print("""pilih kategori :
# 1. bangun datar
# 2. bangun ruang""")
# pilihan = int(input("silahkan pilih: "))

# if pilihan == 1:
#     print('\n--- silahkan pilih bangun datar ---')
#     print('1.persegi\n2.persegi panjang\n3.segitiga\n4.jajar genjang')
#     print('5.lingkaran\n6.trapesium\n7.belah ketupat\n8.layang-layang')
#     milih = int(input('pilih 1-8: '))

#     if milih == 1:
#         S = float(input('masukan sisi: '))
#         print(f"hasilnya: {S * S}")

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

#     elif milih == 5:
#         r = float(input('masukan r: '))
#         print(f"hasilnya: {3.14 * r**2}")

#     elif milih == 6:
#         sAtas = float(input('masukan sisi atas: '))
#         sBawah = float(input('masukan sisi bawah: '))
#         tinggi = float(input('masukan tinggi: '))
#         print(f"hasilnya: {1/2 * (sAtas + sBawah) * tinggi}")
        
#     elif milih == 7:
#         diagonal_1 = float(input('masukan diagonal 1: '))
#         diagonal_2 = float(input('masukan diagonal 2: '))
#         print(f'hasilnya belah ketupat: {1/2 * diagonal_1 * diagonal_2}')

#     elif milih == 8:
#         diagonal_1 = float(input('masukan diagonal 1: '))
#         diagonal_2 = float(input('masukan diagonal 2: '))
#         print(f'hasilnya layang-layang: {1/2 * diagonal_1 * diagonal_2}')
    
#     else:
#         print("pilihanyya cuma 1 sampai 8 broo")


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

# else:        
#     print("pilihanyya cuma 1 dan 2 broo. masukan yg bener lah")











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

















# pertemuan 9
# ini membuat perkalian anak TK 1-10 
# for i in range(1,11):
#     for x in range(1,11):
#         hasil = i*x
#         print(f'{i} x {x} = {hasil} \n',end='')
#     print()



    # a = [[1,2],
    #     [3,4]]

    # b = [[4,3],
    #     [2,1]]

    # hasil = [[0,0],
    #         [0,0]]

# for baris in range(len(a)):
#     for kolom in range(len(a[0])):
#         hasil[baris][kolom] = a[baris][kolom] - b[baris][kolom]
#         print(hasil[baris][kolom],end=' ')
#     print()



# for i in range(len(a[0])):
#     for j in range(len(b)):
#         for k in range(len(b[0])):
#             hasil[i][j] += a[i][k] * b[k][j]











# pertemuan 10

# def bola(r):
#     pi = 3.14
#     hasil = 4/3*pi*r**3
#     print(f'hasilnya: {hasil}')
# bola(5)


# def persegi(S):
#     return f"hasilnya: {S * S}"
# def persegiPanjang(p,l):
#     return f"Hasilnya: {p*l}"
# def segitiga(alas,tinggi):
#     return f"hasilnya: {1/2*alas*tinggi}"
# def jajarGenjang():
#     return f"hasilnya: {alas*tinggi}"
# def lingkaran(r):
#     return f"hasilnya: {3.14 * r**2}"
# def trapesium(a,b,i):
#     return f"hasilnya: {1/2 * (a + b) * i}"
# def ketupatLayang(d1,d2):
#     return f'hasilnya belah ketupat: {1/2 * d1 * d2}'



# print('calculator bangun datar dan bangun ruang')
# print("""pilih kategori :
# 1. bangun datar
# 2. bangun ruang""")
# pilihan = int(input("silahkan pilih: "))

# if pilihan == 1:
#     print('\n--- silahkan pilih bangun datar ---')
#     print('1.persegi\n2.persegi panjang\n3.segitiga\n4.jajar genjang')
#     print('5.lingkaran\n6.trapesium\n7.belah ketupat\n8.layang-layang')
#     milih = int(input('pilih 1-8: '))

#     if milih == 1:
#         S = float(input('masukan sisi: '))
#         print(persegi(S))

#     elif milih == 2:
#         panjang = float(input('masukan panjang: '))
#         lebar = float(input('masukan lebar: '))
#         print(persegiPanjang(panjang,lebar))

#     elif milih == 3:
#         alas = float(input('masukan alas: '))
#         tinggi = float(input('masukan tinggi: '))
#         print(segitiga(alas,tinggi))
        
#     elif milih == 4:
#         alas = float(input('masukan alas: '))
#         tinggi = float(input('masukan tinggi: '))
#         print(jajarGenjang(alas,tinggi))

#     elif milih == 5:
#         r = float(input('masukan r: '))
#         print(lingkaran(r))

#     elif milih == 6:
#         sAtas = float(input('masukan sisi atas: '))
#         sBawah = float(input('masukan sisi bawah: '))
#         tinggi = float(input('masukan tinggi: '))
#         print(trapesium(sAtas,sBawah,tinggi))
        
#     elif milih == 7:
#         diagonal_1 = float(input('masukan diagonal 1: '))
#         diagonal_2 = float(input('masukan diagonal 2: '))
#         print(ketupatLayang(diagonal_1,diagonal_2))

#     elif milih == 8:
#         diagonal_1 = float(input('masukan diagonal 1: '))
#         diagonal_2 = float(input('masukan diagonal 2: '))
#         print(ketupatLayang(diagonal_1,diagonal_2))
    
#     else:
#         print("pilihanyya cuma 1 sampai 8 broo")


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

# else:        
#     print("pilihanyya cuma 1 dan 2 broo. masukan yg bener lah")











