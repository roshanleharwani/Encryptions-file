from cryptography.fernet import Fernet
import colorama
import os
colorama.init(autoreset=True)

def options():
    yellow = colorama.Fore.YELLOW
    style = colorama.Style.BRIGHT
    print(style +yellow + "Options")
    print(style +yellow + "1.Genrate Key")
    print(style +yellow + "2.Encrypt String")
    print(style +yellow + "3.Decrypt String")
    print(style +yellow + "4.Encrypt File")
    print(style +yellow + "5.Decrypt File")
    print(style +yellow + "0.Exit")
print()
while True:
    try:
        options()
        print()
        choice = int(input(">> "))
        if choice == 0:
            break
        elif choice == 1:
            key = (Fernet.generate_key()).decode()
            print(colorama.Fore.GREEN + "[*] KEY GENRATED SUCCESSFULLY")
            print()
            print(f"key >> {key}")
            print()
            try:
                choose = (input(r"Do you want to save this KEY [Y\N]: "))
                if choose == "Y" or choose == "y":
                    key_file = open("key.key", "wb")
                    key_file.write(key)
                    print()
                    print(colorama.Fore.GREEN+ '[*] File Saved Successfully')
                    print()
                    continue
                elif choose == "N" or choose == "n":
                    continue
            except :
                print(colorama.Fore.RED+"[*] Invalid Input !!")
                continue
        elif choice == 2:
            string = input("Enter the string:" )
            string = string.encode()
            try :
                choose = input(r"Do You Have any KEY [Y\N]: ")
                if choose == "Y" or choose == "y":
                    key = input("Enter the KEY [Make sure that the key in string format not in bytes]:")
                    key = key.encode()
                elif choose == "N" or choose == "n":
                    key = Fernet.generate_key()
                    print()
                    print(colorama.Fore.GREEN+"KEY GENRATED SUCCESSFULLY")
                    print()
                    print(f"KEY >> {key.decode()}")
                    print()
                    try:
                        choose = (input(r"Do you want to save this KEY [Y\N]: "))
                        if choose == "Y" or choose == "y":
                            key_file = open("key.key", "wb")
                            key_file.write(key)
                            print()
                            print(colorama.Fore.GREEN+ '[*] File Saved Successfully')
                            print()
                        elif choose == "N" or choose == "n":
                            pass
                    except :
                        pass
            except:
                print()
                print(colorama.Fore.RED+"[*] Invalid Input !!")
                break
            encrypted_string = (Fernet(key).encrypt(string)).decode()
            print()
            print(f"Encrypted String >> {encrypted_string}")
            print()
        elif choice == 3:
            try :
                encrypted_string = (input("Enter the Encrypted String: ")).encode()
                key = (input("Enter the KEY: ")).encode()
                decrypted_string = (Fernet(key).decrypt(encrypted_string)).decode()
                print()
                print(f"Decrypted String >> {decrypted_string}")
                break
            except:
                print()
                print("[*] Please check your key and hash")
                print()
                continue
        elif choice == 4:
            try :
                file_path = input("Enter the path of the file with the file name: ")
                check = lambda x:os.path.isfile(x)
                if check(file_path) == True:
                    file = open(file_path,"rb")
                    data = file.read()
                    choose = input(r"Do you have any KEY [Y\N]: ")
                    if choose == "y" or choose == "Y":
                        key = (input("Enter the KEY [Make sure that the key in string format not in bytes]: ")).encode()
                        print()
                        encrypted_data = Fernet(key).encrypt(data)
                        file_name = input("Enter the name of encrypted file: ")
                        encrypted_file = open(file_name,'wb')
                        encrypted_file.write(encrypted_data)
                        print()
                        print(colorama.Fore.GREEN +"New File saved successfully")
                    elif choose == "N" or choose == "n":
                        key = Fernet.generate_key()
                        print()
                        print(colorama.Fore.GREEN + "[*] KEY GENRATED SUCCESSFULLY")
                        print()
                        print(f"key >> {(key).decode()}")
                        print()
                        encrypted_data = Fernet(key).encrypt(data)
                        file_name = input("Enter the name of encrypted file: ")
                        encrypted_file = open(file_name,'wb')
                        encrypted_file.write(encrypted_data)
                        print()
                        print(colorama.Fore.GREEN +"[*] New File saved successfully")
                        print()
                    else:
                        print()
                        print(colorama.Fore.RED +"[*] Invalid input")
                        continue
            except :
                print(colorama.Fore.RED+"[*] Invalid Input !!")
                print()
                continue
        elif choice == 5:
            file_path = input("Enter the path of the file with the file name: ")
            check = lambda x: os.path.isfile(x)
            if check(file_path) == True:

                print()
                key = (input("Enter the KEY [Make sure that the key in string format not in bytes]: ")).encode()
                encrypted_file = open(file_path,'rb')
                encrypted_data = encrypted_file.read()
                decrypted_data = Fernet(key).decrypt(encrypted_data)
                print()
                file_name = input("Enter the name of new file: ")
                print()
                decrypted_file = open(file_name,'wb')
                decrypted_file.write(decrypted_data)
                print(colorama.Fore.GREEN +"[*] New File saved successfully")
                print()
            else:
                print()
                print("[*] Please check the file path and try again !!")
                print()
                continue
            
    except:
        print()
        print("[*] Invalid Input")
        print()
        continue
