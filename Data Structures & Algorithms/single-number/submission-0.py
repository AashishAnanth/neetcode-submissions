class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        xor = nums[0]

        for num in nums[1:]:
            xor = xor ^ num
        
        return xor