inventory = {}
def add_stock():
    item_name = input("masukan nama : ").lower()
    kualitas = int(input("Masukan kualitas : "))
    inventory[item_name] = kualitas
    print("Inventory sudah di update.")

def lihat_stok():
    if inventory:
        print("inventory saat ini : ")
        for item_name, kualitas in inventory.items():
            print(f"{item_name.upper()}: kualitas = {kualitas}")
    else:
        print("inventory is empty")

def hapus_stok():
    item_name = input("enter item name to delete : ").lower()
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name.upper()} remove from inventory.")
    else:
        print(f"{item_name.upper()} not found in inventory")

def main():
    while True:
        print("-"*30)
        print("Stock Management System")
        print("1. Add stock")
        print("2. View Stock")
        print("3. Remove stock")
        print("4. Exit")

        pilihan = input("select 1 2 3 4 : ")
        print("-"*30)

        if pilihan == "1":
            add_stock()
        elif pilihan == "2":
            lihat_stok()
        elif pilihan == "3":
            hapus_stok()
        elif pilihan == "4":
            next = input("stop kah (y/n) : ")
            if next == "y":
                print("sudah selesai kau")
                break
        else:
            print("Input yg bener lah")

if __name__ == "__main__":
    main()
