#operations
#union
#intersection
#difference

#union                          #remove duplicated value then combine elements
set1={1,2,3,4,5,6}
set2={5,5,6,7,8,9,10}
set3=set1.union(set2)
print(set3)

#intersection                   #return a common element
set4=set1.intersection(set2)
print(set4)

#difference
set1-set2
set5=set1.difference(set2)
print(set5)

set2-set1
set6=set2.difference(set1)
print(set6)
