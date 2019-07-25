aq,bq=map(str,input(' ').split(' '))
cq=0
if len(aq)>len(bq):
    aq,bq=bq,aq
dq=0
while dq<len(aq):
      cq+=(ord(bq[dq])-ord(aq[dq]))
      dq+=1
for dq in range(dq,len(bq)):
      cq+=ord(bq[dq])-ord('a')+1
print(cq)
