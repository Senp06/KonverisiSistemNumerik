from lib2to3.pgen2.token import STRING
from os import replace, system


def heading():
    system('cls')
    print('XII RPL7 Senopati Eka Sasura'.center(40))
    print('Konversi Bilangan'.center(40))
    print('                                      ')

def pilihan():
    heading()
    print(' 1. Desimal                        ')
    print(' 2. Biner                          ')
    print(' 3. Oktal                          ')
    print(' 4. Hexadecimal                    ')
    print(' 5. ASCII                          ')
    print(' 6. Exit                           ')
    print('                                      ')
    masukkan = input('Masukkan Menu Konversi Pilihan : ')
    if masukkan == '1':
        desimal()
    elif masukkan == '2':
        biner()
    elif masukkan == '3':
        oktal()
    elif masukkan == '4':
        hexadecimal()
    elif masukkan == '5':
        string_to_ascii()
    elif masukkan == '6':
        keluar()
    else:
        salah()

def salah():
    salah1 = input("Pilihan Tidak Ada ! [Enter]")
    pilihan()

def desimal():
    heading()
    try:
        angka = int(input("Masukkan Bilangan Desimal : "))
    except ValueError:
        error = input("Bilangan Tidak Sesuai! ulangi[Enter]")
        desimal()
    bineri = bin(angka).replace("0b", "")
    oktal = oct(angka).replace("0o", "")
    heks = hex(angka).replace("0x", "")

    print('                                      ')
    print(' Biner : ', bineri)
    print(' Oktal : ', oktal)
    print(' Hexa  : ', heks)
    print('                                      ')
    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        desimal()
    else:
        pilihan()

def biner():
    heading()
    try:
        angka = int(input("Masukkan Bilangan Biner : "), 2)
    except ValueError:
        error = input("Bilangan Tidak Sesuai! ulangi[Enter]")
        biner()
    oktal = oct(angka).replace("0o", "")
    heks = hex(angka).replace("0x", "")

    print('                                      ')
    print(' Decimal : ', angka)
    print(' Oktal   : ', oktal)
    print(' Hexa    : ', heks)
    print('                                      ')
    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        biner()
    else:
        pilihan()

def oktal():
    heading()
    try:
        angka = int(input("Masukkan Bilangan Oktal : "), 8)
    except ValueError:
        error = input("Bilangan Tidak Sesuai! ulangi[Enter]")
        oktal()
    biner = bin(angka).replace("0b", "")
    heks = hex(angka).replace("0x", "")

    print('                                      ')
    print(' Decimal : ', angka)
    print(' biner   : ', biner)
    print(' Hexa    : ', heks)
    print('                                      ')
    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        oktal()
    else:
        pilihan()

def hexadecimal():
    heading()
    try:
        angka = int(input("Masukkan Bilangan Hexa : "), 16)
    except ValueError:
        error = input("Bilangan Tidak Sesuai! ulangi[Enter]")
        hexadecimal()
    biner = bin(angka).replace("0b", "")
    oktal = oct(angka).replace("0o", "")

    print('                                      ')
    print(' Decimal : ', angka)
    print(' Biner   : ', biner)
    print(' Oktal   : ', oktal)
    print('                                      ')

    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        hexadecimal()
    else:
        pilihan()

def string_to_ascii():
    heading()
    try:
        string = input("Masukkan String: ")
    except ValueError:
        error = input("Input tidak valid! Tekan [Enter] untuk mengulangi...")
        string_to_ascii()

    ascii_string= ""

    for character in string:
        ascii_string += str(ord(character)) + " "

    print('                                      ')
    print('| STRING : ', string)
    print('| ASCII : ', ascii_string)
    print('                                      ')
    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        string_to_ascii()
    else:
        pilihan()

def keluar():
    exit()

pilihan()