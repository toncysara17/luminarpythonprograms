#number is even
#function with argument and return type
def even(num):
    num=int(input("Enter the number"))
    if(num%2==0):#9%2==0
        result="Even"
    else:
       result="Not Even"
    return result
data=even(2)
print(data)

