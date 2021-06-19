import os 
import random
import time 
import colorama

colorama.init(autoreset=True)
level = int(input("Please Set Your Level [1-10]: "))
colors = "VIBGYOR"
simon = " "
counter = 0
print("Get Set GO !!")
time.sleep(2)
os.system("cls")
for i in range(level):
    color = random.choice(colors)
    
    while color == simon[-1] and counter > 1:
        color = random.choice(colors)
    else:
        pass
    simon += color 
    print(colorama.Style.BRIGHT + f"{color}")
    counter += 1
    time.sleep(1.5)
    os.system("cls")
    
repeat = input("Repeat: ")
if repeat == str.strip(simon):
    print()
    print(colorama.Fore.GREEN +"Congrats You have won the game !!")
else:
    print()
    print(colorama.Fore.CYAN +"Oh-oh !! you missed it,try again.")