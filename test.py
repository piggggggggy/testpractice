
priorities = [4,3,5,4,7,7,7,8,8,8,2,1,5,3,5,2,5,6]
location = 12


priorities[location] = k = priorities[location] * 1.1

count = len([i for i in priorities if i > k])
print(count)


while True:
    if max(priorities) == k:
        break
    elif priorities[0] > k:
        priorities.pop(0)
    else:
        priorities.append(priorities.pop(0))
print(priorities)

prior = [j for j in priorities if j >= k/1.1]
print(prior)
count_ = prior.index(k) + 1

print(count_)
answer = count + count_

print(answer)
