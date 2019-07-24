import sys
sys.stdin = open('input.txt')

dy = [0,1,0,-1]
dx = [1,0,-1,0]


T = int(input())
N, K = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

