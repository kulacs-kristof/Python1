import math
a = int(input("a = "))
b = int(input("b = "))
if a > b:
    print(math.factorial(a)/math.factorial(b))
else:
    print(math.factorial(b)/math.factorial(a))