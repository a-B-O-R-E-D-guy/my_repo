import timeit

code_to_test = """
s = 'afasda'
li = {}
ans = 0
i = 0
for j in range(len(s)):
    if s[j] in li.keys():
        i = max(li[s[j]], i)
    ans = max(ans, j - i + 1)
    li[s[j]] = j + 1
print(ans)
"""
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print(elapsed_time)
