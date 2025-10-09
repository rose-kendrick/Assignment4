import numpy as np
import matplotlib.pyplot as plt

k=1.3807e-23 #J/K
c=299792458 #m/s
I=6
v=[0.6e9, 1.2e9, 2.4e9, 4.8e9, 9.6e9, 22e9] #frequency (Hz)
a=[2e-4, 4e-4, 8e-4, 1.6e-3, 3.2e-3, 7e-3] #constant that depends of frequency,v 
b=[1.15, 1.18, 1.2, 1.23, 1.26, 1.30] #constant that depends of frequency,v 
d=[0.0025, 0.0027, 0.0030, 0.0033, 0.0036, 0.0040] #constant that depends of frequency,v
D=[0, 50, 100,170, 250, 375] #depth from 1 bar level (km)
e=2.7182818284590452353602874713527 
F=[7.59342e-21, 6.15189e-20, 3.90419e-19, 1.86758e-18, 8.12656e-18, 4.14506e-17]
T=[]


def f(T,i):
    #(W m^-2 sr^-1 Hz^-1)                               
    y = (((2*k*(v[i])**2)/(c**2))*(T/(1+(d[i])*np.sqrt(T)))*(1-e**((-a[i])*(T)**(b[i]))))-F[i]
    return y

li=float(input('guess a value '))
mi=float(input('guess another value '))

tol=1e-23

for i in range(I):
    l,m=li,mi
    

    if f(l,i)*f(m,i)>0:
        print('Try again with differnt numbers')
    else:
        while abs(f(l,i)) > tol:
            n = (l+m)/2
            if f(l,i)*f(n,i) < 0:
                m=n
            else:
                l=n
        print(l,i,f(l,i))
        T.append(l)

print(T)


plt.plot(T, D)    
plt.xlabel('T (K)') 
plt.ylabel('Depth (km)')
plt.title('Temperature vs. Depth')
plt.savefig('mwrTemperature.png')


