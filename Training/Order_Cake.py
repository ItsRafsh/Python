import os
os.system('cls')
import time

cake_menu = {
    'kue coklat': 5000,
    'kue vanila': 5000,
    'kue stoberi': 6000,
    'kue pukis': 1000,
    'kue donat': 3000,
}
def display_menu():
    print('available cake:')
    for cake, price in cake_menu.items():
        print(f'- {cake.title():<15}: Rp.{price:,}')

def order_cake():
    choice = input('enter the cake name: ').lower()

    if choice in cake_menu:
        quantity = int(input('enter the quantity: '))
        total_price = cake_menu[choice] * quantity
        print(f'you ordered {quantity} X {choice.title()} for a total of Rp.{total_price:,}.')
        simulate_baking()
    else:
        print('sorry, that cake is not available')

def simulate_baking():
    print('baking your cake....')
    time.sleep(4)
    print('decorating your cake')
    time.sleep(2)
    print('your cake is already, enjoy your delicious cake')

def main():
    while True:
        print('-'*30)
        print('1. show cake menu')
        print('2. order a cake')
        print('3. Exit')
        choice = input('Enter your choice 1-3: ')
        print('-'*30)

        if choice == '1':
            display_menu()
        elif choice == '2':
            order_cake()
        elif choice == '3':
            print('thank you for visiting, have a sweet day')
            break
        else:
            print('invalid choice!! please enter a number between 1-3.')

if __name__ == '__main__':
    main()
    

