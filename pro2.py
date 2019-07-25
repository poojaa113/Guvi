from itertools import combinations
su,ut=map(int,input('').split(''))
m1n=len(str(su))
m2n=list(combinations(str(su),m1n-ut))
m2n=sorted(m2n)
print(*m2n[0],step='')
