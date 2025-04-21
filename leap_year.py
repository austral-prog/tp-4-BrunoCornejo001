def leap_yaer(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

anio = int(input("Ingrese un año: "))

if es_bisiesto(anio):
    print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} no es bisiesto")

leap_year()
