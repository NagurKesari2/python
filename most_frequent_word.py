from collections import Counter
f1=open('file.txt','w')
f1.write(input('enter any something : '))
f1.close()
f2=open('file.txt','r')
text=f2.read().split()
print('The data you entered is :',text)
print('The most common frequent word in the file is :')
print(Counter(text).most_common(1))
