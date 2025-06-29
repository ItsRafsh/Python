
def pembelian(hargaProduk,pesanan):
    for produk in hargaProduk:
        kuantitas = int(input(f"berapa banyak {produk} yg mau di beli: "))
        if kuantitas > 0:
            pesanan[produk] = kuantitas

def menghitungTotalBiayapesanan(hargaProduk,pesanan):
    totalpesananBiaya = 0
    for produk,kuantitas in pesanan.items():
        totalpesananBiaya += hargaProduk[produk] * kuantitas
    return totalpesananBiaya

def displaypesanan(pesanan,kategoryNama,totalpesananBiaya):
    print(f"\npesanan: {kategoryNama}")
    if pesanan :
        for produk,kuantitas in pesanan.items():
            print(f"{kuantitas} X {produk}")
        print(f"total {kategoryNama} biaya: Rp{totalpesananBiaya:,}")
    else:
        print(f"total {kategoryNama} pesanan kosong")

def menghitungTotalBiaya(totalBiayaMakanan,totalBiayaMinuman):
    return totalBiayaMakanan + totalBiayaMinuman 

def main():
    print("----------Selamat datang----------")
    biayaMakanan = {
        'ayamRica':17000,
        'rendang':15000,
        'kerupuk':1000
    } #menu tambah sendiri
    biayaMinuman = {
        'marjan':3000,
        'teh anget':5000,
        'abc leci': 3000
    }

    print('Menu Makanan')
    for manakan,harga in biayaMakanan.items():
        print(f'{manakan:<15}: Rp{harga}')

    print('\nMenu Minuman')
    for minuman,harga in biayaMinuman.items():
        print(f'{minuman:<15} : Rp{harga}')
    print('\nSilahkan pesan')

    pesananMakanan = {}
    pesananMinuman = {}
    try:
        pembelian(biayaMakanan,pesananMakanan)
        totalBiayaMakanan = menghitungTotalBiayapesanan(biayaMakanan,pesananMakanan)
        pembelian(biayaMinuman,pesananMinuman)
        totalBiayaMinuman = menghitungTotalBiayapesanan(biayaMinuman,pesananMinuman)

        displaypesanan(pesananMakanan,"Makanan",totalBiayaMakanan)
        displaypesanan(pesananMinuman,"Minuman",totalBiayaMinuman)
        totalBiaya = menghitungTotalBiaya(totalBiayaMakanan,totalBiayaMinuman)

        if totalBiaya > 0:
            print(f"\nTotal biaya Rp{totalBiaya:,}")
        else:
            print("Kamua gada beli")

    except:
        print('Anda tidak jadi pesan diwarteg kami')

if __name__ == "__main__":
    main()