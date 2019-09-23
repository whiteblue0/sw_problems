def preorder(node):
    if node != 0:
        r.append(chr(node+64))
        preorder(tree[node][0])
        preorder(tree[node][1])

def interorder(node):
    if node != 0:
        interorder(tree[node][0])
        r.append(chr(node+64))
        interorder(tree[node][1])

def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        r.append(chr(node+64))

table = {'.':0,
         'A':1,
         'B':2,
         'C':3,
         'D':4,
         'E':5,
         'F':6,
         'G':7,
         'H':8,
         'I':9,
         'J':10,
         'K':11,
         'L':12,
         'M':13,
         'N':14,
         'O':15,
         'P':16,
         'Q':17,
         'R':18,
         'S':19,
         'T':20,
         'U':21,
         'V':22,
         'W':23,
         'X':24,
         'Y':25,
         'Z':26
         }



N = int(input())
tree = [0]*(N+1)
for i in range(N):
    temp = input().split()
    temp2 = [table[temp[1]],table[temp[2]]]
    tree[table[temp[0]]] = temp2
#
# for i in range(N):
#     print(i,tree[i])
r = []
preorder(1)
print(''.join(r))
r = []
interorder(1)
print(''.join(r))
r = []
postorder(1)
print(''.join(r))