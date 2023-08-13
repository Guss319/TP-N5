import random
def funcSuerte():
    numero=random.randint(1,8)
    if numero==1:
        rta="Es seguro que si"
    else:
        if numero==2:
            rta="Las chances son buenas"
        else:
            if numero==3:
                rta="Puedes contar con ello"
            else:
                if numero==4:
                    rta="Pregunta de nuevo mas tarde"
                else:
                    if numero==5:
                        rta="Concentrate y pregunta de nuevo"
                    else:
                        if numero==6:
                            rta="No veo con claridad, pregunta de nuevo"
                        else:
                            if numero==7:
                                rta="Mi repuesta es NO"
                            else:
                                if numero==8:
                                    rta="Los seres de la 4º dimension dicen que no"
    return rta
input("Realiza una pregunta....=")
print ("la repuesta es la siguente: ", funcSuerte())