import numpy as np 
import matplotlib.pyplot as plt
def func(x):
    return 0.5*np.exp(x)+1
a,b=1,10
x=np.linspace(0,2.5)
y=func(x)
fig,ax=plt.subplots(figsize=(8,5))
plt.plot(x,y,'b',linewidth=2)
plt.ylim(ymin=0)
