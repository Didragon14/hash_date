# -*- coding: utf-8 -*-

import hashlib

def date_hash_md5():
    date_input = input('Введите хэшируемые данные(md5): ')
    
    a = hashlib.md5(date_input.encode())
    print(a.hexdigest())


def date_hash_sha1():
    date_input = input('Введите хэшируемые данные(sha1): ')
    a = hashlib.sha1(date_input.encode())
    print(a.hexdigest())


def date_hash_sha224():
    date_input = input('Введите хэшируемые данные(sha224): ')
    
    a = hashlib.sha224(date_input.encode())
    print(a.hexdigest())


def date_hash_sha256():
    date_input = input('Введите хэшируемые данные(sha226): ')
    
    a = hashlib.sha256(date_input.encode())
    print(a.hexdigest())


def date_hash_sha384():
    date_input = input('Введите хэшируемые данные(sha384): ')
    
    a = hashlib.sha384(date_input.encode())
    print(a.hexdigest)


def date_hash_sha512():
    date_input = input('Введите хэшируемые данные(sha512): ')
    
    a = hashlib.sha512(date_input.encode())
    print(a.hexdigest())



def cycle():
    while True:
        ans = input('Введите тип хэширования(md5, sha1, sha224, sha256, sha384, sha512), выход на (q): ')

        if ans == 'q':
            print('До скорого хозяин!')
            break

        elif ans == 'md5':
            date_hash_md5()
            print()

        elif ans == 'sha1':
            date_hash_sha1()
            print()

        elif ans == 'sha224':
            date_hash_sha224()
            print()

        elif ans == 'sha256':
            date_hash_sha256()
            print()

        elif ans == 'sha384':
            date_hash_sha384()
            print()

        elif ans == 'sha512':
            date_hash_sha512()
            print()

        else:
            print('Да ты заебал))')
            print()

cycle()