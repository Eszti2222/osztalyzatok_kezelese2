import metodosuk
lista=[5,2,3,4,4,5,5,5,1,2,2,3,4,5,5,5,4,3,3]
print("2.Összesen hány ötös van? ")
otos:int=metodosuk.hany_otos(lista,5)
print(f"Összesen {otos} db ötös van.")

print("3.Összesen hányan kaptak elégtelent?")
elegtelen:int=metodosuk.hany_otos(lista,1)
print(f"Összesen {elegtelen} diák kapott elégtelent.")

print("5.Készíts eljárást, mely sávdiagrammal megjeleníti, hogy hány 1-es, hány 2-es, hány 3-as, hány 4-es, hány 5-ös van.")
szam:int=metodosuk.kiir(metodosuk.hany_otos(lista,1))


print("1. Mennyi a programozás jegyek átlaga?")
x:float=metodosuk.jegyek_atlaga(lista)
print(f"a jegyek átlaga:{x}")