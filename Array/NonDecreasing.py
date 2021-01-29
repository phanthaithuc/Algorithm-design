class Solution(object):
    def checkPossibility(self, A):
        one = A[:]
        two = A[:]
        for i in range(len(A)-1):
            if(A[i]>A[i+1]):
                del one[i]
                del two[i+1]
                break
        return two == sorted(two) or one == sorted(one)

if __name__ == "__main__":
    check = Solution()
    print(check.checkPossibility([5,4,3,3,5,6,7]))
