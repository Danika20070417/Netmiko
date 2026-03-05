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
        
        #F1
        
        roas = ["int g0/0/1.11",
                "encap dot1q 11",
                "ip add 192.168.11.11 255.255.255.0",
                "no shut",
                "int g0/0/1.13",
                "encap dot1q 13",
                "ip add 192.168.13.13 255.255.254.0",
                "no shut",
                "int g0/0/1",
                "no shut"
                ]
        
        kapcsolat.send_config_set(roas)
        
        #F2
        
        vazon = input("Adj meg egy vlan azonosítót [1-1005]:")
        
        while vazon == "" or not vazon.isdigit() or int(vazon) <= 1 or int(vazon) > 1005 or int(vazon) == 11 or int(vazon) == 13:
            vazon = input("Adj meg egy vlan azonosítót [1-1005]:")
        
        ip = input("Adj meg egy IP címet:")
        maszk = input("Add meg az IP címhez a maszkot:")
        
        mas_roas = [f"int g0/0/1.{vazon}",
                    f"encap dot1q {vazon}",
                    f"ip add {ip} {maszk}",
                    "no shut"
                    ]
        
        kapcsolat.send_config_set(mas_roas)


        #F3
        '''
        tftp_ip = input("Add meg a szerver IP-címét:")
        fajlnev = input("Mentendő konfig fájl neve:")
        
        output = kapcsolat.send_multiline_timing(["copy run tftp", tftp_ip, fajlnev])
        '''
        #F4
        
        valami = kapcsolat.send_command("show run | sec interface").strip().split('\n')
        alint = []
        
        for i in range(len(valami)):
            if "interface" in valami[i] and "." in valami[i]:
                alint.append(valami[i].strip().split(' ')[-1])
        
        for i in range(len(alint)):
            mas = kapcsolat.send_command(f"show run | sec {alint[i]}")
        
            print(mas)
        
except Exception as ex:
    print(ex)