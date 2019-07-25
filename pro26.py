a8=int(input())
c8=list(map(int,input().split()))
x8=[1]*a8
for pq in range(a8):
    if pq==0:
        if c8[pq]>c8[pq+1]:
            x8[pq]=x8[pq]+x8[pq+1]
    elif pq>0:
        if c8[pq]>c8[pq-1]:
            x8[pq]=x8[pq]+x8[pq-1]
print(sum(x8))
