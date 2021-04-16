#set
#properties

set1={}                 #dictionary
print(type(set1))

#using a function           #true=1
set2={1,2,3,4,"sabir",1,2}      #it support heterogeneous data
print(set2)                 #it doesnot support duplicated values
set={1,2,3,"sabir",100}                       #insertion order not preserved
print(set)                  #it is mutable


#add a value in a list
#using add function
set2.add(5)
print(set2)

#at a time multiple value in a list
#using update function
set2.update([10,"technolab,20"])
print(set2)

#sum
set5={1,2,3,4,5,6}
print(sum(set5))
#max
print(max(set5))
#min
print(min(set5))
#length
print(len(set5))