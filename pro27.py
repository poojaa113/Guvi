x8,j8=map(int,input().split())
y8=list(map(int,input().split()))[:x8]
count8=0
for kl in range(0,len(y8)-1):
  for sec in range(kl+1,len(y8)-1):
    if(y8[kl]+y8[sec]==j8):
      count8+=1  
if count8==1:
  print("yes")
else:
  print("no")
