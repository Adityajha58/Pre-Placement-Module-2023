class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def fill(i):
            if isConnected[i][i] == 0:
                return
            isConnected[i][i] = 0
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    fill(j)
        cnt = 0
        for i in range(len(isConnected)):
            if isConnected[i][i]:
                cnt += 1
                fill(i)
        return cnt