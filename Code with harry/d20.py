'''
#this code shows the use of functions
def isGreater(a,b):
    if(a>b):
        print(a, "is greater.")
    else:
        print(b, "is greater.")
isGreater(8,2)

#now using default parameters

def averageOf(a=5,b=7):
    avg=(a+b)/2
    print("The average is", avg)

averageOf()
averageOf(b=9)
averageOf(8,10)

#when there are indefinite arguments
'''
def averageOf(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    print("Average is :",sum/len(numbers))

averageOf(5,6,4,8,9)