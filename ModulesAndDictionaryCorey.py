student = {'name':"DJ", 'roll' : 164457, 'course': ['math', 'science', 'comp']}

print(student['course'])
print (student.get('course'))

#print(student['phone'])         #returns key error, as phone dosent exist in dictionary
print (student.get('phone'))    # returns none by default
print("If the key not present in the dictionary it prints the custome message  : %s\n"%student.get('phone', '"not here buddy....!"'))      #returns custome message
student['name'] = "Deb"
student['phone'] = 9996999969

student['roll'] = 16111006
print ("Now this will print the updates on the Dictionary 'student' : \n%s"%student)

student.update({'name':"DJ", 'roll' : 16111006, 'course': ['math', 'science', 'comp', 'blockchains']})
print ("Now this will print the updates on the Dictionary 'student' all in one sentence command : \n%s"%student)

student['age'] = 30
print(student)

del student['age']
print(student)

student['age'] = 30
popped = student.pop("age")

print("\nthe age that is poped is : %d\n"%popped)
print("\nthe value of the 'student' dictionary is : %s"%student)

print("\nFYI...the number of keys in student are : %d"%len(student))
print("\nand...the keys in student are : %s"%student.keys())
print("\nand...the valuesof the keys in student are : %s"%student.values())
print("\nand...the keys-value pairs in student are : %s"%student.keys())
print("\nthe key-value pairs in items are termed as items and are retrived as follows : %s"%student.items())

for k in student:
    print("\nthe key  is : %s"%k)

print("%s"%(190*"="))
for k,v in student.items():
    print("\nthe key value pair is : %s,%s\n"%(k,v))

print("%s"%(190*"="))


'''using the modules and the associated functions'''                                #chapter on modules
import module1
index = module1.search_index(student.get('course'), 'comp')
print("\nusing the custom made module1.py we have obtained the index as %d" %index)

'''using alias names for modules'''
import module1 as m                                                                 #m is the alias for module 1
index = m.search_index(student.get('course'), 'comp')
print("\nusing the custom made module1.py we have obtained the index as %d" %index)

'''dont wanna type the module name and with alias in shorthand --> '''
from module1 import search_index as si                                              #si is the alias for the function 
index = si(student.get('course'), 'comp')
print("\nusing the custom made module1.py we have obtained the index as %d" %index)

'''using alias names for multiple f() and var of module'''
from module1 import search_index,dummy                                                                  #multiple objects from module 
index =search_index(student.get('course'), 'comp')
print("\nusing the custom made module1.py we have obtained the index as %d" %index)
print(dummy)

'''to import everything  use "*"'''
from module1 import *
import sys                                                                                              #this module used to see which path is used to import the file
sys.path.append('/home/debjyoti/Downloads/IIT Kanpur Academics/Semester-IV 2018/Python/Modules/')    #adding a custom module                                      
index =search_index(student.get('course'), 'comp')
print("\nusing the custom made module1.py we have obtained the index as %d. and everything is still working." %index)
print(dummy)
print(sys.path)
from DjModule2 import module2 
module2()
