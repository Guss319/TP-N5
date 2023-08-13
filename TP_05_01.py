def funRedondear(numero):
    entero,decimal=divmod(numero,1)
    if decimal>0.5:
            entero+=1
    return entero
numero=float(input("ingrese un numero: "))
print(f"el numero fue redondeado a: ", funRedondear(numero))