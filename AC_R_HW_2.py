# This is the file for homework #2

# figure out how to import CoolProp functions
from CoolProp.CoolProp import PropsSI
# quick check example from documentation
# print(PropsSI('D', 'T', 298.15, 'P', 100e5, 'CO2'))

# problem 2

h1 = PropsSI('H', 'T', 273.15, 'Q', 1, 'R134A')
s1 = PropsSI('S', 'T', 273.15, 'Q', 1, 'R134A')
P_sat = PropsSI('P', 'T', 333.15, 'Q', 1, 'R134A')

h2 = PropsSI('H', 'S', s1, 'P', P_sat, 'R134A')
# h4 = h3 = hf(333.15)
h4 = PropsSI('H', 'T', 333.15, 'Q', 0, 'R134A')

m_dot = 20e3/(h1 - h4)
W_in = m_dot*(h2-h1)
COP_r134a = 20e3/W_in

print('For R134A:')
print('Mdot = ', m_dot, 'W_in = ', W_in, 'COP=', COP_r134a)


h1a = PropsSI('H', 'T', 273.15, 'Q', 1, 'Ammonia')
s1a = PropsSI('S', 'T', 273.15, 'Q', 1, 'Ammonia')
P_sata = PropsSI('P', 'T', 333.15, 'Q', 1, 'Ammonia')

h2a = PropsSI('H', 'S', s1a, 'P', P_sata, 'Ammonia')
sfa = PropsSI('S', 'T', 333.15, 'Q', 0, 'Ammonia')
# h4 = h3 = hf(333.15)
h4a = PropsSI('H', 'T', 333.15, 'Q', 0,'Ammonia')

m_dota = 20e3/(h1a - h4a)
W_ina = m_dota*(h2a-h1a)
COP_A = 20e3/W_ina

print('For Ammonia:')
print('Mdot = ', m_dota, 'W_in = ', W_ina, 'COP=', COP_A)


# problem 3

n_c = 0.65
Q_load = 10e3

h1_p2 = PropsSI('H', 'T', 277.15, 'Q', 1,'R290')
# h4 = h3
h4_p2 = PropsSI('H', 'T', 329.15, 'Q', 0, 'R290')

m_dot_P2 = Q_load/(h1_p2 - h4_p2)

s1_p2 = PropsSI('S','T', 277.15, 'Q', 1, 'R290')
P_sat_p2 = PropsSI('P','T', 329.15, 'Q', 1, 'R290')

h2s = PropsSI('H','S', s1_p2, 'P', P_sat_p2, 'R290')

h2_p2 = h1_p2 +(h2s - h1_p2)/n_c
W_in_p2 = m_dot_P2*(h2_p2-h1_p2)

COP_p2 = Q_load/W_in_p2

T_2 = PropsSI('T', 'P', P_sat_p2, 'H', h2_p2, 'R290')
T_2_C = T_2 - 273.15

print('COP for Problem 2 is', COP_p2)
print('Compressor discharge Temperature (C) is', T_2_C)

