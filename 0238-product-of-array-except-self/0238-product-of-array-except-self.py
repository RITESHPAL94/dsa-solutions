class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        k = 1
        
        for i in range(len(nums)):
            prefix.append(k)
            k = nums[i] * k

        k = 1
        for i in range(len(nums)-1,-1,-1):
            prefix[i] = prefix[i] * k
            k = nums[i] * k
        return prefix