from netmiko import ConnectHandler

def netmiko_show_version():

    try:
        with ConnectHandler(**kapcsolo) as kapcsolat:
            output = kapcsolat.send_command("show version")
    except Exception() as ex:
        print(f"Hiba: {ex}")

def fajlbeolvasas():
    try:
        with open("show_version.txt", encoding="utf-8") as fajl:
            szoveg = fajl.read()
        
    except IOError as ex:
        print(f"IO hiba: {ex}")

    return szoveg


# Hány Ethernet interface van a kapcsolón?



###############################################################################
#    PROGRAM
###############################################################################

output = ""

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.115",
    "username": "dani",
    "password": "netmiko2026"
}

#netmiko_show_version(kapcsolo)
#print(output)

verzio_info = fajlbeolvasas()

print(verzio_info)