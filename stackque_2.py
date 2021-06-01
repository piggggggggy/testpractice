def solution(priorities, location):
    k = priorities[location]
    priorities[location] = k * 0.9
    count = 0
    while True:
        if max(priorities) == k or max(priorities) == k * 0.9:
            break
        elif priorities[0] > k:
            priorities.pop(0)
            count += 1
        else:
            priorities.append(priorities.pop(0))

    prior = [i for i in priorities if i >= k * 0.9]
    count_ = prior.index(k * 0.9) + 1
    answer = count + count_
    return answer
