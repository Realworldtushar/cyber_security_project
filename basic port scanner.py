import socket as so
s=so.socket(so.AF_INET,so.SOCK_STREAM)
target=input("what you want to scan:")
t_ip=so.gethostbyname(target)
print("starting scan on host:",t_ip)

def port_scan(port):
    try:
        s.connect(t_ip,port)
        return True
    except:
        return False

    port=int(input("Enter the port no you want to scan:"))
    if port_scan(port):
        print("port",port,"is open")
    else:
        print("port",port,"is closed")
