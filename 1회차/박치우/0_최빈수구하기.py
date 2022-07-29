import sys

sys.stdin = open("_최빈수구하기.txt")

test_case = int(input())
for i in range(1,1+test_case):
    max = -9999
    number = int(input())
    dic = dict()
    numbers = input().split()
    for key in numbers:
        if key not in dic:
            dic[key] = 1
        else:
            dic[key] += 1
    for j in dic:
        if max < dic[j]:
            max = dic[j]
    for k in dic:
        if dic[k] == max:
            print(k)
