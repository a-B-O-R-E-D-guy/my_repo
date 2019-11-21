s = input('substring: ')
k = int(input('k value: '))
li = []
[li.append(s[i:i + k+j]) for i in range(len(s)) for j in range(len(s)-k+1)]
[li.remove(li[j]) for j in list(range(len(li)))[::-1] if len(set(li[j])) != k]
print(sorted(li, key=len)[len(li) - 1])
