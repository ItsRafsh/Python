

# pertemuan 9
# ini membuat perkalian anak TK 1-10 
for i in range(1,11):
    for x in range(1,11):
        hasil = i*x
        print(f'{i} x {x} = {hasil} \n',end='')
    print()



    a = [[1,2],
        [3,4]]

    b = [[4,3],
        [2,1]]

    hasil = [[0,0],
            [0,0]]

for baris in range(len(a)):
    for kolom in range(len(a[0])):
        hasil[baris][kolom] = a[baris][kolom] - b[baris][kolom]
        print(hasil[baris][kolom],end=' ')
    print()



for i in range(len(a[0])):
    for j in range(len(b)):
        for k in range(len(b[0])):
            hasil[i][j] += a[i][k] * b[k][j]

