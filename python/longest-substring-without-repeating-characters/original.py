import timeit

code_to_test = """
s = 'safasdfasf'
li = []
for i in range(len(s)):
    for j in range(len(s) - i):
        if len(set(s[i:i + j + 1])) == len(s[i:i + j + 1]):
            li.append(s[i:i + j + 1])
print(len(sorted(li, key=len)[len(li) - 1]))
"""
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print(elapsed_time)
