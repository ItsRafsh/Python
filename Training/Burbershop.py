import os
os.system('cls')
import time

haircut_menu = {
    'buzz cut': 18000,
    'fade': 15000,
    'undercut': 20000,
    'pompadour': 25000
}

def display():
    print('Available Haircuts')
    for style, price in haircut_menu.items():
        print(f'- {style.title():<15}:Rp{price:,}')

def choice_haircut():
    choice = input('Enter your haircut choice: ').lower()

    if choice in haircut_menu:
        print(f'your choice {choice.title()} for Rp.{haircut_menu[choice]:,}')
        simulate_haircut()
    else:
        print('sorry, that haircut is not available')

def simulate_haircut():
    print('the barber is getting ready')
    time.sleep(3)
    print('starting your haircut')
    time.sleep(2)
    print('your haircut is done! Loking cool!')


def main():
    while True:
        print('-'*30)
        print('1. show a haicuts menu')
        print('2. get a haircuts')
        print('3. Exit')

        choice = input('enter your choice 1-3: ')
        print('-'*30)

        if choice == '1':
            display()
        elif choice == '2':
            choice_haircut()
        elif choice == '3':
            print('thank you for visiting! have a great day')
            break
        else:
            print('invalid choice. please choice a valid option')

if __name__ == "__main__":
    main()
