#코드업 16진법 만들기

# a = input()
#
# sixt = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
# for k,v in sixt.items():
#     if v == a:
#         p=k
#
# for i in range(1,16):
#     m = p*i//16
#     r = p*i%16
#     if p*i<16 :
#         print(a+"*"+sixt[i]+"="+a)
#     else:
#         print(a+"*"+sixt[i]+"="+sixt[m]+sixt[r])

# a = {'a':5,'b': 7, 'c':4}
#
# b = list(map(int, a))
#
# print(b)


# 3. 오른쪽갔다가 왼쪽으로 갈 경우



    #
    # name = 'BBDAEFADA'
    #
    #
    #
    # N = len(name)
    #
    # # 위아래
    # alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # updown = 0
    # for i in name:
    #     p = alp.index(i)
    #     if p < 13:
    #         updown += p
    #     else:
    #         updown += (26 - p)
    # # 좌우
    # # 1. 오른쪽으로만 갈 경우
    # a = 1
    # for i in range(N):
    #     if name[N - a] == 'A':
    #         a += 1
    #     else:
    #         break
    # right = N - a
    #
    # # 2. 왼쪽으로만 갈 경우
    # b = 0
    # for j in name:
    #     if j == 'A':
    #         b += 1
    #     else:
    #         break
    # left = N - b
    #
    # lst = []
    # t = 0
    # for l in name:
    #     if l != 'A':
    #         lst.append(t)
    #     t += 1
    #
    # rl = []
    # le = len(lst)
    # if le > 1:
    #     if lst[0] != 0:
    #         for q in range(le - 1):
    #             o = (2 * lst[q] + N - lst[q + 1])
    #             rl.append(o)
    #     else:
    #         for q in range(1, le - 1):
    #             o = (2 * lst[q] + N - lst[q + 1])
    #             rl.append(o)
    # else:
    #     for m in lst:
    #         o = m
    #         rl.append(o)
    # answer = min(right,left,min(rl))+updown
    # print(answer)


# name = 'JAZAAAABBA'
# N=len(name)
#
# for j in range(N):
#     if name[j + 1] == 'A':
#         pass
#     else:
#         break
# left = N - (j + 1)
#
# print(left)
# a = [0]
# print(min(a))


name = 'AABBBBSSADAABA'
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# updown = 0
# for spel in name:
#     num = alphabet.index(spel)
#     if num < 13:
#         updown += num
#     else:
#         updown += (26-num)
#
# print(updown)


N = len(name)
# 1. 오른쪽으로만 갈 경우   'AXXAAXXA' 라고 했을 때 가장 마지막에 있는 X의 index값
i=1
while i < N:
    if name[N - i] != 'A':
        break
    i += 1
right = N - i
print(right)