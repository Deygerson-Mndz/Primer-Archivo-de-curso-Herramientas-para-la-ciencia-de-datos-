def calcular_impuestos(edad,ingresos):
    if edad >= 18 and ingresos >= 1000:
        print (ingresos * 0.4)
    else: 
        print (0)

calcular_impuestos(18,1000)
calcular_impuestos(40,10000)
calcular_impuestos(17,5000)