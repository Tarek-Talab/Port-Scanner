import socket
import time
from termcolor import colored
import colorama
import pyfiglet
colorama.init()
banner = pyfiglet.figlet_format("Port Scanner")
print(banner)

giris = "Merhaba şimdi sizden IP address ile port aralığı girmenizi isticez ona göre bilgiler giriniz."
for harf in giris:
    print(harf,end="",flush=True)
    time.sleep(0.02)
print()

def port_scanner(ip_address,port_start,port_end):
    for port in range(port_start,port_end + 1):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.001)
        sock.connect_ex((ip_address,port))
        try:
            service_name = socket.getservbyport(port,"tcp")
        except OSError:
            service_name = "Bilinmiyor"
        if service_name == "Bilinmiyor":
            print(f"Port No : {port} | Service: {service_name}")
        else:
            print(f"Port No: {colored(port,"red")} | Service: {colored(service_name,"red")}")
        sock.close()
        

ip_address = input(colored("[+] IP:","red"))
port_start = int(input(colored("[+] Port BaşlangıÇ sınırı: ","green")))
port_end = int(input(colored("[+] Port bitiş sınırı: ","green")))
port_scanner(ip_address,port_start,port_end)

