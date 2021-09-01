num = int(input("Enter any Non-negative Integer: "))
product = 1
def factorial(num,product):
    if num == 0:
        return 1
    elif num > 0:
        for i in range(1,num+1):
            product *= i
        print()
        return product
    else:
        print()
        print (r"Invalid Input: [Enter any Postive Integer]")
        print()
fact = factorial(num,product)
if num >=0:
    print("factorial of",num,"is",fact)