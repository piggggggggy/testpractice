def solution(name):
    N = len(name)
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def alphabet(spel):
        index = alph.index(spel)
        if index > 13:
            index = 26-index
        return index
    updown = sum(map(alphabet,[i for i in name]))
    # A가 아닌 알파벳들의 index list
    lst = [i for i,v in enumerate(name) if v != 'A']
    # 우 이동
    right = lst[-1]
    # 좌 이동
    if lst[0]==0:
        lst.remove(0)
    left = N-lst[0]
    # 왼->오
    NN = len(lst)
    def countleftright(index):
        return 2*lst[index]+N-lst[index+1]
    if NN > 1:
        leftright = min(map(countleftright, [j for j in range(NN-1)]))

        lst.reverse()
        lst = list(map(lambda x:N-x, lst))
        rightleft = min(map(countleftright, [k for k in range(NN-1)]))
    # right, left, leftright, rightleft 중 최소값과 updown
        answer = min(right, left, rightleft, leftright) + updown
    else:
        answer = min(right,left)+updown
    return answer