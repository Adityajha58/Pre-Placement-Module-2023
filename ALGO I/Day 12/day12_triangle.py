class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        
        m = len(triangle)
        state = [[triangle[0][0]]]
        for i in range(1,m):
            state.append([0]*(i+1))
            
        for i in range(1,m):
            state[i][0] = triangle[i][0] + state[i-1][0]
            state[i][-1] = triangle[i][-1] + state[i-1][-1]
            
        for i in range(2,m):
            for j in range(1,len(state[i])-1):
                state[i][j] = min(state[i-1][j]+triangle[i][j], state[i-1][j-1]+triangle[i][j])

        return min(state[-1])