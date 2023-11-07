#Task 2: Predator-Prey Model by Zehra Ahmed 20889523

import numpy as np 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def predator_prey(t,x):
    r,f = x 
    drdt = r * (1- (2*f)) 
    dfdt = -f *(1 - r)
    return (drdt,dfdt)

r0 = 0.5
f0 = 0.3
x0 = (r0,f0)
t_span= (0,20)

sol = solve_ivp(lambda t, x:predator_prey(t,x), t_span, x0)

r =sol.y[0]
f = sol.y[1]
t= sol.t

#Part 1: Population over time
plt.plot(t,r, label = "rabbits")
plt.plot(t,f,label = "foxes")
plt.xlabel('time')
plt.ylabel('population')
plt.legend()
plt.title("Part 1: Population over time")
plt.show()

#Part 2: Phase plot
plt.plot(r,f)
plt.xlabel('rabbits')
plt.ylabel('foxes')
plt.title("Part 2: Phase plot")
plt.show()

#Bonus 
for i in range (0,20):
    plt.plot(r[i],f[i],"o")
    plt.pause(0.1) 
    plt.xlabel('rabbits')
    plt.ylabel('foxes')
    plt.title("Bonus")

plt.show() 
