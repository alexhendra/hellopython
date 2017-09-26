x = 10
y = 5

def test_print(a):
    # keyword 'global' digunakan untuk memakai variable yang ada di luar fungsi
    global x
    x=a
    print('Nilai x : %i' % x)

test_print(8)