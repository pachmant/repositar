def soubor(a,b):
    soubor=open(a+".txt",'w')
    soubor.write(b+"\n")
    soubor.close()

def pridani(a,b):
    soubor=open(a+".txt",'a')
    soubor.write(b+"\n")
    soubor.close()

def precti(a):
    soubor=open(a+".txt",'r') 
    print(type(soubor))
    for line in soubor:
        print(line, end="")
    soubor.close

if __name__=="__main__":

# Vytvoreni a zapis
    # 1.zpusob
    soubor=open("mujnovysoubor.txt",'w')
    soubor.write("Ahoj svete\n")
    soubor.close()

    # 2.zpusob
    with open("muj novysoubor2.txt",'w') as f:
        f.write("Ahoj svete2\n")

# Cteni
    # 1.zposob
    soubor=open("mujnovysoubor.txt",'r') 
    print(type(soubor))
    for line in soubor:
        print(line)
    soubor.close

    # 2.zpusob
    with open("muj novysoubor2.txt",'r') as f:
        print(f.readline())

    # 2,5.zpusob
        # line=f.readline()
        # print(line)
    
# Append
    # 1.zpusob
    soubor=open("mujnovysoubor.txt",'a')
    soubor.write("Ahoj sveteNew\n")
    soubor.close

    a=input(("Zadej nazev souboru:"))
    b=input(("Zadej co chces napsat:"))
    
    soubor(a,b)
    pridani(a,b)
    precti(a)

