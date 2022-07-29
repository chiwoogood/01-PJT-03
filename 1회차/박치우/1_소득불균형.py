import sys

sys.stdin = open("_소득불균형.txt")


test_case = int(input())
for i in range(1,1+test_case):
    number = int(input())
    member = list(map(int,input().split(' ')))
    count = 0
    sum = 0
    for j in member:
        sum += j
    avg = sum / len(member)
    for k in member:
        if k <= avg:
            count +=1
    print('#{0} {1}'.format(i,count))
