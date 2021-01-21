f = open("data.decane20",encoding="utf-8")
lines = f.readlines()
del lines[0]
del lines[1:10]
del lines[4:19]
lines.insert(4,"0.0 0.0 0.0")
for line in lines:
    line=line.strip()
    print(line)
f.close()
