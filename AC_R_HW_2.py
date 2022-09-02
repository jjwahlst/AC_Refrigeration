# This is the file for homework #2

# figure out how to import CoolProp fucntions
from CoolProp.CoolProp import PropsSI
# quick check example from documentation
# print(PropsSI('D', 'T', 298.15, 'P', 100e5, 'CO2'))

h1 = PropsSI('H','T',273.15,'Q',1,'R134A')
s1 = PropsSI('S','T',273.15,'Q',1,'R134A')
Psat = PropsSI('P','T',(333.15),'Q',1,'R134A')
print(h1)
h2 = PropsSI('H','S', s1, 'P', Psat,'R134A')
print(h2)