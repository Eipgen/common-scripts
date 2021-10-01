f = open("decane2200k.txt")
for line in f:
    word = line.split
    line = f.__next__()
    number = line.split()
    try:
        no1=number[word.index("C12H26")-1]
    except ValueError:
        no1=0
    print(int(number[0])/10000,no1)
f.close()
