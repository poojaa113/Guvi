m1n=int(input(''))
k2l=[]
for i in range(0,m1n):
    k2l.append(input())
m2n=len(k2l[0])
k3l=""
for i in range(0,m1n):
    k4l=k2l[0][i]
    k5l=0
    for j in range(0,m1n):
        if(k4l!=k2l[j][i]):
            k5l=1
    if(k5l==0):
        k3l=k3l+k4l
    else:
        break
print(k3l)
