print ("imported module from module1.py in Dj")
def search_index(search_in,search_for):
    '''defining function for searching string in series of strings'''
    for i, value in enumerate(search_in):
        if value == search_for:
            return i
    return -1

dummy = 'i am a dummy string'
