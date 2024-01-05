import numpy as np
from scipy.linalg import lu_factor, lu_solve
import matplotlib.pyplot as plt



#spacing for y
dy=.006
(y0,yend)=(0,0.1)
n=int((yend-y0)/dy + 1) #number of points in y
y_val=np.linspace(y0,yend,n)


#spacing for t
dt=15
(t0,tend)=(0,1500)
m=int((tend-t0)/dt + 1) #number of points in t
t_val=np.linspace(t0,tend,m)

#lambda=(mu/2 rho) delt/dely^2
mu=8.931e-4 #kg /m s
rho=994.6 #kg/m^3
lam=mu/(2*rho) *dt/dy**2#note it can be shown that 2*lam>0.5 creates some oscillations
print('lambda is =',lam)

vmax=0.2#m/s
#row 1 of V holds velocity values at t0=0
#row 2 holds values at t=t0+delt
#row 3 holds values at t=t0+2*delt
#we need m rows, n columns
V=np.zeros((m,n))

#apply BCs
V[:,0]=vmax#bottom velocity, vmax
#V[:,-1]=0 velocity at the end nodes of position already zero.



A=np.diag((1+2*lam)*np.ones(n-2))+np.diag(-lam*np.ones(n-3),1)+\
  np.diag(-lam*np.ones(n-3),-1)
#factor A
lu, piv = lu_factor(A)#this doesnt change 

#now for b  
for l in range(m-1):
 	b=lam*V[l,:-2]+(1-2*lam)*V[l,1:-1]+lam*V[l,2:]
	#add lam Vmax to it
 	b[0]+=lam*V[l,0]
 	V[l+1,1:-1] = lu_solve((lu, piv), b)
 
 
#V vs position at various times
plt.figure()
snap1=10
snap2,snap3=2*snap1,3*snap1

plt.plot(y_val,V[snap1,:])
plt.plot(y_val,V[snap2,:])
plt.plot(y_val,V[snap3,:])
plt.xlabel("y")
plt.ylabel("$V_x$")
plt.title("V as a function of position")

plt.legend(['t = '+str(t_val[snap1]) + ' s',\
			   't = '+str(t_val[snap2]) + ' s','t = '+str(t_val[snap3])+ ' s'])
	
#V vs time for various positions
plt.figure()
plt.title("V as a function of time")
for i in range(0,n,2):
	plt.plot(t_val,V[:,i],label='node'+str(i))
plt.xlabel("t")
plt.ylabel("V")
plt.legend()
plt.show()