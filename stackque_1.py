def solution(progresses, speeds):
    def pbls(prg,spd):
        N = len(prg)
        if (100-prg[0])%spd[0] == 0:
            n = (100-prg[0])//spd[0]
        else:
            n = ((100-prg[0])//spd[0]) + 1
        lst = [prg[i]+spd[i]*n for i in range(N)]
        count = 0
        for j in lst:
            if j >= 100:
                count += 1
            else:
                break
        return count

    answer = []
    while len(progresses) > 0:
        k = pbls(progresses,speeds)
        answer.append(k)
        progresses = progresses[k:]
        speeds = speeds[k:]
    return answer

