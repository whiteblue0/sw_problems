import sys
sys.stdin = open('4408.txt')

def run(data):


    cnt=0
    for i in range(len(data)):
        line=[0 for _ in range(eroom+1)]

        que=[]
        que.append(i)
        # lining data[i]
        for _ in range(data[i][0],data[i][1]+1):
            line[_]=1
        for j in range(len(data)):
            if j!=i:
                flag=1
                while flag:
                    # que에 들어있는 이동과 겹치는지 확인
                    for c in range(data[j][0],data[j][1]+1):
                        if line[c]==1:
                            flag=0
                    que.append(j)
                    # lining data[j]
                    for _ in range(data[j][0],data[j][1]+1):
                        line[_]=1
                    print(que)
                    flag=0
        if len(que)==len(data):
            result=1
            return result
        elif cnt<len(que):
            cnt=len(que)
            tray=que.copy()
        return tray

T = int(input())
N = int(input())

data = []

for i in range(N):
    data.append(list(map(int, input().split())))
print(data)
sroom = 400
eroom = 0
for w in range(N):
    for u in range(2):
        if sroom >= data[w][u]:
            sroom = data[w][u]
        if eroom <= data[w][u]:
            eroom = data[w][u]


check = [0 for _ in range(len(data))]

go = 0