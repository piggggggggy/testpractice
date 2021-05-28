def solution(n,lost,reserve):
    setlost = set(lost) - set(reserve)
    setreserve = set(reserve) - set(lost)
    count = 0
    for i in setlost:
        if i-1 in setreserve:
            count +=1
            setreserve.remove(i-1)
        elif i+1 in setreserve:
            count +=1
            setreserve.remove(i+1)
    answer = n-len(setlost)+count
    return answer


a = 5
b = [2,4]
c = [1,3,5]

print(solution(a,b,c))