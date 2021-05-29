def solution(name):
    N = len(name)


    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def alphabet(spel):
        num = alph.index(spel)
        if num > 13:
            num = 26-num
        return num
    updownCount = sum(map(alphabet,[i for i in name]))


  # A가 아닌 알파벳들의 index list
    _idxList = [i for i,v in enumerate(name) if v != 'A']
    if _idxList[0]==0:
    	_idxList.remove(0)


  # 우 이동
    right = _idxList[-1]
  # 좌 이동
    left = N-_idxList[0]



  # 좌우우좌
    def countlr(index):
        return 2*_idxList[index]+N-_idxList[index+1]
    if len(_idxList) > 1:
        leftright = min(map(countlr, [j for j in range(len(_idxList)-1)]))

        _idxList.reverse()
        _idxList = list(map(lambda x:N-x, lst))

        rightleft = min(map(countlr, [k for k in range(len(_idxList)-1)]))

        answer = min(right, left, rightleft, leftright) + updownCount
    else:
        answer = min(right,left)+updownCount
    return answer