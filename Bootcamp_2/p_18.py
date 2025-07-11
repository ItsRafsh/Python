# pertemuan 18

import math

class Calculator:
    def __init__(self):
        pass

    def penjumlahan(self,angka1,angka2):
        self.angka1 = angka1
        self.angka2 = angka2
        print(self.angka1 + self.angka2)

    def pengurangan(self,angka1,angka2):
        self.angka1 = angka1
        self.angka2 = angka2
        print(self.angka1 - self.angka2)
        
    def perkalian(self,angka1,angka2):
        self.angka1 = angka1
        self.angka2 = angka2
        print(self.angka1 * self.angka2)

    def pembagian(self,angka1,angka2):
        self.angka1 = angka1
        self.angka2 = angka2
        print(self.angka1 / self.angka2)



class Scientific(Calculator):
    def __init__(self):
        super().__init__()

    def penjumlahan_sin(self,derajat1,derajat2):
        self.radiant1 = math.radians(derajat1)
        self.radiant2 = math.radians(derajat2)
        self.hasil = self.penjumlahan(math.sin(self.radiant1), math.sin(self.radiant2))
        print(f"hasil sin{derajat1} + sin{derajat2} = {self.hasil}")
    
    def penjumlahan_cos(self,derajat1,derajat2):
        self.radiant1 = math.radians(derajat1)
        self.radiant2 = math.radians(derajat2)
        self.hasil = self.penjumlahan(math.cos(self.radiant1), math.cos(self.radiant2))
        print(f"hasil cos{derajat1} + cos{derajat2} = {self.hasil}")

    def penjumlahan_tan(self,derajat1,derajat2):
        self.radiant1 = math.radians(derajat1)
        self.radiant2 = math.radians(derajat2)
        self.hasil = self.penjumlahan(math.tan(self.radiant1), math.tan(self.radiant2))
        print(f"hasil tan{derajat1} + tan{derajat2} = {self.hasil}")

rafa = Scientific()
rafa.penjumlahan_sin(1,2)
