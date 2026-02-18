from netmiko import ConnectHandler

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.174",
    "username": "dani",
    "password": "netmiko2026"
}

try:
    with ConnectHandler(**kapcsolo) as kapcsolat:
        
        tftp_ip = input("Add meg a szerver IP-címét:")
        fajlnev = input("Mentendő konfig fájl neve:")
        
        output = kapcsolat.send_multiline_timing(["copy run tftp", tftp_ip, fajlnev])
        
        print(output)

except Exception as ex:
    print(f"Hiba: {ex}")