a=int(input('Enter x^2 coeffiecent : '))
b=int(input('Enter x coeffiecent : '))
c=int(input('Enter constant term : '))
print('The qudratic equation is : ({})x^2+({})x+({})'.format(a,b,c))
S=(b**2)-(4*a*c)
fr=(-b+(S**0.5))/(2*a) #first root
sr=(-b-(S**0.5))/(2*a) # second root
print('The first root of the equation is : ',fr)
print('The second root of then equation is :',sr)
