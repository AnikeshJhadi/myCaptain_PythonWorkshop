i=int(input("Enter the no. of term:-"))
a=[]
for n in range(0,i):
    if n==0:
        a.append(0)
    elif n==1:
        a.append(1)
    else:
        a.append(a[n-1]+a[n-2])
print(a)
