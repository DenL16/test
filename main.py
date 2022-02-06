def f1(i):
    def f2(k):
        print(i+k)
    return f2
A=f1(10)
print(A(35))