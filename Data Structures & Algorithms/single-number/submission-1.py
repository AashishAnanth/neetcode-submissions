class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        xor = 0

        for num in nums:
            xor = xor ^ num
        
        return xor