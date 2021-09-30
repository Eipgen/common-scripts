import numpy as np
from collections import OrderedDict,Counter,defaultdict
import itertools
import matplotlib.pyplot as plt
import numpy as np

def convert(L):
    Cum=L.count("C")
    Hum=L.count("H")
    Oum=L.count("O")
    return [Cum,Hum,Oum]

#print(convert("OOHH"))

def getnumber4(s):
    num=np.zeros((len(h)))
    for i,t in enumerate(h):
        if s in h[t]:
            num[i]=h[t][s]
    return num

specs=['C2H6O1', 'C1H2O1', 'C1H3O2', 'C1H4O2', 'C0H2O1', 'C0H0O2', 'C0H1O1', 'C0H1O2', 'C1H4O0']
a=[]
c={}
with open("dump.ch.species") as f:
    for line in f:
        line=line.split(" ")
        a.append(line)
    h={}
    for i in range(len(a)):
        b=[a[i][j:j+2] for j in range(0,len(a[i]),2)]

        b[0][1]=int((b[0][1][:-1]))
        for s in range(len(b[1:])):
            fol="C"+str(convert(b[1:][s][0])[0])+"H"+str(convert(b[1:][s][0])[1])+"O"+str(convert(b[1:][s][0])[2])
            b[1:][s][0]=fol
            b[1:][s][1]=int(b[1:][s][1])
        d=[]
        for i in b:
            c={}
            c[i[0]]=i[1]
            d.append(c)
        f={}
        for j in d:
            for k,v in j.items():
                f.setdefault(k,[]).append(v)
        g=[{k:sum(v)} for k,v in f.items()]
        #print(g)
        for i in g[1:]:
            g[1].update(i)
        h[g[0]["Timestep"]]=g[1]
#print(h)

nums=[getnumber4(x) for x in specs]
#print(len(nums[1]))
print(specs)
for j in range(10001):
    print(nums[0][j],nums[1][j],nums[2][j],nums[3][j],nums[4][j],nums[5][j],nums[6][j],nums[7][j],nums[8][j])

"""
nums = [getnumber4(x) for x in specs]
print(nums)
steps4=np.array(list(c.keys()))[0:100001:1000]
reactant4=nums[0]+nums[1]+nums[2]+nums[3]
nums4=[]
nums4.insert(0,reactant4[0:100001:1000])
nums4.insert(1,nums[4][0:100001:1000])
nums4.insert(2,nums[5][0:100001:1000])

spec=["RP-1","C2H4","H2"]
f,ax=plt.subplots(2,2,figsize=(14,10))


ax[1][1].plot(steps4/10000,nums4[0],label="RP-1",linewidth=2,c="dodgerblue")
ax[1][1].plot(steps4/10000,nums4[1],label="Ethylene",linewidth=2,c="m")
ax[1][1].plot(steps4/10000,nums4[2],label="Hydogen",linewidth=2,c="y")
ax[1][1].set_xlabel("Time(ps)")
ax[1][1].set_ylabel("Molecule number")
#ax[1][1].set_title("CVHD_2500K")
#ax[1][1].tick_params(labelcolor='r',labelsize=12,width=2)
#ax[1][1].set_yticks([0,10,20,30,40,50,60])
ax[1][1].legend(loc='best')

plt.savefig("CVHD.png")
"""
