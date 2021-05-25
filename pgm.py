
def solution(name):
    N = len(name)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    updown = 0
    for spel in name:
        num = alphabet.index(spel)
        if num < 13:
            updown += num
        else:
            updown += (26-num)

    i = 1
    while i < N:
        if name[N-i] != 'A':
            break
        i +=1
    right = N - i

    j = 1
    while j < N:
        if name[j] != 'A':
            break
        j += 1
    left = N - j

    lst = []
    for i, v in enumerate(name):
        if v != 'A':
            lst.append(i)

    # 3-1. 오른쪽 갔다가 왼쪽
    rightleft = 0
    if len(lst) > 1 and lst[0] != 0:
        k = 0
        while k < len(lst) - 1:
            move = 2 * lst[k] + N - lst[k + 1]
            # rightleft.append(move)
            if rightleft == 0 or move < rightleft:
                rightleft = move
            k += 1
    elif len(lst) > 1 and lst[0] == 0:
        l = 1
        while l < len(lst) - 1:
            move = 2 * lst[l] + N - lst[l + 1]
            # rightleft.append(move)
            if rightleft == 0 or move < rightleft:
                rightleft = move
            l += 1

    leftright = 0
    if len(lst) > 1 and lst[0] != 0:
        k = -1
        while -k < len(lst):
            move = 2 * (N - lst[k]) + lst[k - 1]
            # leftright.append(move)
            if leftright == 0 or move < leftright:
                leftright = move
            k -= 1
    elif len(lst) > 1 and lst[0] == 0:
        k = -1
        while -k < len(lst)-1:
            move = 2 * (N - lst[k]) + lst[k - 1]
            # leftright.append(move)
            if leftright == 0 or move < leftright:
                leftright = move
            k -= 1

    if leftright>0 and rightleft>0:
        mini = min(right, left, leftright,rightleft)
    elif leftright == 0 and rightleft>0:
        mini = min(right, left, rightleft)
    elif rightleft == 0 and leftright >0:
        mini = min(right, left, leftright)
    else:
        mini = min(right,left)

    answer = mini + updown
    return answer
