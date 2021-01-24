#!/usr/bin/python3

import sys, time, colorama
from colorama import Fore, Style

def main():

    # Print banner
    banner()

    # Colored text
    colorama.init(autoreset=True)

    if len(sys.argv) <= 4:
        print(Fore.RED + Style.BRIGHT + '[!] Wrong usage...')
        print(Fore.RED + Style.BRIGHT + '[!] Sample usage - python3 main.py -e \'Hello World\' \'Testing\'')
    else:
        print(Fore.GREEN + '[+] Starting up Vigenere Cipher\n')
        time.sleep(2.5)

        if sys.argv[1] == '-e' or sys.argv[1] == '--encrypt':
            # -e for encryption
            print(Fore.GREEN + '[+] Beginning encryption process')
            time.sleep(1)

            print(Fore.GREEN + '[+] Encryption completed:\n')
            print(Fore.YELLOW + encryption(sys.argv[2], sys.argv[3]))
        elif sys.argv[1] == '-d' or sys.argv[1] == '--decrypt':
            # -d for decryption
            print(Fore.GREEN + '[+] Beginning decryption process')
            time.sleep(1)

            print(Fore.GREEN + '[+] Decryption completed:\n')
            print(Fore.YELLOW + decryption(sys.argv[2], sys.argv[3]))
        else:
            print(Fore.RED + Style.BRIGHT + '[!] Wrong usage...')


def banner():
    banner_ascii = '''
+-----------------------------------------------------------------------------+
|  __     ___                                   ____ _       _                |
|  \ \   / (_) __ _  ___ _ __   ___ _ __ ___   / ___(_)_ __ | |__   ___ _ __  |
|   \ \ / /| |/ _` |/ _ \ '_ \ / _ \ '__/ _ \ | |   | | '_ \| '_ \ / _ \ '__| |
|    \ V / | | (_| |  __/ | | |  __/ | |  __/ | |___| | |_) | | | |  __/ |    |
|     \_/  |_|\__, |\___|_| |_|\___|_|  \___|  \____|_| .__/|_| |_|\___|_|    |
|             |___/                                   |_|                     |
|                                                                             |
+-----------------------------------------------------------------------------+
    '''
    print(Fore.WHITE + banner_ascii)

def encryption(plain_text, key):

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Encrypted plain text
    cipher_text = ''

    # Converting plain_text to uppercase
    plain_text = plain_text.upper()

    # Position of character in the key
    key_character_pos = 0

    for plain_character in plain_text:
        if not plain_character.isalpha():
            # Append without encrypting
            cipher_text += plain_character
        else:
            # Getting new character
            position = alpha.find(plain_character) + alpha.find(key[key_character_pos % len(key)].upper())
            cipher_text += alpha[position % len(alpha)]

            # Incrementing key position
            key_character_pos += 1

    return cipher_text

def decryption(cipher_text, key):

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Decrypted cipher text
    plain_text = ''

    # Converting cipher_text to uppercase
    cipher_text = cipher_text.upper()

    # Position of character in the key
    key_character_pos = 0

    for cipher_character in cipher_text:
        if not cipher_character.isalpha():
            # Append without decrypting
            plain_text += cipher_character
        else:
            # Getting new character
            position = abs(alpha.find(cipher_character) - alpha.find(key[key_character_pos % len(key)].upper()))
            plain_text += alpha[position % len(alpha)]
            print(alpha[position % len(alpha)])

            # Incrementing key position
            key_character_pos += 1

    return plain_text

if __name__ == '__main__':
    main()
