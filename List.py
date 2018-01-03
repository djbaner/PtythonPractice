#..........List............
a = ["awsev","jjsvbd","itihstb","uoihetv","iuhebs"]
print(a[:2])
print(a[-2])
print(a[2:])

#append
a.append("Jam")
print(a)

#insert
a.insert(3,"Cheese")
print(a)

#inserting array as an element inside another array
a1 = ['mac', 'cheese']
a.insert(0, a1)
print(a)

#difference between EXTEND and APPEND
a.extend(a1)    #adds value
print(a)
a.append(a1)    #appends the Array 
print(a)

#To remove or POP value from a list
print("\npops the last element")
poped = a.pop()
print("popped element is : %s \n" %poped)
print(a)     

a.remove(['mac', 'cheese'])           #note the way the array element within the array is written with the exact spacing
print(a)

#to reverse the list
a.reverse()
print("\nthe reversed list is :\n%s" %a)  

#sort
b = a
print(a)
b.sort()
print("\nthe sorted and reversed list (in alphabetical order) is :\n%s" %b)
sorted_array = sorted(a)
print("\nthe sorted and reversed version of array (in alphabetical order) is :\n%s" %sorted_array)
print("\nthe roiginal list is :\n%s" %a)        #needs to be checked

num = [3,3,1,1,5,6,2,7,8,3,7,5,89,2,1,4,5,2,35,3,12]
print("\nthe number list is :\n%s" %num)
num.sort(reverse=False)
print("\nthe ordered list in ascending order is :\n%s" %num)
num.sort(reverse=True)
print("\nthe reversed list in descending order is :\n%s\n" %num)
print("max num is: %d\n"%max(num))
print("min num is: %d\n"%min(num))
print("sum of num is: %d\n"%sum(num))

#index 
print("the index value of 'cheese' is %d\n"%a.index('cheese'))
print("Jam" in a)       #prints wether the value exists in array

#for loop
for stuff in a:
    print(stuff)

print("\nnow we enumerate the items along with the index")
for index, dj in enumerate(a):
    print(index, dj)

print("\nnow we make the index to start from 1")
for ind, dj in enumerate(a, start=1):
    print(ind, dj)

b = ' # '.join(a)
print("\nthe contents of the array are joined using the '.join' command and using any special character (for e.g ' # ') : \n%s"%b)

original = b.split(" # ")
print("\nthe contents of the array are split using the '.split' command and removing any special character as previously set (for e.g ' # ') : \n%s"%original)