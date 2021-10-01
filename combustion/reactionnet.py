import os
import numpy as np
def sortindex(ele):
    return ele[1]
def checksim(L):
    T=[ele[1] for ele in L]
    def get_index(L):
        E=[]
        for i in L:
            d=[j for j,v in enumerate(L) if v==i]
            t=[i,d]
            E.append(t)
        return E
    return get_index(T)

def netreaction(F):
    with open(F) as P:
        R=[]
        for line in P:
            mline=[]
            nline=line.split()
            mline.append(nline[0])
            oline=[]
            rea=nline[1].split("->")[0].split("+")
            pro=nline[1].split("->")[1].split("+")
            oline.append(rea)
            oline.append(pro)
            tot=rea+pro
            tot.sort()
            #oline.append(tot)
            mline.append(tot)
            mline.append(oline)
            R.append(mline)
        R.sort(key=sortindex)
        return R
#T=checksim(netreaction("./traj_03.reactionabcd"))
T=netreaction("./traj_03.reactionabcd")

for i in T:
    print(i)

