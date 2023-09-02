num=int(input("Enter the number \n"))
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("The number lies between 1 -10")
    elif(num > 10 and num <= 20):
        print("the number lies betweeen 10 - 20")
    else:
        print("The number is greater than 20")    
else:
    print("The number is zero ")
