import collections

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = collections.defaultdict(list)

# for i in strs:
#     string = i
#     tup = tuple(sorted(i))
#     print("string =", string, ", tuple=", tup)
#

def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.items()


class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


print(groupAnagrams(strs))
obj = Solution
print(obj.groupAnagrams(strs))
