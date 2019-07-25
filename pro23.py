a8,b8=map(int,input().split())
lis=list(map(int,input().split()))
l8=[]
for i in range(0,b8):
     u8,v8=map(int,input().split())
     l8.append([u8,v8])
for i in range(b8):
     lower=l8[i][0]
     upper=l8[i][1]
     s8=sum(lis[lower-1:upper])
     print(s8)
