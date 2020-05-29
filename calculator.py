#
import time 
import os ; os.system('clear') ; os.system('sleep 1')
print('''\033[94m
===================================
< Kalkulator V.1 >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
                Coded By : Riss.ID
                Thnks    : #Sky.ID And You :D 
====================================
''')
print('\033[91m\t#.::Kalkulator::.V.1.::.#')
print('\033[92m1. Pertambahan  [+]')
print('\033[92m2. Pengurangan  [-]')
print('\033[92m3. Perkalian    [X]')
print('\033[92m4. Pembagian    [:]')
print('\033[92m5. Perpangkatan [**]')
print('\033[93m6. Keluar')
def tambah():
    print('\033[95mPertambahan [+]')
    kk = int(input('Input Pertama ~> '))
    ko = int(input('Input Kedua   ~> '))
    os.system('sleep 1')
    out = kk+ko
    print('Hasil : ',out)

def kurang():
    print('\033[96mPengurangan [-]')
    ki = int(input('Input Pertama ~> '))
    ku = int(input('Input Kedua   ~> '))
    os.system('sleep 1')
    out = ki-ku
    print('Hasil : ',out)

def kali():
    print('\033[97mPerkalian [x]]')
    kh = int(input('Input Pertama ~> '))
    kj = int(input('Input Kedua   ~> '))
    os.system('sleep 1')
    out = kh*kj 
    print('Hasil : ',out)
def bagi():
    print('\033[98mPembagian [:]')
    kp = int(input('Input Pertama ~> '))
    kb = int(input('Input kedua   ~> '))
    os.system('sleep 1')
    out = kp/kb
    print('Hasil : ',out)
def pangkat():
    print('\033[93mPemangkatan [**]')
    xc = int(input('Input Pertama ~> '))
    cx = int(input('Input Kedua   ~> '))
    os.system('sleep 1')
    out = xc**cx 
    print('Hasil : ',out)

def keluar():
    print('Waitttt')
    os.system('sleep 1')
    os.system('exit')

select = str(input('root@user ~ # '))
if select in ['1','01']:
    tambah()
elif select in ['2','02']:
    kurang()
elif select in ['3','03']:
    kali()
elif select in ['4','04']:
    bagi()
elif select in ['5','05']:
    pangkat()
if select in ['6','06']:
    keluar()
else:
    print('===============')

