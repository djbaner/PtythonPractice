courses = ['math','algo','software arch', 'comp security', 'python', 'Java', 'Node JS']
import sys
#print (sys.path)
import random                                                   # importing std library function 
print(random.choice(courses))                                   # choice is an attribute of random 

import math
rads = math.radians(90)
print(rads)                                                     # prints radian values
print(math.sin(rads))                                           
print("*"*150)

import datetime                                                 # datetime buitin
import calendar

today = datetime.date.today()
print(today)
isit = calendar.isleap(2018)
print(isit)
print("*"*150)

import os                                                       # operates with the underlying OS
print(os.getcwd())                                              # prints the current working directory
print(calendar.__file__)                                        # prints the location of file "calendar" saved as .pyc file 
print(os.__file__)                                              # prints "os" file location.
print("*"*150)

#import webbrowser
#webbrowser.open("https://xkcd.com/353/")
print(os.environ.get('HOME'))
file_path = os.environ.get('HOME') + 'tst.txt'
print(file_path)                                                #works but with issues as '/' is not included

file_path = os.path.join(os.environ.get('HOME') , 'tst.txt')    # now it joins the two path
print(file_path)                                                
print("*"*150)

print(os.path.exists('/tmp/tst.txt'))                           #to check path exists or not
print(os.path.exists('/home/debjyoti'))
print(os.path.splitext('/tmp/tst.txt'))                         #to get the file name without the extension
print(dir(os.path))                                             # ** lists all methods that can be used with os.path method