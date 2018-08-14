n = float(input("the match in box: "))
k = float(input("the rest match in right box when left is empty: "))
if n < k:
    print("False")
#the loop
import math
a = 2*n-k  
b = n-k
d = 1
e = math.pow(0.5, a)
while True:
    if a > n and b >=1:
        c = a/b
        d = d*c
        a = a-1
        b = b-1
    else:
        print(d*e)
        break
    




