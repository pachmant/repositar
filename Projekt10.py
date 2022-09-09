def napis_ahoj():
    print("Ahoj")

def napis_co_ti_poslu(veta):
    print(veta)

def nxn_hvezdicek(a,b):
    for i in range(0,a,1):
        for j in range(0,b,1):
            print("*", end ="")
        print()    

def vrat_mi_2():
    return 2

def soucet(c,d):
    return c+d

def odcitani(e,f):
    return e-f

def nasobeni(g,h):
    return g*h

def deleni(i,j):
    return i/j

if __name__=="__main__":

    a=5
    napis_ahoj()
    slovo="Ahoj svete pisu ted neco noveho"
    napis_co_ti_poslu(slovo)
    napis_co_ti_poslu("Ahoj tohle pisu jinym zpusobem")
    napis_co_ti_poslu(veta="Ahoj toto je dalsi zpusob")
    
    nxn_hvezdicek(5,8)
    nxn_hvezdicek(5,5)
    
    b=vrat_mi_2()
    print(b)
    print(vrat_mi_2())
    nxn_hvezdicek(vrat_mi_2(),vrat_mi_2())

    print(soucet(5,6))
    b=soucet(10,4)
    b=soucet(b,6)
    print(b)

    print(odcitani(10,5))
    a=odcitani(50,10)
    a=odcitani(a,5)
    print(a)

    print(nasobeni(5,10))

    print(deleni(50,10))

    vysledek=deleni(nasobeni(soucet(6,5),3),2)
    print(vysledek)

