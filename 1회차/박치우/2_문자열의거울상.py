import sys

sys.stdin = open("_문자열의거울상.txt")


test_case = int(input())
for i in range(1,1+test_case):
    word = input()
    lst = []
    dic = {'b' : 'd','d' :'b','p':'q','q':'p'}
    for j in word:
        for k in dic:
            if j == k:
                lst.append(dic[k])
    print('#{0}'.format(i),''.join(lst[::-1]))
