import sys

sys.stdin = open("_직사각형길이찾기.txt")


test_case = int(input())
for i in range(1,1+test_case):
    numbers = list(map(int,input().split()))
    dic = dict()
    for j in numbers:
        if j not in dic:
            dic[j] = 1
        else:
            dic[j] += 1
    for k in dic.keys():
        if dic[k] % 2 == 0:
            continue
        else:
            print('#{0} {1}'.format(i,k))

    
