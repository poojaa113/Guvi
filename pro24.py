vj8,vk8=map(int,input().split())
l8=list(map(int,input().split()))
vj8=[]
l8.insert(0,0)
for a in range(vk8):
     v8=[]
     sumup=0
     ccc,ddd=map(int,input().split())
     for bb in range(ccc,ddd+1):         
         sumup^=l7[bb]     
     vj8.append(sumup)
for cc in vj8:
    print(cc)
