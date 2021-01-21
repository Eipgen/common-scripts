import itertools as its 
words = "0123"
r = its.product(words,repeat=3)
dic = open("pass.txt","a")
for i in r:
	dic.write("".join(i))
dic.close()