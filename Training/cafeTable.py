

# project membuat booking meja cafe menggunakan dictionary

import os
os.system('cls')
tables = {
    'window table': 'Available',
    'corner table': 'Available',
    'garden table': 'Available',
    'family table': 'Available',
}

def display():
    print('Table Status')
    for table_name,status in tables.items():
        print(f'{table_name.title()}: {status}')

def book_table():
    table_name = input('enter the name of the table you wanna book: ')
    if table_name in tables:
        if tables[table_name] == 'Available':
            tables[table_name] = 'Booked'
            print(f'{table_name.title()} successfully booked')
        else:
            print(f'{table_name.title()} is alredy booked')
    else:
        print('sorry, we dont have this table')

def cancel_booking():
    table_name = input('enter the name of the table you want to cancel: ').lower()
    if table_name in tables:
        if tables[table_name] == 'Booked':
            tables[table_name] = 'Available'
            print(f'Booking for {table_name.title()} has been canceled')
        else:
            print(f'{table_name.title()} is not booked')
    else:
        print('sorry, we dont have this table')

def main():
    while True:
        print('-'*30)
        print('1. view availabe table')
        print('2. book a table')
        print('3. cancel a booking')
        print('4. exit')

        choice = int(input('enter your choice: '))
        if choice == 1:
            display()
        elif choice == 2:
            book_table()
        elif choice == 3:
            cancel_booking()
        elif choice == 4:
            print('Thank you for using the cafe table reservation system. goodbye'.title())
            break
        else:
            print('invalid choice. choice a valid option')

if __name__ == "__main__":
    main()

