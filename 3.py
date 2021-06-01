N,K = map(int, input().split())

count = 0
while True:
    if N%K ==0:
        N = N/K
        count +=1
    else:
        N = N-1
        count += 1
    if N == 1: break

print(count)
# a = 0
# count = 0
# while True:
#     a += N%K
#     if N//K == 0 or : 1
#     else:
#         N = N//K
#         count +=1
# print(a+count)
#실패...