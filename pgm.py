

#
# def solution(name):
# 위아래@@

    # name = 'AABBBBSSADAABA'
    # alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # updown = 0
    # for spel in name:
    #     num = alphabet.index(spel)
    #     if num < 13:
    #         updown += num
    #     else:
    #         updown += (26-num)

    # updown : A->? 조이스틱 횟수의 합

# 좌우@@
    N = len(name)

    # 1. 오른쪽으로만 갈 경우   'AXXAAXXA' 라고 했을 때 가장 마지막에 있는 X의 index값
    i=1
    while i < N:
        if name[N-i] != 'A':
            break
        i +=1
    right = N - i

#     # 2. 왼쪽으로만 갈 경우
    for j in range(N):
        if name[j+1] == 'A':
            pass
        else:
            break
    left = N - (j+1)

#     # 3. 오른쪽갔다가 왼쪽으로 갈 경우
#     lst = []
#     t = 0
#     for l in name:
#         if l != 'A':
#             lst.append(t)
#         t += 1
#
#
#     rl = []
#     le = len(lst)
#     if le >1:
#         if lst[0] != 0:
#             for q in range(le-1):
#                 o = (2*lst[q]+N-lst[q+1])
#                 rl.append(o)
#         else:
#             for q in range(1,le-1):
#                 o = (2 * lst[q] + N - lst[q + 1])
#                 rl.append(o)
#     else:
#         for m in lst:
#             o = m
#             rl.append(o)
#
#     # 1,2,3의 경우 중 최소값과 위아래 최소값의 합
#     answer = min(right,left,min(rl))+updown
#     return print(answer)
#
# aaaa = 'JADDZ'
# solution(aaaa)