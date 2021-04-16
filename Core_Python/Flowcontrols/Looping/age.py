#find current age
birthyear=int(input("Enter the birth year"))
birthmonth=int(input("Enter the birth month"))
birthdate=int(input("Enter the birth date"))
currentyear=int(input("Enter the currentyear"))
currentmonth=int(input("Enter the current month"))
currentdate=int(input("Enter the current date"))

currentage=currentyear-birthyear

if(currentmonth>birthmonth):
    print("Current age is", currentage)
elif(currentmonth<birthmonth):
    currentage=currentage-1
    print("Current age is", currentage)
else:
    if (currentdate >= birthdate):
        print("Current age is", currentage)
    else:
        currentage = currentage - 1
        print("Current age is", currentage)

