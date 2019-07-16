test=int(input())
for i in range(test):
    kk=input()
    st=input()
    st=st.split(" ")
    st=st[:-1]
    count=[]
    for j in range(101):
        count.append(0)

    for j in range(len(st)):
        tmp=int(st[j])
        count[tmp]+=1

    max_component=0
    max_index=0
    for j in range(len(count)):
        if (max_component<=count[j]):
            max_component=count[j]
            max_index=j

    print("#%d %d"%(i+1,max_index))