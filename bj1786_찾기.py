text = input()
pattern = input()
pi = [0 for i in range(0, len(pattern))]
result = list()
count = 0

j=0
for i in range(1,len(pattern)):
    while(j > 0 and pattern[i] != pattern[j]):
        j = pi[j - 1]
    if(pattern[i] == pattern[j]):
        j+=1
        pi[i] = j

j = 0;
patternLength = len(pattern)
textLength = len(text)
for i in range(0, textLength):
    while(j > 0 and text[i] != pattern[j]):
        j = pi[j - 1]
    if(text[i] == pattern[j]):
        if(j == patternLength - 1):
            ##같은 패턴을 찾았음
            result.append(i - patternLength + 2)
            count+=1
            j = pi[j]
        else:
            j+=1

print(count)
for c in result:
    print(c)
