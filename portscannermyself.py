import socket 
def option1():
    def port_scanner(ipaddress,port):
        for i in range (1,port+1):
            try:
                sock=socket.socket()
                sock.connect((ipaddress,i))
                print("[+] This Port is Open ",i)
                sock.close()
            except:
                pass 
    basicstruct=str(input("[+] Enter The First Three Octet of IP-Address "))
    rangestart=int(input("[+] Enter The Starting Range "))
    rangeend=int(input("[+] Enter The Ending Range "))
    portrange=int(input("[+] Enter Port Range "))
    for i in range (rangestart,rangeend+1):
        main_ipaddress=basicstruct+str(i)
        print("[+] For This IP-Address " + main_ipaddress)
        port_scanner(main_ipaddress,portrange)
        
def option2():
    def portscanner(ip_address,ports):
        for i in range (1,ports+1):
            try :
                sock=socket.socket()
                sock.connect((ip_address,i))
                print("[*] This Port is Open " + str(i))
                sock.close()
            except :
                pass

    noofipaddress=int(input("[+] No Of Ip Address To Be Scanned"))
    for x in range (1,noofipaddress+1):
        ip_address=str(input("[+] Enter IP Address "))
        noofports=int(input("[+] Enter No Of Ports Wanted To Scan "))
        print ("[+] For This Ip Address -> " + ip_address)
        portscanner(ip_address,noofports)
def option3():

    def port_scanner(ipaddress,port):
        try:
            sock=socket.socket()
            sock.connect((ipaddress,port))
            print("[+] This Port is Open "+str(port))
            sock.close()
        except:
            print("[+] This Port is Closed "+str(port))



    basicstruct=str(input("[+] Enter The First Three Octet of IP-Address "))
    rangestart=int(input("[+] Enter The Starting Range "))
    rangeend=int(input("[+] Enter The Ending Range "))
    portrange=int(input("[+] Enter Port No  "))
    for i in range (rangestart,rangeend+1):
        main_ipaddress=basicstruct+str(i)
        port_scanner(main_ipaddress,portrange)
        print("[+] For This IP-Address " + main_ipaddress)



print("[+] Options ")
print("1-> For Scanning Range of IP-Address")
print("2-> For Scanning Different IP-Address")
print("3-> For Scanning Particular Port Of An IP-Address")
option=int(input("Enter Your Option -> "))
#Switch Case Lagana Haje 
if (option==1):
    option1()
elif (option==2):
    option2()
elif (option==3):
    option3()
elif (option>3) :
    print("Re-run The Program ")


        


