import sys

sys.stdin = open("_신용카드만들기1.txt")

test_case = int(input())
for i in range(1,1+test_case):
    number = []
    number = input().split(' ')
    sum = 0
    N = 0
    for num in range(1,1+len(number)):
        if num % 2 == 1:
            sum += int(number[num-1]) * 2
        else :
            sum += int(number[num-1])
    N = 10 - sum % 10
    if N == 10:
        N = 0
    print('#{0} {1}'.format(i,N))

