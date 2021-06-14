import speedtest
import colorama
while True:
    colorama.init(autoreset=True)
    test = speedtest.Speedtest()
    print("Getting Servers...")
    test.get_servers()
    print("Getting Best Servers...")
    best = test.get_best_server()
    host = best["sponsor"]
    host = (colorama.Fore.GREEN + f'{host}')
    country = best["country"]
    country = (colorama.Fore.GREEN + f"{country}")
    city = best['name']
    city = (colorama.Fore.GREEN + f'{city}')
    print("[*] Server Found")
    print(f"ISP: {host}, {city} ,{country} ")
    print("Calculating Download Speed...")
    down_speed = test.download()
    print()
    print(f"Download Speed: {down_speed / 1024 /1024: .2f} mb/ps OR {down_speed /1024 /1024 /8: .2f} MB/ps")
    print()
    print("Calculating Upload Speed...")
    up_speed = test.upload()
    print()
    print(f"Upload Speed: {up_speed / 1024 /1024: .2f} mb/ps OR {up_speed /1024 /1024 /8: .2f} MB/ps")
    print()
    choice = input("Do you want to Try again [Y/N]: ")
    if choice == "y" or choice == "Y":
        continue
    elif choice == "n" or choice == "N":
        break
    else:
        print("[*] Invalid Input ")
        break
        
