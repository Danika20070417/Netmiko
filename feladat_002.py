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
    '''
    line= ""
    
    line = ssh.send_command("sh run | section line con 0")
    
    line = line.strip().split('\n')
    
    lista = []
    
    for i in range(1, len(line)):
        lista.append(line[i].strip().split(' '))
        
    print(lista)
    
    for i in range(len(lista)):
        if lista[i] == "password":
            if lista[i] == "login":
                print("Konzol jelszó és hitelesítés beállítása OK!")
            else:
                print("Nincs be állítva a login parancs így nem kéri a jelszót bejelentkezéskor")
        else:
            print("Nincs megadva jelszó")
            
    '''

def kon_pass_csere(ssh):
    
    jel = ("line con 0",
           "pass konJelszo",
          )
    
    ssh.send_config_set(jel)

def int_typ_db(ssh):
    
    interfaces = ""
    
    interfaces = ssh.send_command("sh run | inc int")
    
    teszt = interfaces.strip().split(' ')
    
    teszt2 = []
    
    for i in range(len(teszt)):
        teszt2.append(teszt[i].strip().split('\n')[0])
    
    dbg = 0
    dbf = 0
    
    for i in range(len(teszt2)):
        if "GigabitEthernet" in teszt2[i]:
            dbg += 1
        if "FastEthernet" in teszt2[i]:
            dbf += 1
    
    print(f"{dbg} GigabitEthernet interfész van")
    print(f"{dbf} FastEthernet interfész van")

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