import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt

'''def f(x):
    return Gamma(x)'''

alpha_values = [1,2,3,3,3]
# alpha is the shape parameter
beta_values = [0.5,0.5,0.5,1,2]
#beta is the rate parameter
color = ['b','r','g','y','m']
x = np.linspace(1E-6, 10, 1000)


fig, ax = plt.subplots(figsize=(12, 8))

for k, t, c in zip(alpha_values, beta_values, color):
    dist = gamma(k, 0, t)
    plt.plot(x, dist.pdf(x), c=c, label=r'$alpha=%.1f,\ \theta=%.1f$' %(k,
        t))


plt.title('Gamma Distribution')
plt.xlim(0,10)
plt.ylim(0,2)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\alpha, \beta)$')

plt.legend(loc=0)
plt.show()

