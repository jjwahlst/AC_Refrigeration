# This is the file for homework #2

# figure out how to import CoolProp fucntions
from CoolProp.CoolProp import PropsSI
# quick check example from documentation
# print(PropsSI('D', 'T', 298.15, 'P', 100e5, 'CO2'))

h1 = PropsSI('H','T',273.15,'Q',1,'R134A')
s1 = PropsSI('S','T',273.15,'Q',1,'R134A')
Psat = PropsSI('P','T',(333.15),'Q',1,'R134A')

h2 = PropsSI('H','S', s1, 'P', Psat,'R134A')
sf=PropsSI('S','T',333.15,'Q',0,'R134A')
# s3 = sf
h4 = PropsSI('H','T',273.15,'S',sf,'R134A')

mdot = 20e3/(h1 - h4)
W_in = mdot*(h2-h1)
CoeffPref = 20e3/W_in

print('For R134A:')
print('Mdot = ',mdot, 'W_in = ', W_in, 'COP=', CoeffPref)


h1a = PropsSI('H','T',273.15,'Q',1,'Ammonia')
s1a = PropsSI('S','T',273.15,'Q',1,'Ammonia')
Psata = PropsSI('P','T',(333.15),'Q',1,'Ammonia')

h2a = PropsSI('H','S', s1a, 'P', Psata,'Ammonia')
sfa=PropsSI('S','T',333.15,'Q',0,'Ammonia')
# s3 = sf
h4a = PropsSI('H','T',273.15,'S',sfa,'Ammonia')

mdota = 20e3/(h1a - h4a)
W_ina = mdot*(h2a-h1a)
CoeffPrefa = 20e3/W_in

print('For Ammonia:')
print('Mdot = ',mdota, 'W_in = ', W_ina, 'COP=', CoeffPrefa)
