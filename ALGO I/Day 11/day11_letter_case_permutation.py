class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        S = S.lower()
        lenS, ans = len(S), []
        def dfs(i, res=''):
            if i < lenS:
                dfs(i+1, res + S[i])
                if S[i].islower(): dfs(i+1, res + S[i].upper())
            else: ans.append(res)
        dfs(0)
        return ans