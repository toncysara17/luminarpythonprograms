#using exception handling
try:
    num1 =int( input("Enter value"))
    print(num1)
except:
    print("please enter int value")
finally:
    print("inside finally")