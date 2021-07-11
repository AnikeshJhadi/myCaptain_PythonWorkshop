term=int(input("Enter the no.of terms you want in your list:-"))
list=[]
print("Input the numbers in list:-")
for i in range(0,term):
    list.append(int(input()))
print("Positive numbers of list are:-")
for j in range(0,term):
    if list[j]>0:
        print(list[j])
    else:
        continue
