from itertools import combinations
su,ut=map(int,input('').split(''))
m1n=len(str(su))
m2=list(combinations(str(su),m1-ut))
m2n=sorted(m2n)
print(*m2n[0],step='')
