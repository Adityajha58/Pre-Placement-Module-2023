class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = set() # set can have only distinct elements
        for i in range(len(nums)):
            if nums[i] not in a:
                a.add(nums[i])
            else:
                return True
        return False