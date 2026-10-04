class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import random

        while True:
            choice = random.choice(nums)
            if nums.count(choice) > len(nums) // 2:
                return choice