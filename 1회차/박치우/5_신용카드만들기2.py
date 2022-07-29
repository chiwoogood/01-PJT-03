import sys

sys.stdin = open("_신용카드만들기2.txt")

card_list = ['3','4','5','6','9']
test_case = int(input())
for i in range(test_case):
    lst =[]
    number = input()
    lst = [char for char in number]
    for j in lst:
        if j == '-':
            lst.pop(lst.index(j))
    if len(lst) != 16 or lst[0] not in card_list:
        print('#{0} {1}'.format(i+1, 0))
    else :
        print('#{0} {1}'.format(i+1, 1))
    

