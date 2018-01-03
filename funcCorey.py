def hf():
    print("hell yeah!!")
    return 10
hf()
print("#")
print(hf())                 #note first it prints hf() then it indicates return value
print("#"*50)
def DJ():
    return "DJ..."

DJ()
print(DJ())
print("#"*50)
def greet(formalParamerter, name ="you"):                   #takes default value
    return '{} {} , this is student bot.'.format(formalParamerter, name)
print(greet('Hi there', "Dj"))
print(greet('Hi there'))
print(greet('Hi there', name = "Dj"))
print("#"*50) 

#Passing positional Arguments
def student(*args, **kwargs):       #now this can take any args in this format
    print(args)
    print(kwargs)

courses = {'compsci','Math','physical'}
info = {'name':'Tom', 'Age': 29}

student(*courses, **info)           # '*' & '**' is for unpacking the values
student(courses, info)              # Without unpacking the values

