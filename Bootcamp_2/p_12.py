

# pertemuan 12

# cara memanggil diluar folder. fungsi r itu row
def tulis(nama):
    with open(nama,'a') as file:
        file.write('woii cutyy')
tulis(r'contoh.txt')



with open(r'contoh.txt','a') as file:
    file.write("""
Yth. Ranaon
kamu teh kumaha uey
sala mencari
""")



with open(r'game.txt','r+') as file:
    isi = file.readlines()
    print(f'pemain sebelumnya: {isi[0]}',end='')
    print(f'jumlah percobaan: {isi[1]}')

    nama = input('masukin naamlu: ')
    jumlaNyoba = 0
    angka = 10
    benar = False
    while not benar:
        tebak = int(input('masukan tebakanmu: '))
        jumlaNyoba = jumlaNyoba + 1
        if tebak > angka :
            print('tebakan mu lebih besar')
        elif tebak < angka:
            print('tebakan mu lebih kecil')
        else:
            print('bener brooo')
            benar = True
file = open(r'game.txt','r+')
file.write(f"{nama} \n{jumlaNyoba}")
file.close()


