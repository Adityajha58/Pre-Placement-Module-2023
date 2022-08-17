class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        res = 0
        t = 1
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                res += t
                t += 1
            else:
                t = 1
        return res