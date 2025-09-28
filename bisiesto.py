# es un año bisiesto, si o no, y si entra dentro del periodo Gregoriano

year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
    if year % 4 != 0:
        print("Año común")
    elif year % 100 != 0:
        print("Año bisiesto")
    elif year % 400 != 0:
        print("Año común")
    else:
        print("Año bisiesto")