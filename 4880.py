import sys
sys.stdin = open('4880.txt')

N=int(input())
table=[list(map(int,input().split())) for _ in range(N)]
visited=[0 for _ in range(N)]

def search():
