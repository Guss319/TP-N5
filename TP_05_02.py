import TP_05_01
def funSumarNumeros(n1,n2):
    suma=n1+n2
    redondeado=TP_05_01.funRedondear(suma)
    print(f"{n1} + {n2} = {suma} y su valor redondeado es: {redondeado}")

n1=float(input("ingrese el numero A: "))
n2=float(input("ingrese el numero B: "))
funSumarNumeros(n1,n2)