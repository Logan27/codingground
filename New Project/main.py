# Hello World program in Python
k=3
n=4
i=0
l=[]
j=0
old=[1]
while len(l)<k:
    l.append(i)
    i+=1
print (l)
for e in range(1,k):
    print('e',e)
    old[e-1]=l[-e]
    while l[-e]<n:
        l[-e]+=1
        print(l)
    l[-e]=old[e-1]+1    
    for j in range(-e,-1):
        print ('j',j,l[j])
        l[j]=l[j+1]+1
        print ('j+',j,l[j])