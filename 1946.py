import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    data = []
    caselen = int(input())
    print("#{}".format(i+1))
    for i in range(caselen):
        Word, line = input().split()
        line = int(line)
        for j in range(line):
            data.append(Word)

    for i in range(len(data)):

        quota = len(data)//10
        remain = len(data)%10
        for j in range(quota):
            for x in range(10):
                print(data.pop(0), end='')
            print()
        for k in range(remain):
            print(data.pop(0), end='')
    print()