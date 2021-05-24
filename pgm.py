#프로그래머스 그리디 2번문제!!!(미완성)
def solution(name):
    alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    # 알파벳 조정
    count = 0
    for i in name:
        idx = alp.index(i)
        if idx <= 13:
            count += idx
        else:
            count += (26-idx)

    #좌우조정

    return answer
