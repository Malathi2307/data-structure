list=[1,2,3,4,5]
n=len(list)
for i in range(n):
    for j in range(i+1,len(list)):
        print(list[i],list[j])
