#from numpy import *
f = open("species.txt")
print("step CO2 H2O H2 CO C2H4 H2O2 C3H6")
for line in f:
    word = line.split()
    line =next(f)
    number = line.split()
    try:
        n1= number[(word.index("CO2")-1)]
    except ValueError:
        n1=0
    try:
        n2= number[(word.index("H2O")-1)]
    except ValueError:
        n2=0
    try:
        n3= number[(word.index("H2")-1)]
    except ValueError:
        n3=0
    try:
        n4= number[(word.index("CO")-1)]
    except ValueError:
        n4=0
    try:
        n5= number[(word.index("C2H4")-1)]
    except ValueError:
        n5=0
    try:
        n6= number[(word.index("H2O2")-1)]
    except ValueError:
        n6=0
    try:
        n7= number[(word.index("C3H6")-1)]
    except ValueError:
        n7=0
    print int(number[0])/round(10000,5),n1,n2,n3,n4,n5,n6,n7
f.close()

