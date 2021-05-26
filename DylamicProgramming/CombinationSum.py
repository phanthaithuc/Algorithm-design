from typing import List


def CombinationSum(candidate: List[int], target: int) -> List[int]:
    res = [[] for _ in range(target + 1)]

    for c in candidate:
        for i in range(1, target + 1):
            if i < c:
                continue
            if i == c:
                res[i].append([c])
            else:
                for blist in res[i - c]:
                    res[i].append(blist + [c])

    return len(res[target])


print(CombinationSum([1,2,4], 7))
