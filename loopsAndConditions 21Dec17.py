#Testing Range
for a in range(20):
    if a%2 == 0:
        continue
    print(a)
print("End of series\n\n")
#Exercise Python 21 Dec 17 on loops and conditions
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
    ]

print("The given array is having the following elements :\n %s \n \n...and there are %d elements. Phew!!!\n" %(numbers, len(numbers)))
# to display even numbers from the array 'numbers' 
i=0     
n=0
print("\nEven numbers less than 237 from the array 'numbers' are as follows :\n") 
for i in numbers:
    if (i<=237 and i%2==0):
        print(i)
        n+=1
    i += 1
print("\nThere are %d elements above." %n)
# to display even numbers from the array 'numbers'
print("\nOdd numbers >= 237 from the array 'numbers' are as follows :\n")# to display even numbers from the array 'numbers'
n=0
for i in numbers:
    if (i>=237 and i%2==1):
        print(i)
        n+=1        
    i += 1
print("\nThere are %d elements above." %n)