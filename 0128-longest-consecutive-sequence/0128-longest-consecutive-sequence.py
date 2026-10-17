class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        l = set(nums)
        s = 0
        for num in l:
            if num-1 not in l:
                count = 1

                while count + num in l:
                    count += 1
                s = max(count,s)
        return s