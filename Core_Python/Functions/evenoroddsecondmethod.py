#number is even or odd
#function with argument and no return type
def even(num):
    num=int(input("Enter the number"))
    if(num%2==0):#9%2==0
        print("number is even")
    else:
        print("number is odd")
even(2)