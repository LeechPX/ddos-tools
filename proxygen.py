# Tools originally by PhynX
# -*- coding: utf-8 -*-

import os,sys,time,random

def ponik():
    global ttlgen
    if sys.platform.startswith("linux"):
        os.system('clear')
    if sys.platform.startswith("freebsd"):
        os.system('clear')
    if sys.platform.startswith("Win32"):
        os.system('cls')
    else:
        os.system('clear')
    ttlgen = int(input('How many Proxy? [1-Unlimited] : '))
    if ttlgen == '':
        ponik()
    elif ttlgen >= 100000:
        huh = str(input('\nAre you sure want generate ' + str(ttlgen) + 'Proxy? : '))
        if huh == "":
           gen()
        else:
            ponik()
    else:
        if sys.platform.startswith("linux"):
            os.system('clear')
        if sys.platform.startswith("freebsd"):
            os.system('clear')
        if sys.platform.startswith("Win32"):
            os.system('cls')
        else:
            os.system('clear')
        gen()
        
def gen():
    global i, startgen
    startgen = True
    file = open('proxies.txt', 'wb')
    i = 0
    while startgen:
        for x in range(ttlgen):
            try:
                randr = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + ":" + str(random.choice(['80', '1080', '3128', '8080', '8081']))
                file.write(str.encode(randr + "\n"))
                i+=1
                print(str(i) + " Proxy Generated...\r".format(i), end='')
            except KeyboardInterrupt:
                startgen = False
                if sys.platform.startswith("linux"):
                    os.system('clear')
                if sys.platform.startswith("freebsd"):
                    os.system('clear')
                if sys.platform.startswith("Win32"):
                    os.system('cls')
                else:
                    os.system('clear')
                print(str(i) + ' Proxies was Generated.\n')
                surtod.close()
                break
            except:
                if sys.platform.startswith("linux"):
                    os.system('clear')
                if sys.platform.startswith("freebsd"):
                    os.system('clear')
                if sys.platform.startswith("Win32"):
                    os.system('cls')
                else:
                    os.system('clear')
                break
                continue
                sys.stdout.flush()
                print(str(i) + " Proxies Was Generated.")
                file.close()
        else:
            sys.stdout.flush()
            print(str(i) + " Proxies Was Generated.")
            break
            continue
        
if __name__ == '__main__':
    ponik()
