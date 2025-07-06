from math import factorial

m = int(input("m = "))
n = int(input("n = "))
print(factorial(m) // factorial(n) // factorial(m - n))
