with open("dodecane.reaction") as f:
    with open("dodecane.producation") as g:
        new = []
        new2 = []
        for line in f:
            nline = str(line.split()[0])
            sline = line.split()[1].split("->")
            sline.insert(0,nline)
            new.append(sline)
        for line2 in g:
            nline2 = str(line2.split()[0])
            sline2 = line2.split()[1].split("->")
            sline2.insert(0,nline2)
            new2.append(sline2)
        for reaction in new:
            for reaction2 in new2:
                if reaction[2] == reaction2[1]:
                    reaction[0] = int(reaction[0]) - int(reaction2[0])
            print(str(reaction[0])+" "+str(reaction[1])+"->"+str(reaction[2]))
            #print(str(reaction2[0])+" "+str(reaction2[1])+"->"+str(reaction2[2]))
            
#else:
                    #print(str(reaction[0]))
                        #+" "+reaction[1]+"->"+reaction[2]))
                    #else:
                     #   print(str(reaction[0]+" "+reaction[1]+"->"+reaction[2]))
                 
                
                #if reaction[1] == "[H]C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])[H]":
            #print(reaction)''
