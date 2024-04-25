import random

polevka =[] 
jidla = ["polévka", "vývar", "krém", "kaldoun"]
jidla2 = ["hovězí","kuřecí","kachní","gulášová","frankfurtská"]
jidla3 = ["s rýží","s celentýnskými nudlemi", "s baby karotkou"]

def generace(jidla, jidla2, jidla3):
    i = 1
    n = 5
    while True:
        nova_nabidka = (random.choice(jidla2), random.choice(jidla), random.choice(jidla3))
        if nova_nabidka not in polevka:
            polevka.append(nova_nabidka)
            i += 1
        if i == n:
            break
    print(polevka)

generace(jidla, jidla2, jidla3)


