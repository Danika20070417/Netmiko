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

        passwu = kapcsolat.send_command("show run | section username")
        passwe = kapcsolat.send_command("show run | sec enable")
        passwc = kapcsolat.send_command("show run | sec line con")
        passwv = kapcsolat.send_command("show run | sec line vty")
        
        passwe = passwu.strip().split()[-1]
        if len(passwe) < 8:
            jelszo = input("Adj meg egy jelszót ami minimum 8 karakter hosszú")
            while len(jelszo) < 8:
                jelszo = input("Adj meg egy jelszót ami minimum 8 karakter hosszú")
        
        
        '''
        tftp_ip = input("Add meg a szerver IP-címét:")
        fajlnev = input("Mentendő konfig fájl neve:")
        
        output = kapcsolat.send_multiline_timing(["copy run tftp", tftp_ip, fajlnev])
        '''
        

except Exception as ex:
    print(f"Hiba: {ex}")