from netmiko import ConnectHandler

Router = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}


try:
    with ConnectHandler(**Router) as kapcsolat:
        
        #1. feladat
        
        uptime = kapcsolat.send_command("sh ver | inc uptime")
        
        reszek = uptime.split(" ")[-2:]
        
        print(f"Az eszköz {reszek[-2]} {reszek[-1]} ideje működik")
        
        #2. feladat
        
        off = kapcsolat.send_command("sh ip in br")
        
        interfesz_adatok = off.split("\n")
        
        print(f"Inaktív interfészek:")
        for interfesz in interfesz_adatok:
            if "down" in interfesz:
                print(f"\t{interfesz.split(" ")[0]}")
        
        #3. feladat
        
        parancsok = ["interface loopback 100",
                     "ip address 10.10.10.10 255.255.255.0",
                     "no shutdown"
                    ]
        
        kapcsolat.send_config_set(parancsok)
        
        #4. feladat
        
        lekerd = kapcsolat.send_command("show interface g0/0")
        
        print(f"A g0/0 interfész EIGRP érték számításban szereplő paramétereinek értékei:")
        for sor in lekerd.split("\n"):
            if "BW" in sor:
                adatok = sor.split(",")
                
                for adat in adatok:
                    if "BW" in adat:
                        print(f"\t Sávszélesség: {adat.split(" ")[-2:]}")
                    elif "DLY" in adat:
                        print(f"\t Késleltetés: {adat.split(" ")[-2:]}")
            elif "reliability" in sor:
                adatok = sor.split(",")
                
                
                for adat in adatok:
                    if "reliability" in adat:
                        print(f"\t Megbízhatóság: {adat.split(" ")[-1]}")
                        print(f"\t Terhelés:", end=" ")
                    elif "load" in adat:
                        print(f"{adat.split(" ")[-1]}", end=" ")
                        
        
        
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")