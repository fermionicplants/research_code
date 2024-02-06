#Binding energy calculation/ semi emiprical mass calculations

#lets start with the decay heat to use as our baseline

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


Astart = 4
Aend = 200
npts = (Aend-Astart) + 1
#variables

x = np.linspace(Astart, Aend, npts)

element_name = "molybdenum"

A = x

N = A/2


Z = A/2
 #dependent on what you have you can just input the equation here remember A = N + Z


#coefficients



def f(A):
  Z = (A/2 -2)
  c_1 = 14       # Volume term coefficient [Mev]


  c_2 = 13      # Surface term coefficient [Mev]


  c_3 =  .60 # Coulomb term coefficient [Mev]

  c_4 = 19 # N-Z Asymmetry term [MeV]

  term1 = c_1*A
  term2 = c_2*(A**.6667)
  term3 = c_3*Z*(Z-1)/(A**.3333)
  term4 = c_4*((A-2*Z)**2)/A

  return ( term1 - term2 -term3 -term4 )/A

  # return  A * P_0*((T_s**(c)) - ((T_0  + T_s)**c))   --> JUST SO YOU KNOW WHAT YOUR X VALUE IS IN THE EQUATION

y = f(x)

plt.xticks(np.arange(min(A), max(A)+10, 10))


plt.plot(x, y, color='red')
plt.grid()


plt.title ('Binding energy of different size atoms',fontsize=20 )

plt.xlabel('A (U)', fontsize=20)
plt.ylabel('E (MeV)', fontsize=20)

plt.show()


