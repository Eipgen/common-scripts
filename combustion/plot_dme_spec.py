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
T=np.loadtxt("bjchen.txt")

step=T[:,0]
T0=savgol_filter(T[:,1],4001,2)
T1=savgol_filter(T[:,2],4001,2)
T2=savgol_filter(T[:,3],4001,2)
T3=savgol_filter(T[:,4],4001,2)
T4=savgol_filter(T[:,5],4001,2)
T5=savgol_filter(T[:,6],4001,2)
T6=savgol_filter(T[:,7],4001,2)
T7=savgol_filter(T[:,8],4001,2)
T8=savgol_filter(T[:,9],4001,2)

tot=np.array([step,T0,T1,T2,T3,T4,T5,T6,T7,T8])
tot=tot.T

tot0=tot[:,0][0:6390:600]
tot1=tot[:,1][0:6390:600]
tot2=tot[:,2][0:6390:600]
tot3=tot[:,3][0:6390:600]
tot4=tot[:,4][0:6390:600]
tot5=tot[:,5][0:6390:600]
tot6=tot[:,6][0:6390:600]
tot7=tot[:,7][0:6390:600]
tot8=tot[:,8][0:6390:600]
tot9=tot[:,9][0:6390:600]

tot10=np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
tot11=np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])

print(len(tot0))
plt.figure(figsize=(10,14))
plt.legend(loc='best', bbox_to_anchor=(0.3,0.5),ncol=1,prop={'family': 'Arial','size' :16},frameon=False)
grid = plt.GridSpec(4, 4, wspace=0.5, hspace=0.5)
ax1=plt.subplot(grid[0,0:4])
plt.plot(step,T1,linestyle="--",linewidth=2,color="blue")
plt.scatter(tot0,tot2,marker="x",s=120,color='blue',label="CO$\mathregular{_2}$")
ax1.set_xticks([])
#ax1.set_title("DME reaction in 1500K with CVHD",**font2)
ax1.set_xlim(0,70)
ax1.set_ylim(180,200)
ax1.tick_params(labelsize=25)

ax2=plt.subplot(grid[1,0:4])
ax2.set_xticks([])
ax2.tick_params(labelsize=25)
ax2.set_ylim(50,100)
ax2.set_xlim(0,70)
plt.plot(step,T0,linestyle="--",linewidth=2,color="skyblue")
plt.scatter(tot0,tot1,marker="*",s=120,color="skyblue",label="CH$\mathregular{_4}$")
#plt.legend(loc='center left', bbox_to_anchor=(0.05,0.9),ncol=3,prop={'family': 'Arial','size' :16},frameon=False)
#plt.plot(step,T[:,1])

ax3=plt.subplot(grid[2:4,0:4])
y_major_locator=MultipleLocator(10)
x_major_locator=MultipleLocator(10)

plt.gca().yaxis.set_major_locator(y_major_locator)
plt.gca().xaxis.set_major_locator(x_major_locator)
#plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
#plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

#plt.plot(step,T3,linestyle="--",linewidth=2,color='orange')
plt.plot(step,T2,linestyle="--",linewidth=2,color="green")
plt.plot(step,T3,linestyle="--",linewidth=2,color="red")
plt.plot(step,T4,linestyle="--",linewidth=2,color="purple")
plt.plot(step,T5,linestyle="--",linewidth=2,color="cyan")

plt.scatter(tot0,tot10,marker="x",s=120,color='blue',label="CO$\mathregular{_2}$")
plt.scatter(tot0,tot11,marker="x",s=120,color='skyblue',label="CH$\mathregular{_4}$")

#plt.scatter(tot0,tot1,marker="*",s=120,color='orange',label="C$\mathregular{_2}$H$\mathregular{_6}$O")
plt.scatter(tot0,tot3,marker="o",s=120,color="green",label="H$\mathregular{_2}$")
plt.scatter(tot0,tot4,marker="v",s=120,color="red",label="CO")
plt.scatter(tot0,tot5,marker="^",s=120,color="purple",label="CH$\mathregular{_3}$")
plt.scatter(tot0,tot6,marker="s",s=120,color="cyan",label="CH$\mathregular{_2}$")

ax3.set_ylim(0,30)
ax3.set_xlim(0,70)
ax3.tick_params(labelsize=25)



plt.legend(loc='best', bbox_to_anchor=(0.2,0.5),ncol=1,prop={'family': 'Arial','size' :16},frameon=False)
plt.xlabel("Time/ps",**font2)
plt.savefig("test_spec.png")
