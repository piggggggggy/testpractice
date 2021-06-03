def solution(priorities, location):
    priorities[location] = k = priorities[location] * 1.1
    count = len([i for i in priorities if i > k])
    while True:
        if max(priorities) == k:
            break
        elif priorities[0] > k:
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
    prior = [j for j in priorities if j >= k/1.1]
    count_ = prior.index(k) + 1
    answer = count + count_
    return answer

a = [2, 1, 3, 2]
b = 2

print(solution(a,b))