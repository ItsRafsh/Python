
# pertemuan 13
import math
print(math.sqrt(25))                #selalu akar pangkat 2
hasil = math.sin(math.radians(72))
print(f"{hasil:.2f}")

import module as m
m.sapa('rafa')

import random
# def ini masukin ke module.py
def pwGenerator():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    digit = '0123456789'
    symbol = '{:"<>?|+_)(~!@#$%^&*)}'

    all_char = lower + upper + digit +symbol
    # pw = "".join(random.sample(all_char,8))
    # print(pw)

    length = random.randint(8,16)
    password = random.choices(all_char, k=length)
    hasil = ''.join(password)
    # return hasil
    print(hasil)

pwGenerator()

