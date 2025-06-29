import tkinter as tk

calculation = ''

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)

def calculate():
    global calculation
    try:
        result = str(eval(calculation))
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, result)
    except:
        clear()
        text_result.insert(1.0, 'Eror')

def clear():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')


def parenthesis_click():
    global calculation
    open_count = calculation.count('(')
    close_count = calculation.count(')')
    
    if open_count > close_count:
        calculation += ')'
    else:
        calculation += '('
    
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)


root = tk.Tk()
root.geometry('300x520')
root.config()

# text resultnya
text_result = tk.Text(root, height=2, width=16, font=('Arial', 24))
text_result.grid(columnspan=5, pady=10)

# tombol tombolnya
tombol_c = tk.Button(root, text='C', command=clear, width=5, height=3, font=('Arial', 14), bg='#ff9d00', fg='#ffffff', activebackground='#ffc400')
tombol_c.grid(row=2, column=1)

tombol_parenthesis = tk.Button(root, text='()', command=parenthesis_click, width=5, height=3,font=('Arial', 14), bg='#ff0000', fg='#ffffff', activebackground='#ff8080')
tombol_parenthesis.grid(row=2, column=2)

tombol_pangkat = tk.Button(root, text='^', command=lambda: add_to_calculation('**'), width=5, height=3, font=('Arial', 14), bg='#ff0000', fg='#ffffff', activebackground='#ff8080')
tombol_pangkat.grid(row=2, column=3)

tombol_div = tk.Button(root, text='/', command=lambda: add_to_calculation('/'), width=5,height=3, font=('Arial', 14), bg='#ff0000', fg='#ffffff', activebackground='#ff8080')
tombol_div.grid(row=2, column=4)

tombol1 = tk.Button(root, text='1', command=lambda: add_to_calculation(1), width=5,height=3, font=('Arial', 14))
tombol1.grid(row=3, column=1)

tombol2 = tk.Button(root, text='2', command=lambda: add_to_calculation(2), width=5, height=3,font=('Arial', 14))
tombol2.grid(row=3, column=2)

tombol3 = tk.Button(root, text='3', command=lambda: add_to_calculation(3), width=5,height=3, font=('Arial', 14))
tombol3.grid(row=3, column=3)

tombol_mul = tk.Button(root, text='x', command=lambda: add_to_calculation('*'), width=5, height=3,font=('Arial', 14), bg='#ff0000', fg='#ffffff', activebackground='#ff8080')
tombol_mul.grid(row=3, column=4)

tombol4 = tk.Button(root, text='4', command=lambda: add_to_calculation(4), width=5,height=3, font=('Arial', 14))
tombol4.grid(row=4, column=1)

tombol5 = tk.Button(root, text='5', command=lambda: add_to_calculation(5), width=5,height=3, font=('Arial', 14))
tombol5.grid(row=4, column=2)

tombol6 = tk.Button(root, text='6', command=lambda: add_to_calculation(6), width=5,height=3, font=('Arial', 14))
tombol6.grid(row=4, column=3)

tombol_min = tk.Button(root, text='-', command=lambda: add_to_calculation('-'), width=5,height=3, font=('Arial', 14), bg='#ff0000', fg='#ffffff', activebackground='#ff8080')
tombol_min.grid(row=4, column=4)

tombol7 = tk.Button(root, text='7', command=lambda: add_to_calculation(7), width=5,height=3, font=('Arial', 14))
tombol7.grid(row=5, column=1)

tombol8 = tk.Button(root, text='8', command=lambda: add_to_calculation(8), width=5,height=3, font=('Arial', 14))
tombol8.grid(row=5, column=2)

tombol9 = tk.Button(root, text='9', command=lambda: add_to_calculation(9), width=5,height=3, font=('Arial', 14))
tombol9.grid(row=5, column=3)

tombol_plus = tk.Button(root, text='+', command=lambda: add_to_calculation('+'), width=5,height=3, font=('Arial', 14), bg='#ff0000', fg='#ffffff', activebackground='#ff8080')
tombol_plus.grid(row=5, column=4)

tombol0 = tk.Button(root, text='0', command=lambda: add_to_calculation(0), width=5,height=3, font=('Arial', 14))
tombol0.grid(row=6, column=1)

tombol_titik = tk.Button(root, text='.', command=lambda: add_to_calculation('.'), width=5,height=3, font=('Arial', 14), fg='#ff0000')
tombol_titik.grid(row=6, column=2)

tombol_equal = tk.Button(root, text='=', command=calculate, width=12,height=3, font=('Arial', 14), bg='#ff9d00', fg='#ffffff', activebackground='#ffc400')
tombol_equal.grid(row=6, column=3, columnspan=2)

root.mainloop()
