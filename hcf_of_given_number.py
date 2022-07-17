a=int(input('Enter a number : '))
b=int(input('Enter a number : '))
hcf=1
for i in range(1,a+1):
    if (a%i)==0 and (b%i)==0:
        hcf=i
print('The highest common factor is : ',hcf)
