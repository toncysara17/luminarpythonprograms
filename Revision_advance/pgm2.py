#using exception handling
a=[1,2,3]
i=int(input("enter index"))
try:
    print(a[i])

except Exception as e:
    print("exception occured")

