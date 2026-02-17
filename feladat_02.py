def kon_pass():
    
    try:
        with open("konzol.txt", encoding="utf-8") as fajl:
            szoveg = fajl.readlines()
    except IOError as ex:
        print(ex)
    
    lista = []
    ell = []
    
    for sor in szoveg:
        lista.append(sor.strip().split('\n'))
    
    for i in range(len(lista)):
        if "password" in lista[i]:
            ell.append(lista[i])
        elif lista[i] == "login":
            ell.append(lista[i])

    
    if len(ell) == 2:
        print("Jó a konzol védelem beállítás")
    elif len(ell) == 0:
        print("Nincs jelszó meg login se beállítva")
    else:
        if ell[0] == "login":
            print("Nincs jelszó beállítva")
        else:
            print("Nincs login beállítva")
                
    

kon_pass()