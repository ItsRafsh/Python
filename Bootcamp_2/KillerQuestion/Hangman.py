import random
import os
import bahan
os.system('cls')



print(bahan.title)
print('''Aturan permainan:
1. Selamatkan Budi dengan cara menjawab 1 pertanyaan dengan benar!
2. Budi hanya memiliki 6 kesempatan
3. 1 kesalahan akan mengurangi nyawa Budi!
''')

siap = input("kamu siap / tidak: ")
if siap == "siap".lower():
    pertanyaan = open("KillerQuestion\pertanyaan.txt",'r')
    list_pertanyaan = pertanyaan.readlines()

    jawaban = open("KillerQuestion\jawaban.txt",'r')
    list_jawaban = jawaban.readlines()

    for i in range(0,6):
        print(bahan.hangman[i])

        choose = random.randint(0, 100)
        print(f'pertanyaan: {list_pertanyaan[choose]}',end='')
        user_jawab = input("Jawabanmu: ").strip().lower()

        if user_jawab == (list_jawaban[choose]).strip().lower():
            print(bahan.congrats)
            print("jawaban mu benar")
            break

        elif i == 5:
            print(bahan.rose)
            print('kamu gagal')

    pertanyaan.close()
    jawaban.close()

else:
    print(bahan.hangman[5])
    print('Kamu tidak siap maka Budi sudah tidak ada di dunia ini\nmakasih dah main')