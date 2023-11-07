#BVP by Zehra Ahmed 20889523
import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def dxdr(r, x):
    # x= [T, u]
    df1= x[1]
    df2= -x[1]/r
    return [df1, df2]

def bc(xa,xb):
    return [xa[0]-120,xb[0]-60]


sol= solve_bvp(dxdr,bc,np.linspace(5,10),np.zeros((2,50)))

print(sol.x)

x = sol.x
T =sol.y[0]
u = sol.y[1]
plt.plot(x,T)
plt.plot(x,u)
plt.show()



