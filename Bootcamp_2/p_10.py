


# pertemuan 10

# def bola(r):
#     pi = 3.14
#     hasil = 4/3*pi*r**3
#     print(f'hasilnya: {hasil}')
# bola(5)


def persegi(S):
    return f"hasilnya: {S * S}"
def persegiPanjang(p,l):
    return f"Hasilnya: {p*l}"
def segitiga(alas,tinggi):
    return f"hasilnya: {1/2*alas*tinggi}"
def jajarGenjang():
    return f"hasilnya: {alas*tinggi}"
def lingkaran(r):
    return f"hasilnya: {3.14 * r**2}"
def trapesium(a,b,i):
    return f"hasilnya: {1/2 * (a + b) * i}"
def ketupatLayang(d1,d2):
    return f'hasilnya belah ketupat: {1/2 * d1 * d2}'



print('calculator bangun datar dan bangun ruang')
print("""pilih kategori :
1. bangun datar
2. bangun ruang""")
pilihan = int(input("silahkan pilih: "))

if pilihan == 1:
    print('\n--- silahkan pilih bangun datar ---')
    print('1.persegi\n2.persegi panjang\n3.segitiga\n4.jajar genjang')
    print('5.lingkaran\n6.trapesium\n7.belah ketupat\n8.layang-layang')
    milih = int(input('pilih 1-8: '))

    if milih == 1:
        S = float(input('masukan sisi: '))
        print(persegi(S))

    elif milih == 2:
        panjang = float(input('masukan panjang: '))
        lebar = float(input('masukan lebar: '))
        print(persegiPanjang(panjang,lebar))

    elif milih == 3:
        alas = float(input('masukan alas: '))
        tinggi = float(input('masukan tinggi: '))
        print(segitiga(alas,tinggi))
        
    elif milih == 4:
        alas = float(input('masukan alas: '))
        tinggi = float(input('masukan tinggi: '))
        print(jajarGenjang(alas,tinggi))

    elif milih == 5:
        r = float(input('masukan r: '))
        print(lingkaran(r))

    elif milih == 6:
        sAtas = float(input('masukan sisi atas: '))
        sBawah = float(input('masukan sisi bawah: '))
        tinggi = float(input('masukan tinggi: '))
        print(trapesium(sAtas,sBawah,tinggi))
        
    elif milih == 7:
        diagonal_1 = float(input('masukan diagonal 1: '))
        diagonal_2 = float(input('masukan diagonal 2: '))
        print(ketupatLayang(diagonal_1,diagonal_2))

    elif milih == 8:
        diagonal_1 = float(input('masukan diagonal 1: '))
        diagonal_2 = float(input('masukan diagonal 2: '))
        print(ketupatLayang(diagonal_1,diagonal_2))
    
    else:
        print("pilihanyya cuma 1 sampai 8 broo")


elif pilihan == 2:
    print('\n--- silahkan pilih bangun ruang ---')
    print('1.kubus\n2.balok')
    milih_lagi = int(input('pilih 1-2: '))

    if milih_lagi == 1:
        sisi = float(input('masukan sisi: '))
        print(f"hasilnya kubus: {sisi**3}")

    elif milih_lagi == 2:
        panjang = float(input('masukan panjang: '))
        lebar = float(input('masukan lebar: '))
        tinggi = float(input('masukan tinggi: '))
        print(f"hasilnya balok: {panjang * lebar * tinggi}")

    else:
        print("pilihanyya cuma 1 dan 2 broo")

else:        
    print("pilihanyya cuma 1 dan 2 broo. masukan yg bener lah")




