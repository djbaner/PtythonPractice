nums = [1,2,3,4,5,6,7,8,9,10]
for n in nums:
    if (n==5):
        print("i am brute and i am goin to come out of this loop")
        break
    else:
        print(n)
print("*"*190)
for n in nums:
    if (n==4):
        print("i am brute and i am going to continue to the next iteration skipping everything else following this statement.")
        continue
    else:
        print(n)
print("*"*100)
for n in nums:
    for s in ("ab", n+1, 'abc'):
        if (n==4):
            print (n)
            break               #only breaks from the inner loop
        print (s ,n)
print("*"*100)
for n in nums:
    for s in ("ab"):
        print (s ,n)
print("*"*100)
for i in range(10):
    print(i)
print("*"*100)
for i in range(1,11,2):
    print(i)
print("*"*100)
x=0
while(x<=50):
    if (x==20):
        print("shortcut")
        break
    print(x)
    x+=4
print("*"*100)