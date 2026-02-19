from netmiko import ConnectHandler

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.174",
    "username": "dani",
    "password": "netmiko2026"
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
                    
        user = kapcsolat.send_command("sh run | inc username")
        user1 = user.strip().split(" ")
        user = user.strip().split('\n')
        print(user, user1)
        
        for i in user:
            user = i.split(' ')[-1]
        print(user)
            
        if len(user1[-1]) < 8:
            ujjelszo4 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                    
            while len(ujjelszo4) < 8:
                ujjelszo4 = input("Adj meg egy legalább 8 karakterből álló jelszót: ")
                    
                    
                    
            kapcsolat.send_config_set(f"{ujjelszo4}")
        
        '''
        tftp_ip = input("Add meg a szerver IP-címét:")
        fajlnev = input("Mentendő konfig fájl neve:")
        
        output = kapcsolat.send_multiline_timing(["copy run tftp", tftp_ip, fajlnev])
        '''
        

except Exception as ex:
    print(f"Hiba: {ex}")