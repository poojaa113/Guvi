a8=int(input())
n8=list(map(int,input().split()))
l8=[]
for ij in n8:
  k1=bin(ij)
  l8.append(k1)
fg=sorted(l8)
fg.reverse()
for jk in fg:
  print(int(jk,2))
