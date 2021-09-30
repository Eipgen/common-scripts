import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from scipy.signal import savgol_filter    
import matplotlib.ticker as ticker


from matplotlib.pyplot import MultipleLocator

plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.f'))

font2 = {'family' : 'Arial',
        'weight' : 'normal',
        'size'   : 24,
} 
T=np.loadtxt("newreac.txt")

step=T[:,0]/(1e+9)

plt.figure(figsize=(10,10))
grid = plt.GridSpec(4, 4, wspace=0.5, hspace=0.5)
ax1=plt.subplot(grid[0,0:4])

T5=T[:,6]
T5=savgol_filter(T5,10001,2)

plt.plot(step,T5,linestyle="--",linewidth=4,color="blue",label="O$\mathregular{_2}$")
ax1.set_xticks([])
ax1.set_title("DME reaction in 1500K with CVHD",**font2)
#ax1.set_xlim(0,12)
ax1.set_ylim(170,180)
ax1.tick_params(labelsize=25)
plt.legend(loc='center left', bbox_to_anchor=(0.05,0.9),ncol=3,prop={'family': 'Arial','size' :16},frameon=False)
#plt.plot(step,T[:,1])
ax2=plt.subplot(grid[1:4,0:4])
T0=T[:,1]
T1=T[:,2]
T2=T[:,3]
T3=T[:,4]
T4=T[:,5]

T0=savgol_filter(T0,9501,2)
T1=savgol_filter(T1,9501,2)
T2=savgol_filter(T2,9501,2)
T3=savgol_filter(T3,9501,2)
T4=savgol_filter(T4,9501,2)

"""
tot=np.array([step,T0,T1,T2,T3,T4,T5])
tot=tot.T
for i in tot:
    print(i)
tot0=tot[:,0][0:10001:1000]
tot1=tot[:,1][0:10001:1000]
tot2=tot[:,2][0:10001:1000]
tot3=tot[:,3][0:10001:1000]
tot4=tot[:,4][0:10001:1000]
tot5=tot[:,5][0:10001:1000]
tot6=tot[:,6][0:10001:1000]
"""

y_major_locator=MultipleLocator(5)
#x_major_locator=MultipleLocator(2)
plt.gca().yaxis.set_major_locator(y_major_locator)
#plt.gca().xaxis.set_major_locator(x_major_locator)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

plt.plot(step,T0,linestyle="--",linewidth=4,color='orange',label="C$\mathregular{_2}$H$\mathregular{_6}$O")
plt.plot(step,T1,linestyle="--",linewidth=4,color="green",label="CH$\mathregular{_2}$O")
plt.plot(step,T2,linestyle="--",linewidth=4,color="red",label="CH$\mathregular{_3}$O$\mathregular{_2}$")
plt.plot(step,T3,linestyle="--",linewidth=4,color="purple",label="CH$\mathregular{_4}$O$\mathregular{_2}$")
plt.plot(step,T4,linestyle="--",linewidth=4,color="cyan",label="H$\mathregular{_2}$O")
"""
plt.scatter(tot0,tot1,marker="*",linewidth=4,color='orange',label="C$\mathregular{_2}$H$\mathregular{_6}$O")
plt.scatter(tot0,tot2,marker="*",linewidth=4,color="green",label="CH$\mathregular{_2}$O")
plt.scatter(tot0,tot3,marker="*",linewidth=4,color="red",label="CH$\mathregular{_3}$O$\mathregular{_2}$")
plt.scatter(tot0,tot4,marker="*",linewidth=4,color="purple",label="CH$\mathregular{_4}$O$\mathregular{_2}$")
plt.scatter(tot0,tot5,marker="*",linewidth=4,color="cyan",label="H$\mathregular{_2}$O")
"""
ax2.set_ylim(0,20)
#ax2.set_xlim(0,12)
ax2.tick_params(labelsize=25)
plt.legend(loc='best', bbox_to_anchor=(0.3,0.5),ncol=1,prop={'family': 'Arial','size' :16},frameon=False)
plt.xlabel("Time/ms",**font2)
plt.savefig("dme_spec_new.png")
