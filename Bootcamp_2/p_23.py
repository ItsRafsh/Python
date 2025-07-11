

# pertemuan 23
import tkinter as tk

def on_click():
    label2.config(text=f'Halo {entry.get()}')

root = tk.Tk()
root.title('Basic Calculator')
root.geometry('600x200')
# label
label = tk.Label(root, text='Masukan Nama:')
# .pack()
label.pack(pady=10)
# entry
entry = tk.Entry(root)
entry.pack(pady=10)
# button
button = tk.Button(root, text='Kirim', command=on_click)
button.pack(pady=10)

label2 = tk.Label(root, text='')
label2.pack(pady=10)
root.mainloop()


# tugas penjumlahan --------------
def jumlah1():
    angka1 = float(entry1.get())
    angka2 = float(entry2.get())
    jumlah = angka1+angka2
    kirim.config(text=f'Hasilnya: {jumlah}')

# ini membuat kalkulator
root = tk.Tk()   #screenName='Kalkulator'    menamai display yg kita buat
root.title('Calculator Penjumlahan')
root.geometry('500x200')

angka1 = tk.Label(root, text='Angka 1: ')
angka1.place(x=50,y=20) #x itu lebar kekanan. y itu vertikal kebawah

entry1 = tk.Entry(root)
entry1.place(x=120,y=20)

# ----------------
angka2 = tk.Label(root, text='Angka 2: ')
angka2.place(x=50,y=60)

entry2 = tk.Entry(root)
entry2.place(x=120,y=60)


button3 = tk.Button(root, text='Kirim',command=jumlah1)
button3.place(x=50,y=100)

kirim = tk.Label(root,text='')
kirim.place(x=50,y=120)

root.mainloop()

