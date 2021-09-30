import numpy as np
import os 
import re
from itertools import groupby
#flist=os.listdir("./reaction")
#flist.sort(key=lambda x:int(x[21:]))
#hlist=flist[0:100]
#print(hlist)
#print(flist)
def convert(L):
    Cum=L.count("C")
    Hum=L.count("H")
    Oum=L.count("O")
    S=[Cum,Hum,Oum]
    M="CHO"
    if S.count(0)==2:
        x=[i for i,a in enumerate(S) if a>0][0]
        if S[x]==1:
            if x==0:
                return "C"
            elif x==1:
                return "H"
            elif x==2:
                return "O"
        elif S[x]>1:
            if x==0:
                return "C"+str(Cum)
            elif x==1:
                return "H"+str(Hum)
            elif x==2:
                return "O"+str(Oum)
    elif S.count(0)==1:
        x=[i for i,a in enumerate(S) if a==0][0]
        if x==0:
            if Hum==1 and Oum==1:
                return "H"+"O"
            elif Hum==1 and Oum>1:
                return "H"+"O"+str(Oum)
            elif Hum>1 and Oum==1:
                return "H"+str(Hum)+"O"
            elif Hum>1 and Oum>1:
                return "H"+str(Hum)+"O"+str(Oum)
        elif x==1:
            if Cum==1 and Oum==1:
                return "C"+"O"
            elif Cum==1 and Oum>1:
                return "C"+"O"+str(Oum)
            elif Cum>1 and Oum==1:
                return "C"+str(Cum)+"O"
            elif Cum>1 and Oum>1:
                return "C"+str(Cum)+"O"+str(Oum)
        elif x==2:
            if Cum==1 and Hum==1:
                return "C"+"H"
            elif Cum==1 and Hum>1:
                return "C"+"H"+str(Hum)
            elif Cum>1 and Hum==1:
                return "C"+str(Cum)+"H"
            elif Cum>1 and Hum>1:
                return "C"+str(Cum)+"H"+str(Hum)
    elif S.count(0)==0:
        if Cum==1 and Hum==1 and Oum==1:
            return "C"+"H"+"O"
        elif Cum==1 and Hum==1 and Oum>1:
            return "C"+"H"+"O"+str(Oum)
        elif Cum==1 and Hum>1 and Oum==1:
            return "C"+"H"+str(Hum)+"O"
        elif Cum>1 and Hum==1 and Oum==1:
            return "C"+str(Cum)+"H"+"O"
        elif Cum==1 and Hum>1 and Oum>1:
            return "C"+"H"+str(Hum)+"O"+str(Oum)
        elif Cum>1 and Hum>1 and Oum==1:
            return "C"+str(Cum)+"H"+str(Hum)+"O"
        elif Cum>1 and Hum==1 and Oum>1:
            return "C"+str(Cum)+"H"+"O"+str(Oum)
        elif Cum>1 and Hum>1 and Oum>1:
            return "C"+str(Cum)+"H"+str(Hum)+"O"+str(Oum)
def convert2(L):
    Cum=L.count("C")
    Hum=L.count("H")
    Oum=L.count("O")
    return "C"+str(Cum)+"H"+str(Hum)+"O"+str(Oum)
#print(convert("HH"))
#es={}
#for ele in hlist:

with open("./bonds.reaxc.route") as f:
    for line in f:
        mline=[]
        sline=[]
        nline=line.split(":")
        mline.append(nline[0])
        #sline.append(nline[0])
        #print(nline[1])
        species=nline[1].split("->")
        #sea=nline[0].split("->")[0].split("+")
        mline.append(species)
        #sline.append(sea)
        #pro=nline[0].split("->")[1].split("+")
        #sro=nline[0].split("->")[1].split("+")
        #mline.append(pro)
        #sline.append(sro)
        a="+"
        mline[1]=list(map(convert,(i for i in mline[1])))
        mline[1]=[x[0] for x in groupby(mline[1])]
        print(mline[0],mline[1])
"""
        #mline[2]=list(map(convert,(i for i in mline[2])))
        #sline[1]=list(map(convert2,(i for i in sline[1])))
        #sline[2]=list(map(convert2,(i for i in sline[2])))
        #if len(mline[1])>1 or len(mline[2])>1:
        #print(mline[0],a.join(mline[1])+"->"+a.join(mline[2]),a.join(sline[1])+"->"+a.join(sline[2]))
        print(mline[0],a.join(mline[1])+"->"+a.join(mline[2]))
"""
