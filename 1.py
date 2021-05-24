N,M,K = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
# count = 0
# val = 0
# for i in range(M):
#     if count <= K:
#         count +=1
#         val = val + lst[-1]
#     else:
#         count = 0
#         val = val + lst[-2]
# print(val)

a = lst[-1]
b = lst[-2]
if M != K:
    result = (a*K+b)*(M//(K+1)) + a*(M%(K+1))
else:
    result = K*a

print(result)