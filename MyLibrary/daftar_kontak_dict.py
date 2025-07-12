# BUATAN SENDIRI
daftar_kontak = {}

while True:
    print("1. tambahkan kontak")
    print("2. menghapus kontak")
    print("3. isi kontak")
    print("4. keluar")
    pilihan = input("masukan 1,2,3,4, : ")

    if pilihan == "1":
        print()
        nim = input("Masukan nim : ")
        if nim in daftar_kontak:
            print("kode nim sudah ada di kontak")
        else:
            nama = input("Masukan nama kontak : ")
            daftar_kontak.update({nim : nama})
            print(f"nim {nim} dan nama {nama} sudah ditambahkan")
            print(f"{"-"*30}\n")


    elif pilihan == "2":
        delete = input("nim yg mau dihapus : ")
        if delete in daftar_kontak:
            nama = daftar_kontak.pop(delete)
            print(f"\nkontak dengan nim {nim} dan nama {nama} SUCCESS dihapus.\n")
        else:
            print("gada di data kontak mu dia")


    elif pilihan == "3":
        print("\n ```````Daftar kontak anda ```````")
        for nim,nama in daftar_kontak.items():
            print(f"nim {nim} : nama {nama}")
        print(f"{"-"*30}\n")


    elif pilihan == "4":
        lanjut = input("lanjutkan (y/n) : ")
        if lanjut == "y":
            break
    
    else:
        print("\n--------- masukan angka yang bener ---------\n")
print("program selesai")








# operasi dictionary

# mahasiswa = {
#     "nama" : "Rafa",
#     "NIM" : "2411102441049",
#     "jurusan" : "Informatika"
# }
# print(mahasiswa.get("nama"))

# mahasiswa.update({"alamat" : "Tanah Grogot"})
# print(mahasiswa)

# mahasiswa.pop("NIM")
# print(mahasiswa)





# fungsi dictionary

# mahasiswa = {
#     "Rafa" : "123456",
#     "Haris" : "123457",
#     "Budin" : "123458"
# }

# print(mahasiswa.keys())
# print(mahasiswa.values())
# print(mahasiswa.items())





