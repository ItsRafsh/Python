'''
create sebuah permainan dengan cuma tekan enter dan bisa
mendapatkan hadiah doolprize.
seperti itu lah simple nya
'''



import random

def mystery_box():
    bahan_hadiah = ['laptop ORG','Liburan ke Paser','Tiket pesawat','jalan bareng pasangan','NOTHING(HAHAHA)']
    hadiah = random.choice(bahan_hadiah)
    return hadiah

def utama():
    print("Selamat datang di Undian pejabat")
    print("kamu bisa mendapatkan kesempatan untuk membuka 1 kali dan mendapatkan hadiah if you lucky")

    input("press enter if you want lucky prize")
    hadiah = mystery_box()
    if hadiah == 'nothing':
        print("Yahahaa, the prize is empty, try it and spend ur money")
    else:
        print(f"Selamat!! You Have won {hadiah}!!!!!")

if __name__ == "__main__":
    utama()

