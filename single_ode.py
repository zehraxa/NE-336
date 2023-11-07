# Task 1 by Zehra Ahmed 20889523

import numpy as np 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def myode(t,x,B):
    dxdt = B * x
    return dxdt

x0 = 10
t_span = (5, 15)
B_values = [-2,-4,-6,-8]

plt.figure()

for B in B_values:
    sol = solve_ivp(lambda t, x: myode(t, x, B), t_span, [x0])
    t = sol.t
    x = sol.y[0]
    plt.plot(t, x,label= {B})

plt.xlabel('time')
plt.ylabel('x(t)')
plt.title(f'the solution of dx/dt = {B_values}x')
plt.grid()
plt.legend()
plt.show()