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
    
    pass

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
        
    print(teszt2)

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        # 1.f
        
        vlanok(kapcsolat)
        
        print(kapcsolat.send_command("sh vl br"))
        
        # 2.f
        
        
        # 3.f
        
        kon_pass_csere(kapcsolat)
        
        # 4.f
        
        int_typ_db(kapcsolat)

except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")