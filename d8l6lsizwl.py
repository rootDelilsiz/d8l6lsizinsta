#!/usr/bin/env python
# -*- coding: utf-8 -*-
#####################################
#       Delilsiz WORDLİST MAKER     #
#####################################
from sys import exit
from os import name,mkdir,path
import requests
from colorama import Fore
import colorama
import sys
import time
#####################################
colorama.init()


def progress_bar(progress,total,color=Fore.GREEN):
    percent = 100 * (progress / float(total))
    bar = '#' * int(percent) + '-' * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%",end="\r")

numbers = [x * 5 for x in range(2000, 3000)]
result = []


k = requests.get("https://raw.githubusercontent.com/rootDelilsiz/d8l6lsizinsta/main/d8l6lsizwl.py").text
with open("d8l6lsizwl.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == k:
    import d8l6lsizinsta
else:
    print(Fore.MAGENTA + "Güncellemeler Denetleniyor...")
    time.sleep(3)
    print(Fore.YELLOW + "Güncelleme Yapılıyor ")
    import time
    
    with open("d8l6lsizwl.py", "w", encoding="utf-8") as f:
        f.write(k)
        progress_bar(0,len(numbers))
        for i, x in enumerate(numbers):
            result.append(math.factorial(x))
            progress_bar(i + 1,len(numbers))
        print(Fore.GREEN + "\nGüncelleme Tamamlandı!")
        time.sleep(5)
        os.system("cls||clear")
    
class color:
   if name == 'nt':
       PURPLE = ''
       CYAN = ''
       BLUE = ''
       YELLOW = ''
       RED = ''
       ORANGE = ''
       RESET = ''
   else:
       PURPLE = '\033[95m'
       CYAN = '\033[96m'
       BLUE = '\033[94m'
       YELLOW = '\033[93m'
       RED = '\033[91m'
       ORANGE = '\033[33m'
       RESET = '\033[0m'
#####################################
KELIMELER = []
YENI_KELIMELER = []
OZEL_UZUNLUK = []
OZEL_KARAKTER = []
OLASI_SAYILAR = []
UZUNLUK = None
secim = {}
#####################################
def bosmu(value):
    value = str(value)
    if len(value) == 0 or value.isspace():
        return True
    return False

def imza():
    print(color.CYAN,"""
██████╗ ███████╗██╗     ██╗██╗     ███████╗██╗███████╗
██╔══██╗██╔════╝██║     ██║██║     ██╔════╝██║╚══███╔╝
██║  ██║█████╗  ██║     ██║██║     ███████╗██║  ███╔╝ 
██║  ██║██╔══╝  ██║     ██║██║     ╚════██║██║ ███╔╝  
██████╔╝███████╗███████╗██║███████╗███████║██║███████╗
╚═════╝ ╚══════╝╚══════╝╚═╝╚══════╝╚══════╝╚═╝╚══════╝
                
               [+]Delilsiz[+]
                
                """)



    

def sorular():
    print(color.RED,'\n','#'*60)
    print(color.BLUE,'[ YOKSA BOŞ BIRAKINIZ! ]')
    print(' [ ÇOKLU,DEĞERLER,VİRGÜLLE,AYIRARAK,YAZILIR,YANİ,BÖYLE ]\n',color.CYAN)

    global KELIMELER
    global OLASI_SAYILAR

    isim = input(' [+] AD : ')
    KELIMELER.extend(isim.title().split(','))
    KELIMELER.extend(isim.split(','))
    soyad = input(' [+] SOYAD : ')
    KELIMELER.extend(soyad.title().split(','))      
    KELIMELER.extend(soyad.split(','))              
    sehir = input(' [+] ŞEHİR : ')
    KELIMELER.extend(sehir.title().split(','))
    KELIMELER.extend(sehir.split(','))
    lakap = input(' [+] LAKAP : ')
    KELIMELER.extend(lakap.title().split(','))
    KELIMELER.extend(lakap.split(','))
    sanslisayi = input(' [+] ŞANSLI SAYILARI (örn: 1907) : ')
    OLASI_SAYILAR.extend(sanslisayi.split(','))
    ozelisimler = input(' [+] HOŞLANDIGI ŞEYLER (örn: fb,gs,bjk) : ')
    KELIMELER.extend(ozelisimler.title().split(','))
    KELIMELER.extend(ozelisimler.split(','))

    KELIMELER = [i for i in KELIMELER if i]   
    OLASI_SAYILAR = [a for a in OLASI_SAYILAR if len(a) > 2]

def secimler():
    def yanlisdeger(deger):
        if secim[deger] == 'Y' or secim[deger] == 'N':
            pass
        else:
            print(' {}[!]{} Lütfen [Y] veya [N] değerlerini giriniz.'.format(color.RED,color.RESET))
            exit()

    global secim
    secim = {'sayi':'','ozel':'','ters':''} 

    print(color.RED,'#'*60,color.RESET,color.CYAN)

    
    secim['sayi'] = input('\n [?] Sayılar Dahil Edilsin mi ? [0123456789}] [Y/N] : ').capitalize()
    yanlisdeger('sayi')

    
    if secim['sayi'] == 'Y':
        secim['ters'] = input(f'\n [?] Başlarada Sayı Eklensin mi ?  [Y/N]  : ').capitalize()
        yanlisdeger('ters')
    else:
        pass

    
    while True:
        global UZUNLUK
        UZUNLUK = input(' [?] Max. Uzunluğu Giriniz [Boş Bırakabilirsiniz] : ')
        if bosmu(UZUNLUK) == True:
            UZUNLUK = None
            break
        elif UZUNLUK.isalpha() == True:
            print('{} [!]{} Lütfen Sayı Giriniz...{}'.format(color.RED,color.RESET,color.CYAN))
        else:
            UZUNLUK = int(UZUNLUK)
            break

    
    secim['ozel'] = input(f'\n [?] Özel Semboller Dahil Edilsin mi ?  [Y/N]  : ').capitalize()
    yanlisdeger('ozel')

    if secim['ozel'] == 'Y':
        global OZEL_KARAKTER
        OZEL_KARAKTER.extend(input(f'\n {color.YELLOW}[?]{color.CYAN} Hangi Özel Karakterleri Dahil Etmek İstersiniz [ !,?,#,$ ] \n {color.YELLOW}[!]{color.CYAN} Üstteki Gibi Virgülle Yazınız : ').split(','))

def kombinasyon():
    def kombin(loop):
        
        for newpass in eval(loop):
            YENI_KELIMELER.append(newpass)

    if secim['sayi'] == 'Y':
        
        kombin('[word1 + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for sayi in range(1,101)]')

        
        kombin("[word1 + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for sayi in OLASI_SAYILAR ]")

        
        kombin('[word1 + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for sayi in range(2000,2021)]')

        if secim['ozel'] == 'Y':  
            kombin('[word1 + ozel + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for sayi in range(1,101)]')

            
            kombin("[word1 + ozel + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for sayi in OLASI_SAYILAR ]")

            
            kombin('[word1 + ozel + word2 + ozel2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for ozel2 in OZEL_KARAKTER for sayi in range(1,101)]')

            
            kombin("[word1 + ozel + word2 + ozel2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for ozel2 in OZEL_KARAKTER for sayi in OLASI_SAYILAR ]")

            
            kombin('[word1 + word2 + ozel +str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for sayi in range(1,101)]')

            
            kombin('[word1 + ozel + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for sayi in range(2000,2021)]')

        if secim['ters'] == 'Y':
            
            kombin('[str(sayi) + word1 + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for sayi in range(1,101)]')
            
            kombin('[str(sayi) + word1 + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for sayi in range(2000,2021)]')
           
            kombin('[str(sayi) + word1 + word2 for word1 in KELIMELER for word2 in KELIMELER for sayi in range(1,101)]')
            
            kombin('[str(sayi) + word1 + word2 for word1 in KELIMELER for word2 in KELIMELER for sayi in range(2000,2021)]')

            if secim['ozel'] == 'Y':
              
                kombin('[str(sayi) + word1 + ozel + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for sayi in range(1,101)]')

               
                kombin('[str(sayi) + word1 + ozel + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for sayi in range(2000,2021)]')


    if secim['sayi'] == 'N':
        
        kombin('[word1 + word2 for word1 in KELIMELER for word2 in KELIMELER]')

        
        if secim['ozel'] == 'Y':
            kombin('[word1 + ozel + word2 for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER]')



    if UZUNLUK != None:
        for uz in YENI_KELIMELER:
            if len(uz) <= UZUNLUK:
                OZEL_UZUNLUK.append(uz)
    else:
        pass

def kaydet():

    WORDLIST_ISIM = input(f'\n [+] Wordlist İsmi Ne Olsun ? >>> ')

    if bosmu(WORDLIST_ISIM) == True:
        WORDLIST_ISIM = 'passwords'
        pass

    
    with open(f'{path.abspath("Wordlist")}/{WORDLIST_ISIM}.txt', 'w',encoding='utf-8') as dosya:
        if UZUNLUK == None:
            for word in YENI_KELIMELER:
                dosya.write(word + '\n')

            print('\n\n')
            print(color.RED,'#'*40,color.CYAN)
            print(f' [+] {len(YENI_KELIMELER)} Kombinasyon Oluşturuldu.')
        else:
            for word in OZEL_UZUNLUK:
                dosya.write(word + '\n')
            print('\n\n')
            print(color.RED, '#' * 40, color.CYAN)
            print(f' [*] {len(OZEL_UZUNLUK)} Kombinasyon Oluşturuldu.')



    print(color.RED,'#'*40,color.RESET)
    print(f'{color.CYAN} [*] {WORDLIST_ISIM}.txt kaydedildi...')
    print(color.RED,'#'*40,color.RESET)

if __name__ == '__main__':
    if path.exists('Wordlist') == False:
        mkdir('Wordlist')
    else:
        pass



######################################
imza()
sorular()
secimler()
kombinasyon()
kaydet()
######################################
