class Solution:

    def __init__(self, nums: List[int]):
        self.original_nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original_nums
       
    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffle_nums = [0 for i in range(0, len(self.original_nums))]
        
        new_positions = set()
        
        for i in range(0, len(self.original_nums)):
            num = self.original_nums[i]

            new_position = randint(0, len(self.original_nums) - 1)
            while new_position in new_positions:
                new_position = randint(0, len(self.original_nums) - 1)
    
            new_positions.add(new_position)
            shuffle_nums[new_position] = num
    
        return shuffle_nums 