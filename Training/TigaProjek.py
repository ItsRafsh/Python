import os
os.system('cls')


# ------------------------------------------
# Random password Generaor
import random
import string

# char = string.ascii_letters + string.digits + string.punctuation

# length = int(input('Enter required length: '))
# random_passwrd = ''.join(random.choice(char) for i in range(length))

# print(f"The random password is : {random_passwrd}")








# ------------------------------------------
# BMI CALCULATOR    Body Mass Index, untuk menentukan bb yg sehat

weight = float(input('Enter your weight in kilogram (kg): '))
height = float(input('Enter your height in meters (m): '))

BMI_result = weight / (height ** 2)
print('-'*30)
print(f'Your BMI is: {BMI_result:.2f}')
print('-'*30)












# ------------------------------------------
#  Acronym.   Membuat singkata dari huruf depan
phrase = input('Enter a phrase: ')

words = phrase.split()
acronym = ''.join([word[0].upper() for word in words])

print(f'The Acronym is: {acronym}')