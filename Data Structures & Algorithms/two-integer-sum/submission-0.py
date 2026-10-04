class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        key = defaultdict(int)

        if len(nums) == 2:
            return [0,1]
            
        for i in range(len(nums)):
            if target - nums[i] in key:
                return [key[target - nums[i]], i]
            key[nums[i]] = i