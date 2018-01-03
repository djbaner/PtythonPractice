#functions
def list():
    a=["dj","aj","rj","mj","vj"]
    return a

def jockeys(j):
    #print("%s is a Jockey." %j)         #if this is used, the function after printing will return 'None' which will get printed during pj() as we are printing the whole function state  
    return "%s is a Jockey." %j

def pj():
    list_local = list()
    for b in list_local:
        #return jockeys(b)              #//  if this line is uncommented --> it will not execute the next line, it simply goes back to the begining of the for loop
        print(jockeys(b))

pj()

    