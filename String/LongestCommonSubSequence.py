import numpy as np


def longestCommonSubsequence(str1: str, str2: str) -> int:
    dp = [[0 for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]
    for i in range(len(str1) - 1, -1, -1):
        for j in range(len(str2) - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"

    # w = len(text1) + 1
    # h = len(text2) + 1
    # matrix = [[0 for x in range(w)] for _ in range(h)]
    # matrix[0][1] = 1
    # matrix[1][1] = 2
    # print(matrix)

    print(longestCommonSubsequence(text1, text2))
