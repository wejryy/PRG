def calt():
    print("Jak chces spocitat")
    print("1. Scitani")
    print("2. Odcitani")
    print("3. Nasobeni")
    print("4. Deleni")
    print("5. Exit")

    operace = input("Zadej operaci: ")

    if operace == "1":
        num1 = int(input("Zadej prvni cislo: "))
        num2 = int(input("Zadej druhe cislo: "))
        vysledek = num1 + num2
        print("Vysledek je: ", vysledek)

    elif operace == "2":
        num1 = int(input("Zadej prvni cislo: "))
        num2 = int(input("Zadej druhe cislo: "))
        vysledek = num1 - num2
        print("Vysledek je: ", vysledek)    

    elif operace == "3":
        num1 = int(input("Zadej prvni cislo: "))
        num2 = int(input("Zadej druhe cislo: "))
        vysledek = num1 * num2
        print("Vysledek je: ", vysledek)

    elif operace == "4":
        num1 = float(input("Zadej prvni cislo: "))
        num2 = float(input("Zadej druhe cislo: "))
        vysledek = num1 / num2
        if num2 == 0:
            print("Nelze delit nulou")
        else:
            print("Vysledek je: ", vysledek)

    elif operace == "5":
        exit()

    else:
        print("Nespravna operace")
        calt()

calt()