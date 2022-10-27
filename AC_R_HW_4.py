# Homework 4

from CoolProp.HumidAirProp import HAPropsSI
from CoolProp.CoolProp import PropsSI

# problem 1
mw_1 = 0.2*0.35*1.13473  # from hand calculations
print(mw_1)
hw_1 = PropsSI('H', 'T', 299.15, 'Q', 0, 'H2O')
h1_1 = HAPropsSI('H', 'T', 311.15, 'P', 101.35e3, 'R', 0.7)
h2_1 = HAPropsSI('H', 'T', 299.15, 'P', 101.35e3, 'R', 0.5)

qc_1 = mw_1*hw_1
print(qc_1)

# problem 2
ma_2 = 0.62*1.2253
w1_2 = HAPropsSI('W', 'T', 288.15, 'P', 101.35e3, 'R', 0.3)
w2_2 = HAPropsSI('W', 'T', 318.15, 'P', 101.35e3, 'R', 0.3)

mw_2 = ma_2 * (w2_2 - w1_2)
print(mw_2)

hw_2 = PropsSI('H', 'P', 101.35e3, 'Q', 0, 'H2O')
h2_2 = HAPropsSI('H', 'T', 318.15, 'R', 0.3, 'P', 101.35e3)
h1_2 = HAPropsSI('H', 'T', 288.15, 'R', 0.3, 'P', 101.35e3)
qh_2 = ma_2*(h2_2 - h1_2) - mw_2*hw_2
print(qh_2)

# problem 4

R_2 = (0.25*(0.34*1.13473) + 0.6*(0.89*1.1724))/1.429
print('R is', R_2)
# h_3 = HAPropsSI('H', 'P', 101.35e3, 'R', R_2, )
# T_3 = HAPropsSI('T', 'P', 101.35e3, 'H', h_3, 'R', R_2)

# problem 4

T_b = HAPropsSI('B', 'T', 309.15, 'P', 101.35e3, 'R', 0.4)
print('Dew point Temp is', T_b)
h1_5 = HAPropsSI('H', 'T', 309.15, 'P', 101.35e3, 'R', 0.4)
h2_5 = HAPropsSI('H', 'T', T_b, 'P', 101.35e3, 'R', 0.4)
qc_5 = (1.2*1.13194)*(h1_5 - h2_5)
print(qc_5)

