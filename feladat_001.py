from netmiko import ConnectHandler

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.174",
    "username": "dani",
    "password": "netmiko2026"
}


def mentes(ssh):
    ssh.save_config()


def set_enable_pwd(ssh):
    jelszo = input("Add meg az új enable jelszót!: ")
    ssh.send_config_set(f"enable password {jelszo}")

def ser_pass_enc(ssh):
    ssh.send_config_set("service password-encryption")

def banner(ssh):
    ssh.send_config_set("banner motd -Jogosulatlanul bejelentkezni tilos!-")
    
def rapid_pvst(ssh):
    ssh.send_config_set("spanning-tree mode rapid-pvst")

def ment_fajl(ssh):
    pass
    





# ---------------------------
# PROGRAM
# ---------------------------

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        # 2.f
        print(kapcsolat.find_prompt())
        
        #3.f
        mentes(kapcsolat)
        
        valasz = kapcsolat.send_command("show startup-config")
        if "not present" not in valasz:
            print("A mentés sikerült!")
        else:
            print("A mentés NEM sikerült!")
            
        #4.f
        set_enable_pwd(kapcsolat)
        
        print(kapcsolat.send_command("show running-config | include enable"))
        
        #5.f
        ser_pass_enc(kapcsolat)
        
        #6.f
        banner(kapcsolat)
        
        print(kapcsolat.send_command("show running-config | include password"))
        print(kapcsolat.send_command("show running-config | include secret"))
        
        #7.f
        rapid_pvst(kapcsolat)
        
        #8.f
        ment_fajl(kapcsolat)
        

except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")