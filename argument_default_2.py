# apabila terdapat lebih dari 1 argument default, maka kita bisa mengakses beberapa argument dgn menyertakan 
# nama argument ketika memanggilnya
def fungsi(a, b=5, c=10): 
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)

fungsi(3, 7)
fungsi(25, c=24)
fungsi(c=50, a=100)