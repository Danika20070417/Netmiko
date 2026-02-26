from netmiko import ConnectHandler
from getpass import getpass

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.174",
    "username": "dani",
    "password": getpass()
}

try:
    with ConnectHandler(**kapcsolo) as kapcsolat:
        
        kapcsolat.send_config_set("login block-for 600 attempts 3 within 60")

        passwe = kapcsolat.send_command("show run | sec enable")
        
        passwe = passwe.strip().split()[-1]
        if len(passwe) < 8:
            jelszo = input("Adj meg egy jelszót ami minimum 8 karakter hosszú:")
            
            while len(jelszo) < 8:
                jelszo = input("Adj meg egy jelszót ami minimum 8 karakter hosszú:")
            kapcsolat.send_config_set(f"enable password {jelszo}")
        
        konzol = kapcsolat.send_command("sh run | section line con")
        konzol = konzol.split("\n")
        for i in konzol:
            if i.strip().startswith('password'):
                if len(i.split(' ')[-1]) < 8:
                    ujjelszo2 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                
                    while len(ujjelszo2) < 8:
                        ujjelszo2 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                
                    kapcsolat.send_config_set(["line con 0" , f"password {ujjelszo2}"])
        
        vty = kapcsolat.send_command("sh run | section line vty 0")
        vty = vty.split("\n")
        for i in vty:
            if i.strip().startswith('password'):
                if len(i.split(' ')[-1]) < 8:
                    ujjelszo3 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                
                    while len(ujjelszo3) < 8:
                        ujjelszo3 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                
                    kapcsolat.send_config_set(["line vty 0 15" , f"password {ujjelszo3}"])
                    
        ena = kapcsolat.send_command("show run")
        if "username" in ena:
            val = kapcsolat.send_command("show run | include username").split('\n')
            print(val)
            
            for felh in val:
                if len(felh.split(' ')[-1]) < 8:
                    print(f"A {felh.split(' ')[1]} felhasználó jelszava nem megfelelő hosszúságú.")
                    usejelszo = input("Adj meg egy legalább 8 karakter hosszú jelszót: ")
                    while len(usejelszo) < 8:
                        usejelszo = input("Adj meg egy legalább 8 KARAKTER HOSSZÚ jelszót!: ")
                    osszerakott = ''
                    for szo in felh.split(' ')[:-2]:
                        osszerakott += szo + ' '
                    kapcsolat.send_config_set(f"{osszerakott}{usejelszo}")
                    print("A jelszó beállítása megtörtént.(°_,°)")
        
        
        tftp_ip = input("Add meg a szerver IP-címét:")
        fajlnev = input("Mentendő konfig fájl neve:")
        
        output = kapcsolat.send_multiline_timing(["copy run tftp", tftp_ip, fajlnev])
        
        
        cli_out = kapcsolat.check_enable_mode()
        print(f"{cli_out}")

except Exception as ex:
    print(f"Hiba: {ex}")