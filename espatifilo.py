# Verificar una cadena de texto, con 3 posibles salidas 

espatifilo = input()

if espatifilo == "ESPATIFILO": 
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
    exit()
elif espatifilo == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
    exit()
else: 
    print("¡Espatifilo!, ¡No", espatifilo, "!")
    exit()