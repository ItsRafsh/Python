# # PERTEMUAN 6
# # PROJECT KASIR BARANG BELANJAAN



# versi menghapus dengan menulis nomor barang belanja nya

# Program sederhana untuk mengelola daftar belanja menggunakan while, for, if, elif (tanpa try)

daftar_belanja = []

while True:
    print("\nMenu Daftar Belanja:")
    print("1. Lihat Daftar Belanja")
    print("2. Tambahkan Item ke Daftar")
    print("3. Hapus Item dari Daftar")
    print("4. Keluar")
    
    pilihan = input("\nPilih opsi (1/2/3/4): ")

    if pilihan == '1':  # Melihat daftar belanja
        if len(daftar_belanja) == 0:
            print("\nDaftar belanja Anda kosong.")
        else:
            print("\nDaftar Belanja Anda:")
            for i in range(len(daftar_belanja)):
                print(f"{i+1}. {daftar_belanja[i]}")
    
    elif pilihan == '2':  # Menambahkan item ke daftar
        item = input("\nMasukkan nama item yang ingin ditambahkan: ")
        daftar_belanja.append(item)
        print(f"'{item}' telah ditambahkan ke daftar belanja.")
    
    elif pilihan == '3':  # Menghapus item dari daftar
        if len(daftar_belanja) == 0:
            print("\nDaftar belanja kosong, tidak ada yang bisa dihapus.")
        else:
            print("\nDaftar Belanja Anda:")
            for i in range(len(daftar_belanja)):
                print(f"{i+1}. {daftar_belanja[i]}")
            
            nomor_item = input("\nMasukkan nomor item yang ingin dihapus: ")
            
            if nomor_item.isdigit():  # Cek apakah input berupa angka
                nomor_item = int(nomor_item)
                if 1 <= nomor_item <= len(daftar_belanja):
                    item_dihapus = daftar_belanja.pop(nomor_item - 1)
                    print(f"'{item_dihapus}' telah dihapus dari daftar belanja.")
                else:
                    print("Nomor item tidak valid apapun.")
            else:
                print("Input tidak valid. Harap masukkan nomor yang benar.")
    
    elif pilihan == '4':  # Keluar dari program
        print("\nTerima kasih! Selamat belanja!")
        break
    
    else:  # Jika pilihan tidak valid
        print("Pilihan tidak valid. Silakan coba lagi.")





















# # versi menghapus dengan menulis nama barang belanja nya
# # Program sederhana untuk mengelola daftar belanja menggunakan while, for, if, elif (tanpa try)


# daftar_belanja = []
    
# while True:
#     print("\nMenu Daftar Belanja:")
#     print("1. Lihat Daftar Belanja")
#     print("2. Tambahkan Item ke Daftar")
#     print("3. Hapus Item dari Daftar")
#     print("4. Keluar")
    
#     pilihan = input("\nPilih opsi (1/2/3/4): ")

#     if pilihan == '1':  # Melihat daftar belanja
#         if len(daftar_belanja) == 0:
#             print("\nDaftar belanja Anda kosong.")
#         else:
#             print("\nDaftar Belanja Anda:")
#             for i in range(len(daftar_belanja)):
#                 print(f"{i+1}. {daftar_belanja[i]}")
    
#     elif pilihan == '2':  # Menambahkan item ke daftar
#         item = input("\nMasukkan nama item yang ingin ditambahkan: ")
#         daftar_belanja.append(item)
#         print(f"'{item}' telah ditambahkan ke daftar belanja.")
    
#     elif pilihan == '3':  # Menghapus item dari daftar
#         if len(daftar_belanja) == 0:
#             print("\nDaftar belanja kosong, tidak ada yang bisa dihapus.")
#         else:
#             print("\nDaftar Belanja Anda:")
#             for i in range(len(daftar_belanja)):
#                 print(f"{i+1}. {daftar_belanja[i]}")
            
#             nama_item = input("\nMasukkan nama item yang ingin dihapus: ")
#             if nama_item in daftar_belanja:
#                 daftar_belanja.remove(nama_item)
#                 print(f"'{nama_item}' telah dihapus dari daftar belanja.")

#             # if nomor_item:  # Cek apakah input berupa angka
#             #     nama_item in daftar_belanja
#             #     if 1 <= nomor_item <= len(daftar_belanja):
#             #         item_dihapus = daftar_belanja.remove(nomor_item - 1)

#             else:
#                 print("Input tidak valid. Harap masukkan nama yang benar.")
    
#     elif pilihan == '4':  # Keluar dari program
#         print("\nTerima kasih! Selamat belanja!")
#         break
    
#     else:  # Jika pilihan tidak valid
#         print("Pilihan tidak valid. Silakan coba lagi.")




























