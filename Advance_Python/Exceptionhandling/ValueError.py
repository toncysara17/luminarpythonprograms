#value
try:
    num=int(input("enter num"))
    print(num)
except:
    print("enter a int value")
finally:
    print("inside finally")