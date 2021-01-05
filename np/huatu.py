#f(x) = sin^2(x-2)e^-x2
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.sin(x-2)**2) * np.exp(-x**2)
    #return np.sin(x)

x = np.linspace(0,2,1000)
plt.style.use('seaborn')

plt.plot(x,f(x), 'r-', linewidth=3, label='f(x)')

plt.show()