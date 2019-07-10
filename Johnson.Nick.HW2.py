#Nick Johnson
#1/29/2018
#HW2

#1 please define a string variable to denote the path 
#c:\programing\Python\mycodes\Project1

file = r"c:\programing\Python\mycodes\Project1.py"
print (file)

#2. Given three variables, x, i, mystr; please format the output using format function
i =10000;
x= 75
mystr = "walk"
# the output should be :  it takes me 75 minutes to walk 10000 steps
output = "it takes me " + str(x) + " minutes to " + str(mystr) + " " + str(i) + " steps"
print (output)


#3: please write the code uisng if and else
#if today is Tuesday or Thursday, I study Pthon, otherwise, I study R
today = "Friday"
if today in ["Tuesday", "Thursday"]:
    print ("I study Python")
else:
    print ("I study R")
    
    

# define the following funtion
#f(x) = sin(x) if x <=0; tan(x) if 0<x< 1; exp(x) if 1<=x <2; log(x) if x>2 print (f(x))
#hint: you need to import math module, then use the function by calling math.sin(x) etc
import math

x = 1

if x <= 0:
    y = math.sin(x)
    print(y)
elif 0 < x < 1:
    y = math.tan(x)
    print(y)
elif 1 <= x < 2:
    y = math.exp(x)
    print (y)
else:
    y = math.log(x)
    print (y)
    

#3 write a for loop to compute the product of 1,2,3, ...,1million
# 1*2*3*...1,000,000
for x in range (1000000):
    y = x*x+1
    print(y)
    
#4 write a for loop to compute the sume of the EVEN numbers 2,4,6,8, ..., 2,000,000
n = 2000000
sum = 0
x = 0
while(n>0):
    for x in range(0,n+1):
        if(x%2==0):
            sum = sum + x
            n = n - 2
    print(sum)
    
    
#5 Explain what does the following program do by using comments
mylist = [1, 3, 6, 2, 8, 10]
target = 2
for idx in range(len(mylist)):
    if mylist[idx] == target:
        break
print(idx)

# Within the mylist array there are 6 variables
# target is the target the variable value we want to find within the list
#the index will tell us where the variable in stored 





