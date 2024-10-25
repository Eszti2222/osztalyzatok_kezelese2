def hany_otos(lista,szam):
    i:int=0
    while(i<len(lista)):
        if(i<lista[i]==szam):
            szam+=1
        i+=1
    return szam

def kiir(lista,szam,):
    kiir_lista=[]
    i:int=0
    db:int=0
    while(i<len(lista)):
        if(szam==lista[i]):
            db+=1
        i+=1
    kiir_lista.append(db)
    kiir_lista.append(szam)
    return kiir_lista
        
def jegyek_atlaga(lista):
    i:int=0
    db:int=0
    osszeg:int=0
    while i<len(lista):
        osszeg=lista[i]+osszeg
        db+=1
        i+=1
    atlag:float=osszeg/db
    return atlag

def hanyadik_elegtelen(lista):
    i:int=0
    index_lista=[]
    while (i<len(lista)):
        if (lista[i]==1):
            index_lista.append(i)
        i+=1
    return index_lista

