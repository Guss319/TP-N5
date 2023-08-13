import random
dicLista={2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
while True:
    numero=random.randint(2,10)
    valor=0
    valor=dicLista[numero]+1
    dicLista[numero]=valor 
    i=2
    band=True
    while i<11 and band:  
        if dicLista[i]==0:
            band=False
        else:
            i=i+1
    if i==11:
        break
print(dicLista)
