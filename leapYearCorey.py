month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
'''defining founction to determine a leap year'''
def leap(year):                 
    return year %4 == 0 and (year%100!=0 and year%400==0)   #'''returns true is condition satisfied'''

def DIM(year,month):
    if not 1<=month<=12:
        return 'invalid month'
    if month==2 and leap(year):
        return 29
    else:
        return month_days[month]

print(DIM(2009, 2))
print(leap(2101))

