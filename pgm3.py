p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]

if (100 - p[0]) % s[0] == 0:
    n = (100 - p[0]) // s[0]
else:
    n = ((100 - p[0]) // s[0]) + 1
print(n)

count = []
for i in range(len(p)):
    pp = p[i] + n * s[i]
    count.append(pp)
print(count)

while True:
    if count[0] < 100:
        break
    count.pop(0)
answer = len(p) - len(count)

# for j, v in enumerate(count):
#     if v >= 100:
#         count[j] = 0
#     else:
#         break
# answer = count.count(0)


print(answer)
