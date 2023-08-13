import random
def funParticipantes():
    dicParticipantes={}
    nombre=""
    dni=1
    band=True
    while band:  
        dni=input("ingrese un dni: ")
        
        if dni=="0":
            band=False
        else:
            nombre=input("ingrese un nombre: ").upper()
            dicParticipantes[dni]=nombre
       
    return dicParticipantes
def sorteo(dicParcipantes):
    largo=len(dicParcipantes)
    ganador=random.choice(list(dicParcipantes.values()))
    print("el ganador es:...........", ganador)

print("ingrese un DNI y el nombre de los participantes, para finalizar la carga ingrese DNI=0")
diccionario=funParticipantes()
pregunta=input("desea realizar el sorteo S/N: ").upper()
if pregunta=="S":
    sorteo(diccionario)
