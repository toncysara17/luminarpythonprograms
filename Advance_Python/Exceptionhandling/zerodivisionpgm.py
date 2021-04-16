#Advanced Python
#Exception Handling
# zero division pgm
num1=int(input("enter num1"))      #5      #5
num2=int(input("enter num2"))      #5      #0
                            #c=a/b
                            #print(c)
try:
    res=num1/num2
    print("res is",res)
except:
    print("exception occured")