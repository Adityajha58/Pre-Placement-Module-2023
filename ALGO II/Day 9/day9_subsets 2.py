class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[], [nums[0]]]
        tmp = [[nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                tmp = [t + [nums[i]] for t in tmp]
            else:
                tmp = [t + [nums[i]] for t in res]
            res += tmp
        return res