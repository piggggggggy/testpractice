N,M = map(int, input().split())

val = 0
for i in range(N):
    lst = list(map(int,input().split()))
    lst.sort()
    if val < lst[0] :
        val = lst[0]

print(val)

