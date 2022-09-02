# This is the file for homework #2

# figure out how to import CoolProp functions
from CoolProp.CoolProp import PropsSI
# quick check example from documentation
# print(PropsSI('D', 'T', 298.15, 'P', 100e5, 'CO2'))

h1 = PropsSI('H', 'T', 273.15, 'Q', 1, 'R134A')
s1 = PropsSI('S', 'T', 273.15, 'Q', 1, 'R134A')
P_sat = PropsSI('P', 'T', 333.15, 'Q', 1, 'R134A')

h2 = PropsSI('H', 'S', s1, 'P', P_sat, 'R134A')
sf = PropsSI('S', 'T', 333.15, 'Q', 0, 'R134A')
# s3 = sf
h4 = PropsSI('H', 'T', 273.15, 'S', sf, 'R134A')

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
# s3 = sf
h4a = PropsSI('H', 'T', 273.15, 'S', sfa, 'Ammonia')

m_dota = 20e3/(h1a - h4a)
W_ina = m_dota*(h2a-h1a)
COP_A = 20e3/W_ina

print('For Ammonia:')
print('Mdot = ', m_dota, 'W_in = ', W_ina, 'COP=', COP_A)
