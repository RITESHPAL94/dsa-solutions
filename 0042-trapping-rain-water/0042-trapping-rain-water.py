class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        left_height = 0
        right_height = 0
        water = 0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=left_height:
                    left_height = height[left]
                else:
                    water += left_height - height[left]
                left +=1
            else:
                if height[right] >=right_height:
                    right_height = height[right]
                else:
                    water += right_height - height[right]
                right -=1
        return water