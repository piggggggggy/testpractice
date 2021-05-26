def solution(name):
    N = len(name)
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def alphabet(spel):
        num = alph.index(spel)
        if num > 13:
            num = 26-num
        return num
    updown = sum(map(alphabet,[i for i in name]))
    # A가 아닌 알파벳들의 index list
    lst = [i for i,v in enumerate(name) if v != 'A']
    # 우 이동
    right = lst[-1]
    # 좌 이동
    left = N-lst[1] if lst[0]==0 else N-lst[0]
    # 왼->오
    if lst[0]==0:
        lst.remove(0)
    NN = len(lst)
    def countlr(index):
        return 2*lst[index]+N-lst[index+1]
    if NN > 1:
        leftright = min(map(countlr, [j for j in range(NN-1)]))

        lst.reverse()
        lst = list(map(lambda x:N-x, lst))

        rightleft = min(map(countlr, [k for k in range(NN-1)]))

        answer = min(right, left, rightleft, leftright) + updown
    else:
        answer = min(right,left)+updown
    return answer