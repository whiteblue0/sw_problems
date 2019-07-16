import sys
sys.stdin = open('input.txt')

Case = int(input())

# i = test case number, 
for i in  range(1,Case+1):
    TestNum = int(input())
    table = []
    
#table에 0~9까지 수 입력, len(table) =10 일때 빠져나옴
    j = 0
    while len(table)<10:
        j+=1                                    #j = testnum에 곱할 n번째 수
        num = TestNum*j
        while num > 0:
            table.append(num%10)                # Testnum*n번째 수의 마지막 숫자 table에 추가
            num //= 10                          # table에 추가한 숫자를 10으로 나눠 지우고, 남은 수를 num으로 반환
            table = list(set(table))            # table의 중복숫자 제거
    print('#{} {}'.format(i, TestNum*j))