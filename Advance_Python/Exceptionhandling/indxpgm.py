# #index exception
# lst=[1,2,3]
# try:
#      res=a[7]
#      print("a[7] is",res)
# except:
#      print("exception occured")


# #Another method
lst=[1,2,3]
try:
    i=int(input("Enter index"))
    print(lst[i])
except Exception as e:
    print("Exception")