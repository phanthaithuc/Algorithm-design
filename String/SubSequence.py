# s = "abcde"
# words = ["a", "bb", "acd", "ace"]
from typing import List
from collections import defaultdict
import bisect

s = "dsahjpjauf"
words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]


def subSequence(s: str, words: []) -> bool:
    count = 0
    for t in words:
        if checker(s, t):
            count += 1
    return count


def checker(s: str, words: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(words):
        if words[j] == s[i]:
            j += 1
        i += 1
    return True if j == len(words) else False


def numMatchingSubseq(S: str, words: List[str]) -> int:
    mp = {}
    for i, w in enumerate(words): mp.setdefault(w[0], []).append((i, 0))

    ans = 0
    for c in S:
        for i, k in mp.pop(c, []):
            if k + 1 == len(words[i]):
                ans += 1
            else:
                mp.setdefault(words[i][k + 1], []).append((i, k + 1))
    return ans


print(numMatchingSubseq(s, words))


def matchingSub(S: str, words: List[str]) -> int:
    D = defaultdict(list)
    for i, x in enumerate(S):
        D[x].append(i)

    bisect_right = bisect.bisect_right

    def match(w):
        i = -1
        for x in w:
            k = bisect_right(D[x], i)
            if k == len(D[x]):
                return False
            i = D[x][k]
        return True

    res = 0
    for w in words:
        res += match(w)
    return res


print(matchingSub(s, words))
