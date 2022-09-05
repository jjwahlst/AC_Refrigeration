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

print('COP for Problem 3 is', COP_p2)
print('Compressor discharge Temperature (C) is', T_2_C)

# Problem 4

nc_4 = .68
Q_ref = 70.3371e3

h1_4 = PropsSI('H', 'Q', 1, 'T', 268.15, 'R404a')

s1_4 = PropsSI('S', 'T', 268.15, 'Q', 1, 'R404a')
P_sat_4 = PropsSI('P', 'T', 318.15, 'Q', 1, 'R404a')

h2s_4 = PropsSI('H', 'S', s1_4, 'P', P_sat_4, 'R404a')
h2_4 = h1_4 + ((h2s_4 - h1_4)/nc_4)
# h4 = h3
h4_4 = PropsSI('H', 'T', 318.15, 'Q', 0, 'R404a')

m_4 = Q_ref/(h1_4 - h4_4)

W_in4 = m_4*(h2_4 - h1_4)

COP_4 = Q_ref/W_in4

print('COP for Problem 4 part a is:', COP_4)

# part b

h_1b = PropsSI('H', 'T', 268.15, 'Q', 1, 'R404a')
sb = PropsSI('S', 'T', 268.15, 'Q', 1, 'R404a')
P_sat_red = PropsSI('P', 'T', 303.15, 'Q', 1, 'R404a')
h_2sb = PropsSI('H', 'P', P_sat_red, 'S', sb, 'R404a')
# h4 = h3
h_4b = PropsSI('H', 'T', 268.15, 'Q', 0, 'R404a')
h_2b = h_1b + (h_2sb - h_1b)/nc_4
m_1 = Q_ref/(h_1b - h_4b)

W_1 = m_1*(h_2b - h_1b)
h_5 = PropsSI('H', 'Q', 1, 'T', 303.15, 'R404a')
h_7 = PropsSI('H', 'Q', 0, 'T', 318.15, 'R404a')

mc = m_1*(h_5-h_2b)/(h_5-h_7)

m_3 = m_1 + mc
s5 = PropsSI('S', 'T', 303.15, 'Q', 1, 'R404a')
# h_5 = PropsSI('H', 'T', 303.15, 'Q', 1, 'R404a')
h_6s = PropsSI('H', 'S', s5, 'T', 318.15, 'R404a')

h_6 = h_5 + (h_6s - h_5)/nc_4
W_2 = m_3*(h_6 - h_5)

W_total = W_1+W_2
COP_4b = Q_ref/W_total

print('COP for Problem 4 part b is:', COP_4b)

