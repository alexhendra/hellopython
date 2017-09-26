# Tuple mirip seperti list, hanya saja nilainya tidak dpt dirubah
# contoh penulisan tuple
tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

print(tup3)

# tuple empty
tupEmpty = ();

# untuk membuat tuple yg hanya memiliki 1 nilai saja, harus ada koma setelah item
tupOne = (50,)
print("tupOne: ", tupOne)
print(type(tupOne))

tupA = (12, 34.56)
tupB = ('abc', 'xyz')
print()

# Aksi seperti dibawah ini tidak bisa dilakukan pada tuple python
# Karena memang nilai pada tuple python tidak bisa diubah
# tupB[0] = 100;
# print(tupB)

# Jadi, buatlah tuple baru sebagai berikut
tupC = tupA + tupB
print (tupC)
del tupC;
# akan error ketika diprint karena tupC sudah dihapus
# print("Setelah dihapus tupC:", tupC)