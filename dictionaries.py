class pb:
    name = ""
    num = 0
    addr = ""
    email = ""

u1 = pb()

def ph():
    ph1 = {"dj" : (9969615615, "krk", "aha") ,"AJ" : 9996999699, 1 : (9969615615, "krk", "aha") }
    return ph1

def ph_book(i):
    return i 
def add():
    a = ph()
    #name = input("enter name :")
    #num = input("enter phone number :")
    #addr = input("enter address :")
    #email = input("enter email :")
    
    a = a +  input("add the contact details : ")
    return a

def view():
    ctc = ph()
    #for name,number in ph.items():
    #print(ctc)
    for a in ctc:
        print(a , ctc[a])



view()
add()
view()

#ph = ph + {"Tj" : 09999612345}

