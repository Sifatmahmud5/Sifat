#coding=utf-8
import sys,time
from platform import uname
from os import path,system
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools');time.sleep(1)
else:
    print('033[1;31mSorry System not support this tools');sys.exit()
    
banner=("""\033[1;37m    :'######::'####:'########::::'###::::'########:
'##... ##:. ##:: ##.....::::'## ##:::... ##..::
 ##:::..::: ##:: ##::::::::'##:. ##::::: ##::::
. ######::: ##:: ######:::'##:::. ##:::: ##::::
:..... ##:: ##:: ##...:::: #########:::: ##::::
'##::: ##:: ##:: ##::::::: ##.... ##:::: ##::::
. ######::'####: ##::::::: ##:::: ##:::: ##::::
:......:::....::..::::::::..:::::..:::::..:::::
[+]════════════════════════════════════════
[+] Author    : SIFAT MAHMUD 
[+] Github    : Sifatmahmud5
[+] Facebook  : Sifat Mahmud 
[+] Tool Type : Premium
[+] Version   : 1.3.3
\033[1;37m[+]════════════════════════════════════════""")

def main():
    if path.isfile():
    system('clear')
    print(banner)
    print('[1] Version : 1.3.3\n[2] Version : 1.3.2\n\033[1;37m[+]════════════════════════════════════════')
    vs=input('[•] Choice : ')
    if vs in ['1','01']:
        if path.isfile("AKING64.so"):
            import AKING64
        else:
            system("curl -L https://raw.githubusercontent.com/Sifat/Data/main/SIFAT.so -o SIFAT.so")
            import SIFAT
    elif vs in ['2','02']:
        if path.isfile("SIFAT.so"):
            import AKING
        else:
            system("curl -L https://raw.githubusercontent.com/Sifatmahmud5/Data/main/SIFAT.so -o SIFAT.so")
            import SIFAT
    else:
        if path.isfile("SIFAT.so"):
            import SIFAT
        else:
            system("curl -L https://raw.githubusercontent.com/Sifatmahmud5/Data/main/SIFAT.so -o SIFAT.so")
            import SIFAT
main()