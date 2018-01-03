tuple1 = ("awsev","jjsvbd","itihstb","uoihetv","iuhebs")
tuple2 = tuple1

#tuple2.sort()      #in tuples we cant modify the data --> immutable
print(tuple1[2])    #we can only access the tuple and cannot use the commands that change the values
print(tuple2)

sete = {'ddlj', 'mbbs', 'knph', 'bakwaas'}
print(sete)
sete.add("cat")
sete.update(["mbbs","mba"])
print("\nnotice the difference in two .update commands : \n%s"%sete)
sete.update("mbbs","mba")
print("\nnow it takes the individual letters : \n%s\n"%sete)
set1 = {'ddlj', 'mbbs', 'knph', 'bakwaas'}
set1.remove("mbbs")
print("the common elements in both sets are : \n%s\n"%set1.intersection(sete))
print("the elements not present in set1 but in sete are : \n%s\n"%sete.difference(set1))
set1.add("gmat")
print("the elements not present in sete but in set1 are : \n%s\n"%set1.difference(sete))
print("the elements not present in sete but in set1 are : \n%s\n"%sete.union(set1))