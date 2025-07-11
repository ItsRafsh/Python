
# pertemuan 7

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
        print(f"hasilnya: {S * S}")

    elif milih == 2:
        panjang = float(input('masukan panjang: '))
        lebar = float(input('masukan lebar: '))
        print(f"hasilnya: {panjang * lebar}")

    elif milih == 3:
        alas = float(input('masukan alas: '))
        tinggi = float(input('masukan tinggi: '))
        print(f"hasilnya: {1/2*alas*tinggi}")
        
    elif milih == 4:
        alas = float(input('masukan alas: '))
        tinggi = float(input('masukan tinggi: '))
        print(f"hasilnya: {alas*tinggi}")

    elif milih == 5:
        r = float(input('masukan r: '))
        print(f"hasilnya: {3.14 * r**2}")

    elif milih == 6:
        sAtas = float(input('masukan sisi atas: '))
        sBawah = float(input('masukan sisi bawah: '))
        tinggi = float(input('masukan tinggi: '))
        print(f"hasilnya: {1/2 * (sAtas + sBawah) * tinggi}")
        
    elif milih == 7:
        diagonal_1 = float(input('masukan diagonal 1: '))
        diagonal_2 = float(input('masukan diagonal 2: '))
        print(f'hasilnya belah ketupat: {1/2 * diagonal_1 * diagonal_2}')

    elif milih == 8:
        diagonal_1 = float(input('masukan diagonal 1: '))
        diagonal_2 = float(input('masukan diagonal 2: '))
        print(f'hasilnya layang-layang: {1/2 * diagonal_1 * diagonal_2}')
    
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



