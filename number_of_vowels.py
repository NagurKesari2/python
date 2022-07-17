string=input('Enter any string of your choice : ')
a='AEIOUaeiou'
n=[i for i in string if i in a]
c=len(n)
print('The number of vowels in the given sring is :',c)
print('The percentage of vowels is :',(c/len(string))*100)
