m1n,m2n=input(' ').split(' ')
ski=abs(len(m1n)-len(m2n))
for i in range(len(m1n)):
    if len(m2n)==1 and m2n[i] in m1n:
        break
    if m1n[i] != m2n[i]:
       ski+=1 
print(ski)
