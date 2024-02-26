
#Q1
'''
l=eval(input("Enter a list: "))
l.sort()
print("largest: ",l[-1])
print("smallest: ",l[0])
'''
#Q2
'''
l=eval(input("Enter a list: "))
l=list(set(l))
l.sort()
print("third largest: ",l[-3])
'''

#Q3
'''
l=eval(input("Enter a list: "))
n=int(input("Enter the number: "))
l1=list()
for i in l:
    if i<n:
        l1.append(i)
print(l1)
'''

#Q4
'''
l=eval(input("Enter a list: "))
l1=list()
for i in l:
    if i%2==0:
        l1.append(i)
l1.sort()
print(l1)
'''

#Q5
'''
l1=eval(input("Enter a list: "))
l2=eval(input("Enter a list: "))
l=list()
for i in l1:
    if i in l2:
        l.append(i)
print(l)
'''
