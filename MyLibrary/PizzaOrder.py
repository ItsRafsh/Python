import time
import os
os.system('cls')

pizza_menu = {
    'daging':120000,
    'jamur':100000,
    'mozarela':110000
}

def show_menu():
    print('Pilih Menu Pizza')
    print('-'*30)
    for pizza,harga in pizza_menu.items():
        print(f'{pizza.capitalize():<10}: Rp.{harga:,}')
    print('-'*30)

def pesanan():
    order = {}
    while True:
        pizza = input('pizza apa yang ingin anda pesan (tulis done untuk selesai): ').lower()
        if pizza == 'done':
            break
        elif pizza not in pizza_menu:
            print('pesanan yg anda tulis tidak tersedia di menu')
        else:
            jumlah = int(input(f'Berapa {pizza.capitalize()} yg ingin anda pesan: '))
            order[pizza] = jumlah
    return order

def hitungPesanan(pesan):
    total = 0
    for pizza,jumlah in pesan.items():
        total += pizza_menu[pizza] * jumlah
    return total

def simulasiPesanan():
    print('your order is being prevered and delivered')
    time.sleep(3)
    print('yor pizza has arrived. nikamtilah')



def main():
    show_menu()
    order = pesanan()
    if not order:
        print('no order placed, keluar lah')
        return
    
    total = hitungPesanan(order)
    print('-'*30)
    print('Order Summary')
    for pizza,jumlah in order.items():
        print(f'{pizza.capitalize()}: {jumlah} x Rp.{pizza_menu[pizza]:,}')
    print(f'total: {total:,}')
    print('-'*30)

    proses = input('apakah pizza nya ingin di proses? (ya/no): ').lower()
    if proses == 'ya':
        simulasiPesanan()
    else:
        print('order di cancel. semoga harimu menyenangkan')

if __name__ == "__main__":
    main()

