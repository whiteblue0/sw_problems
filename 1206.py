import sys
sys.stdin = open('1206.txt')

T = 10
for a in range(1,T+1):
    N = int(input())

    height = list(map(int, input().split()))
    cnt = 0

    for i in range(2,len(height)-2):
        l1 = height[i] - height[i-2]
        l2 = height[i] - height[i-1]
        l3 = height[i] - height[i+1]
        l4 = height[i] - height[i+2]

        if l1>0 and l2>0 and l3>0 and l4>0 :
            temp = 0
            if l1 <= l2 and l1 <= l3 and l1 <= l4:
                temp = l1
            elif l2 <= l1 and l2 <= l3 and l2 <= l4:
                temp = l2
            elif l3 <= l1 and l3 <= l2 and l3 <= l4:
                temp = l3
            elif l4 <= l1 and l4 <= l2 and l4 <= l3:
                temp = l4

            # cnt += min(l1, l2, l3, l4)
            cnt += temp

    print("#{} {}".format(a, cnt))