from netmiko import ConnectHandler

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.174",
    "username": "dani",
    "password": "netmiko2026"
}

def vlanok(ssh):
    
    vlan =  ("vlan 10",
             "name Tanulo",
             "vlan 20",
             "name Oktato",
             "vlan 30",
             "name Pedagogus",
             "vlan 100",
             "name Ugyvitel"
            )
    
    ssh.send_config_set(vlan)

def kon_pass(ssh):
    
    try:
        with open("konzol.txt", encoding="utf-8") as fajl:
            szoveg = fajl.readlines()
    except IOError as ex:
        print(ex)
    
    print(szoveg)
    
    lista = []
    
    
    

def kon_pass_csere(ssh):
    
    jel = ("line con 0",
           "pass konJelszo",
          )
    
    ssh.send_config_set(jel)

def int_typ_db(ssh):
    
    interfaces = ssh.send_command("sh run | inc int")
    
    interfaces = interfaces.strip().split('\n')
    
    lista = []
    
    for szo in interfaces:
        lista.append(szo.strip().split(' ')[1])
    
    lista2 = []
    
    for per in lista:
        lista2.append(per.strip().split('/')[0])
    
    lista3 = []
    
    for ut in lista2:
        lista3.append(ut[:-1])
    
    lista4 =  []
    
    for elem in lista3:
        if "Ethernet" in elem:
            lista4.append(elem)
    
    db = 0
    internev = lista4[0]
    
    for i in range(len(lista4)):
        if lista4[i] == internev:
            db += 1
        else:
            internev = lista4[i]
            db = 1
    
    print(internev, db)

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        # 1.f
        
        vlanok(kapcsolat)
        
        print(kapcsolat.send_command("sh vl br"))
        
        # 2.f
        
        kon_pass(kapcsolat)
        
        # 3.f
        
        kon_pass_csere(kapcsolat)
        
        # 4.f
        
        int_typ_db(kapcsolat)

except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")