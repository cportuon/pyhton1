'''
+------------------------------------------------------+
| Viernes 5 Septiembre de 2025                  12:25  |
|______________________________________________________|
| 4.3.8 LAB Conversion del consumo de conbustible      |
|______________________________________________________|                                                      
|                                                      |
|                                                      |
|                                                      |
+------------------------------------------------------+
'''
def litros_100km_a_millas_galones(litros):
    galones = litros / 3.785411784
    millas = 100000 / 1609.344
    return millas / galones 

def millas_galones_a_litros_100km(millas):
    km100 = millas * 1609.344 / 1000 / 100
    litros = 3.785411784
    return litros / km100 

print("3.9 litros son: ", litros_100km_a_millas_galones(3.9), " galones")
print()
print("7.5 litros son: ", litros_100km_a_millas_galones(7.5), " galones")
print()
print("10. litros son: ",litros_100km_a_millas_galones(10.)," galones")
print()
print("60.3 galones son: ", millas_galones_a_litros_100km(60.3), " litros")
print()
print("31.4 galones son: ", millas_galones_a_litros_100km(31.4), " litros")
print()
print("23.5 galones son: ", millas_galones_a_litros_100km(23.5), " litros")
