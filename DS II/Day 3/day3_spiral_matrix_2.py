class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        su=n**2
        res=[[0 for i in range(n)] for j in range(n)]
        count=(n+1)//2
        cc=1
        k=0
        while k<count and cc<=su:
            for i in range(k,n-k):
                res[k][i]=cc
                cc+=1
            for i in range(k+1,n-1-k):
                res[i][n-1-k]=cc
                cc+=1
            if k!=n-1-k:
                for i in range(k,n-k):
                    res[n-1-k][n-1-i]=cc
                    cc+=1
                for i in range(k+1,n-1-k):
                    res[n-1-i][k]=cc
                    cc+=1
            k+=1
        return res