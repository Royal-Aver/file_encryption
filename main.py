import pyAesCrypt
from pathlib import Path

file_encrypt = Path('files/test.txt')
file_decrypt = Path('files/test.aes')

password = input('Enter a password to encrypt/decrypt the file: ')

# encrypt
pyAesCrypt.encryptFile(f'{file_encrypt}', f'files/{file_encrypt.stem}.aes', password)

#decrypt
pyAesCrypt.decryptFile(f'{file_decrypt}', f'files/{file_decrypt.stem}.txt', password)
