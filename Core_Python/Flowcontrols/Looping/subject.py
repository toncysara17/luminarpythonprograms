#find sub mark,assume that total mark 200
sub1=int(input("Enter a mark in sub1"))
sub2=int(input("Enter a mark in sub2"))
sub3=int(input("Enter a mark in sub3"))
sub4=int(input("Enter a mark in sub4"))
totalheld=200
total=sub1+sub2+sub3+sub4
per=(total/totalheld)*100
if(per>=90):
    print("A+")
elif(80<per<89):
    print("A")
elif(70<per<79):
    print("B+")
elif(60<per<69):
    print("B")
elif(50<per<59):
    print("C+")
elif(40<per<49):
    print("C")
elif(30<per<39):
    print("D+")
else:
    print("fail")