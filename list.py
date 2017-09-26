list1 = ['kimia', 'fisika', 1993, 2017]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['kimia', 'fisika', 1993, 2017]
print(list1)
print(list4)

list1 = ['fisika', 'kimia', 1993, 2017]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

print()
print("Nilai list1 sebelum di hapus itemnya: ", list1)
del list1[2]
print("Nilai list1 setelah itemnya di hapus: ", list1)

listGabungan=[1, 2, 3] + [4, 5, 6] # 2 list data diconcatenations
print("listGabungan: ", listGabungan)
print("Total item listGabungan: ", len(listGabungan))
print("Apakah nilai 2 ada di dalam listGabungan? ", 2 in [1, 2, 3])

listRepetition = ['Halo!'] * 4
print("listRepetition: ", listRepetition)
print()
for x in [1,2,3] : print(x,end = ' ') # mem-print dalam sebaris

print()
L = ['C++', 'Java', 'Python']
print("L[-1]: ", L[-1]) # mengambil index 1 dari kanan
print("L[-2]: ", L[-2]) # mengambil index 2 dari kanan
