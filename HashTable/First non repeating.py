s = "leetcode"
import collections

d = collections.defaultdict(int)

for words in s:
    d[words] += 1

for key, value in d.items():
    if value == 1:
        print(key)
        break
