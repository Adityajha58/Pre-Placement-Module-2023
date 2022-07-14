class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        B = []
        for number in A:
            B.append(number * number)
        return sorted(B)
        