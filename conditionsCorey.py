language = "python"

if language == "C++":
    print("C++")
elif language == "Java":
    print("Java")
elif language == "python":
    print("Python")
else:
    print("language not defined")
print("%s\n"%(190*"="))

user = "Admin"
login = False

if not login:
    print("Please Log in :")
else :
    print("Welcome Admin")
print("%s\n"%(190*"="))
a=[1,2,4]
b=[1,2,4]
if a==b:
    print("a and b are equal")
if a is b:
    print("a is b, as referred in memmroy")
else:
    print(a is b)
    print("as the id of a is %d and the id of b is %d\n"%(id(a), id(b)))

print("%s\n"%(190*"="))
b=a
print(a is b)
print("as now the id of a is %d and the id of b is %d after the operation 'b=a', as ther are the same object in the memory \n"%(id(a), id(b)))
print(id(a)==id(b))
print("%s\n"%(190*"="))
Condition = ""
print(Condition)
if Condition:
    print("thats true")
else:
    print("thats False. It also includes 0,[],{}, and any other empty string")
