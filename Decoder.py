from cryptography.fernet import Fernet
encrypted_text = input ("[*] Enter the encrypted text you want to Decrypt: ")
key_file = input("[*] Enter the path of the key with the file name: ")
try :
    file = open(key_file,'rb')
    key = file.read()
    f = Fernet(key)
    decrypted_text = f.decrypt( encrypted_text.encode())
    decrypted_text = decrypted_text.decode()
    print()
    print(f"Your Decrypted text:\n {decrypted_text}")
except FileNotFoundError:
    print()
    print("Key File Not found !!")
