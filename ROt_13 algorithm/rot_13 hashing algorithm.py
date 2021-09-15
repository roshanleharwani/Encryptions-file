l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
new_str = ""
print()
print("1. Encrypt")
print("2. Decrypt")
option = int(input("Enter the option:"))
str_ = input("Enter the string: ")
lst = list(str_)
if option == 1:
    if type(str_) == str:
        for i in lst:
            k = i.swapcase()
            if i in l1:
                index = l1.index(i)
                new_str += l1[index + 13]
            elif k in l1:
                index = l1.index(k)
                new_str += l1[index + 13].swapcase()
            elif i == " ":
                new_str += "$"
        print()
        print(">>",new_str)
    elif type(str) != str:
        print()
        print("[*] Please enter String format only")
    
        
elif option == 2:
    if type(str_) == str:
        for i in lst:
            k = i.swapcase()
            if i in l1:
                index = l1.index(i)
                new_str += l1[index - 13]
            elif k in l1:
                index = l1.index(k)
                new_str += l1[index - 13].swapcase()
            elif i == "$":
                new_str += " "
        print()
        print(">>",new_str)
    elif type(str) != str:
        print()
        print("[*] Please enter String format only")
    
