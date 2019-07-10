#Homework #3
#Nick Johnson


#1 Please use Ternary expressions rewrite the following codes into one line code:
x =100
if x < 0:
    a = x+1
else:
    a = x*x
print(a)
        
x = 100 
a= x+1 if x < 0 else x*x 
print(a)

#2: create the following lists using Python codes
# country = ("USA", "India", "China", "Russia")
# population = (300, 120, 130, 100)

country = ("USA", "India", "China", "Russia")
population = (300, 120, 130, 100)

#3: what is the results of the following oprations
cp = country + population
print(cp)
    #('USA', 'India', 'China', 'Russia', 300, 120, 130, 100)

p10 = population*10
print(p10)
#    (300, 120, 130, 100, 300, 120, 130, 100, 300, 120, 130, 
#    100, 300, 120, 130, 100, 300, 120, 130, 100, 300, 120, 130,
#    100, 300, 120, 130, 100, 300, 120, 130, 100, 300, 120, 130, 
#    100, 300, 120, 130, 100)

len(country)
    #4
    
country[1]
    #India
    
population[3] = 320
    #TypeError: 'tuple' object does not support item assignment

#4 Given mytup = ((1,2,3), ("M", "T"), 2018)

mytup = ((1,2,3), ("M", "T"), 2018)
a,b,c = mytup

#what is b
print(b)
    #('M', 'T')
    
    
a, (b,c), d = mytup

#what is c
print(c)
    #T
