#no.of classes held and no of classes attend
clsheld=int(input("no of classes held"))
clsattnd=int(input("number of classes attended"))
per=(clsattnd/clsheld)*100
if(per>75):
    print("allowed")
else:
    print("not allowed")