#check whether all properties are ok
#ppty:1

list=[] # using square bracket # empty set
#st=lst() # using function
#print(type(lst)) #datatype?
#print(type(lst)) #datatype?

#ppty:2
lst1=[10,10.5,"luminar","sabir",True]    #its hetrogeneous supported
print(lst1)
#10 int
#10.5 float
#"luminar string
#sabir string
#true boolean


#ppty:3
lst2=[10,10,"sabir","sabir"]      #its duplicated elements supported
print(lst2)


#ppty:4
lst3=[10,20,40,"same"]              #insertion preserved order
print(lst3)


#ppty:5
lst4=[10,8,7,9,1,2,100,45]
# index value
# 0 to n-1
#update the value in 3rd position
lst4[3]=50
print(lst4)                        #it is mutable becausse the value is updated

