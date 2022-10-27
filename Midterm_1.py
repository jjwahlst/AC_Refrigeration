# Code for Midterm 1

# Import Cool Prop Stuff
import numpy as np
import math
import scipy
import CoolProp
import CoolProp.CoolProp as Cool
from CoolProp.HumidAirProp import HAPropsSI
from CoolProp.CoolProp import PropsSI
Cool.set_reference_state('water', 'DEF')

# Set ASHRAE reference to check from WISC.edu
Cool.set_reference_state('R134a', 'ASHRAE')

# Problem 1
Psat_10 = PropsSI('P', 'T', 283.15, 'Q', 1, 'R410a')
h1_1 = PropsSI('H', 'T', 293.15, 'P', Psat_10, 'R410a')
s1_1 = PropsSI('S', 'T', (20+273.15), 'P', Psat_10, 'R410a')
h2s_1 = PropsSI('H', 'T', (60+273.15), 'S', s1_1, 'R410a')
h2_1 = h1_1 + (h2s_1 - h1_1)/0.65
Psat_60 = PropsSI('P', 'T', (60+273.15), 'Q', 1, 'R410a')
h3_1 = PropsSI('H', 'T', (273.15+55), 'P', Psat_60, 'R410a')

Q_1 = 17.585e3

mdot_1 = Q_1/(h1_1 - h3_1)
# ANSWER
W_1 = mdot_1*(h2_1 - h1_1)
print('Power input for compressor is', W_1, 'W')



# PROBLEM 2

hw = PropsSI('H', 'T', (22+273.15), 'Q', 0, 'water')

print('Enthalpy of Sat Water Vap is', hw/1000, 'kJ/kg')


# PROBLEM 3

h2_3 = HAPropsSI('H', 'T', (273.15+24), 'P', 101.325e3, 'R', 0.5)
ho_3 = HAPropsSI('H', 'T', (273.15+8), 'P', 101.325e3, 'R', 0.5)

ma0_ma1 = 24000/(h2_3 - ho_3)

print('Ratio of mao/ma1 is', ma0_ma1)












