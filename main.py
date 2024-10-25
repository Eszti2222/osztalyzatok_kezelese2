import metodosuk
lista=[5,2,3,4,4,5,5,5,1,2,2,3,4,5,5,5,4,3,3]

print("1. Mennyi a programozás jegyek átlaga?")
x:float=metodosuk.jegyek_atlaga(lista)
print(f"a jegyek átlaga:{x}")

print("2.Összesen hány ötös van? ")
otos:int=metodosuk.hany_otos(lista,5)
print(f"Összesen {otos} db ötös van.")

print("3.Összesen hányan kaptak elégtelent?")
elegtelen:int=metodosuk.hany_otos(lista,1)
print(f"Összesen {elegtelen} diák kapott elégtelent.")

print("4. Hányas számú diák kapott elégtelent? ")
index_lista=metodosuk.hanyadik_elegtelen(lista)
print(f"A {index_lista} kapott elégtelent")

print("5.Készíts eljárást, mely sávdiagrammal megjeleníti, hogy hány 1-es, hány 2-es, hány 3-as, hány 4-es, hány 5-ös van.")
metodosuk.kiir(lista)





print("6. Készíts eljárást, mely megjeleníti a diákok jegyeit valamilyen látványos formában. 1. diák : 5; 2. diák: 2 (akár lehet egy másik lista a diákok neveivel. ")
i:int=0
while(i<len(lista)):
    jegy=metodosuk.hatos(lista, i)
    print(f"Az {i}.diák: {lista[i]}")
    i+=1

print("7. Készíts eljárást, mely a diákok jegyeinek listáját véletlen számokkal tölti fel.(17 db jegy legyen) Ügyelj arra, hogy ötöst kétszer akkora valószínűséggel adjunk, mint bármely más jegyet. ")
diak_lista=metodosuk.het()
print(f"Véletlen számos lista: {diak_lista}")
