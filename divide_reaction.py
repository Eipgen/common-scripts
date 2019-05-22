from collections import Counter
import re
with open("bonds.reaxc.reaction") as f:
    new=[]
    for line in f:
        nline=str(line.split()[0])
        sline=line.split()[1].split("->")
        sline.insert(0,nline)
        new.append(sline)
    reactions=sorted(new,key=lambda x:x[1], reverse=True)
    for reaction in reactions:
        print(str(reaction[0]+" "+reaction[1]+"->"+reaction[2]))

def convertsvg = (cls,smiles):

        


        


        
