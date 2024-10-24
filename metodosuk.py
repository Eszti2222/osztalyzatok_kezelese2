def hany_otos(lista,szam):
    i:int=0
    while(i<len(lista)):
        if(i<lista[i]==szam):
            szam+=1
        i+=1
    return szam

def kiir(lista,szam):
    kiir_lista=[]
    print(szam)
    
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
    index_lista:int=0
    while (i<len(lista)):
        if (lista[i]==1):
            x+=1
            index_lista.append(i)
        i+=1
    return index_lista
