from Crypto.Cipher import AES
from binascii import unhexlify
import uuid
import os

key = os.urandom(16)

def encrypt(pt):
    nonce = (str(uuid.uuid1())[-16:]).encode()
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ct, tag = cipher.encrypt_and_digest(pt)
    return ct, tag, nonce

def decrypt(ct, tag, nonce):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    pt = cipher.decrypt_and_verify(ct, tag)
    return pt

def read_flag():
    f = open('flag.txt')
    flag = f.read()
    f.close()
    return flag

def get_something():
    pt = os.urandom(16)
    ct, tag, nonce = encrypt(pt)
    
    pt = pt.hex()
    ct = ct.hex()
    tag = tag.hex()
    nonce = nonce.hex()

    print(f'{pt = }')
    print(f'{ct = }')
    print(f'{tag = }')
    print(f'{nonce = }')

def flaggg():
    ct = unhexlify(input('ct: '))
    tag = unhexlify(input('tag: '))
    nonce = unhexlify(input('nonce: '))
    pt = decrypt(ct, tag, nonce)
    if pt.decode() == "adminadminadminn":
        print(read_flag())

def menu():
    print('1. Get something')
    print('2. Flaggg')
    print('3. Exit')
    choice = int(input('> '))
    return choice

def main():
    while True:
        try:
            choice = menu()
            if choice == 1:
                get_something()
            if choice == 2:
                flaggg()
            if choice == 3:
                break
        except:
            print('Something error happened.')
            break
    print('Bye.')

if __name__ == '__main__':
    main()