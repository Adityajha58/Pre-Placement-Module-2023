class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        O(N) solution 
        Detailed graphical explanation:
        https://medium.com/@edward.zhou/leet-code-560-subarray-sum-equals-k-explained-python3-solution-31ab6262615e
        '''
        cnt, total = 0, 0
        cache = {0:1}
        for v in nums:
            total += v
            if cache.get(total-k):
                cnt += cache[total-k]              
            if cache.get(total):
                cache[total] += 1
            else:
                cache[total] = 1
        return cnt