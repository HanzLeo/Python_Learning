from math import factorial as f

m = int(input("m = "))
n = int(input("n = "))
print(f(m) // f(n) // f(m - n))
