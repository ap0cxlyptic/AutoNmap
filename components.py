import os
#banner
def banner():
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(":::'###::::'##::::'##:'########::'#######::::::'##::: ##:'##::::'##::::'###::::'########::")
    print("::'## ##::: ##:::: ##:... ##..::'##.... ##::::: ###:: ##: ###::'###:::'## ##::: ##.... ##:")
    print(":'##:. ##:: ##:::: ##:::: ##:::: ##:::: ##::::: ####: ##: ####'####::'##:. ##:: ##:::: ##:")
    print("'##:::. ##: ##:::: ##:::: ##:::: ##:::: ##::::: ## ## ##: ## ### ##:'##:::. ##: ########::")
    print(" #########: ##:::: ##:::: ##:::: ##:::: ##::::: ##. ####: ##. #: ##: #########: ##.....:::")
    print(" ##.... ##: ##:::: ##:::: ##:::: ##:::: ##::::: ##:. ###: ##:.:: ##: ##.... ##: ##::::::::")
    print(" ##:::: ##:. #######::::: ##::::. #######:::::: ##::. ##: ##:::: ##: ##:::: ##: ##::::::::")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("\n")
#the base function 
def xyz():
    print("1. Scan a single IP Address / Domain (Default stealth scan)")
    print("2. Scan specific ports of an IP Address / Domain (Default stealth scan)")
    print("3. Scan top 100 ports / Fast Scan ")
    print("4. Scan all ports of an IP Address / Domain  (Time Consuming) ")
    print("5. Aggressive Scan")
    print("6. TCP SYN and UDP scan for all ports")
    print("7. About Developer ")
    print()
    c=int(input("Enter The Number : "))
    if(c==1):                                                               #single ip or domain scan
        q=input("Enter the IP Address / Domain you want to scan : ")
        os.system("clear")
        print("Scanning 1 IP Address . . . . .")
        x="sudo nmap "+q
        scan(x)
    if(c==2):                                                               #selective ports scan
        q=input("Enter the IP Address / Domain you want to scan : ")
        p=input("Enter the ports you want to scan , seperated by comma for multiple ports : ")
        os.system("clear")
        print("Scanning the specified ports . . . . .")
        x="sudo nmap -p "+p+" "+q
        scan(x)
    if(c==3):                                                               #scanning top ports
        q=input("Enter the IP Address / Domain you want to scan : ")
        os.system("clear")
        print("Scanning top 100 ports . . . . .")
        x="sudo nmap -F "+q
        scan(x)
    if(c==4):                                                               #scanning all ports

        q=input("Enter the IP Address / Domain you want to scan : ")
        os.system("clear")
        print("Scanning all ports . . . . .")
        x="sudo nmap -p- "+q
        scan(x)  
    if(c==5):
        q=input("Enter the IP Address / Domain you want to scan : ")
        os.system("clear")
        print("Running Aggressive scan . . . . .")
        x="sudo nmap -T4 -A "+q
        scan(x) 
    if(c==6):
        q=input("Enter the IP Address / Domain you want to scan : ")
        os.system("clear")
        print("Running Scan . . . . .")
        x="sudo nmap -sS -sU -Pn -p 1-65535 "+q
        scan(x)
    if(c==7):                                                              #about developer
        print("Hello it's me ap0cxlypic ! ")
        print("I am a NASA certified HTML Hacker !!")
        print("Follow me on GitHub for the HTML :D ")
    else:
        print("Wrong Choice Bruh !! Are you dumb stoopid or dumb ??? ")
#function scan
def scan(a):
    os.system(a)
