from netmiko import ConnectHandler
from getpass import getpass

router = {
    "device_type": "cisco_ios",
    "host": "192.168.40.174",
    "username": "dani",
    "password": getpass()
}

try:
    with ConnectHandler(**router) as kapcsolat:
        
        szom = kapcsolat.send_command("sh ip ospf neig")
        szom = szom.strip().split('\n')[1:]
        
        print(f"{len(szom)} szomszéd van")
        
        valt = kapcsolat.send_command("sh run | inc ospf")
        
        ospf = [valt,
                "network 172.162.174.12 0.0.0.3 area 0"
                ]
        
        kapcsolat.send_config_set(ospf)
        
        szel = int(input("Add meg a referencia sávszélességet [100, 1000, 10000]:"))
        
        while szel != 100 and szel != 1000 and szel != 10000:
            szel = int(input("Add meg a referencia sávszélességet [100, 1000, 10000]:"))
        
        szel = str(szel)
        
        ref = [valt,
                f"auto-cost refer {szel}"
               ]
        
        kapcsolat.send_config_set(ref)
        
        id = input("Adj meg egy router azonosítót:")
        
        while id == "" or id.isalpha() or len(id.strip().split('.')) != 4:
            id = input("Adj meg egy router azonosítót:")
            
        hey = id.strip().split('.')
        
        while not(hey[0].isdigit() and hey[1].isdigit() and hey[2].isdigit() and hey[3].isdigit()):
            id = input("Adj meg egy router azonosítót:")
            hey = id.strip().split('.')
        
        hey2 = id.strip().split('.')
        
        while int(hey2[0]) and int(hey2[1]) and int(hey2[2]) and int(hey2[3]) > 255:
            id = input("Adj meg egy router azonosítót:")
            hey2 = id.strip().split('.')
        
        while int(hey2[0]) and int(hey2[1]) and int(hey2[2]) and int(hey2[3]) < 0:
            id = input("Adj meg egy router azonosítót:")
            hey2 = id.strip().split('.')
        
        rou_id = [valt,
                  f"router-id {id}"
                 ]
        
        kapcsolat.send_config_set(rou_id)
        
             
        
            
        
except Exception as ex:
    print(ex)