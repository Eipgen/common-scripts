with open("bonds.reaxc.reaction") as f:
    new = []
    for line in f:
        nline = str(line.split()[0])
        sline = line.split()[1].split("->")
        sline.insert(0,nline)
        new.append(sline)
    for reaction in new:
        if reaction[2] == "[H]C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])[H]":
            print(str(reaction[0]+" "+reaction[1]+"->"+reaction[2]))
