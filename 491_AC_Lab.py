# Getting Specific Volume of Air

from CoolProp.HumidAirProp import HAPropsSI
import numpy as np

Twb = [9.799321, 9.748544, 9.572762, 9.479014, 9.439949, 9.498548, 9.705574, 9.87744, 9.912615, 9.943872, 10.01025]
Twb = np.add(Twb, 273.15)
va = np.zeros(10)

for i in range(len(Twb)-1):
    va[i] = HAPropsSI('V', 'Twb', Twb[i], 'T', 300, 'P', 96800)

print(va)






