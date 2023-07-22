from typing import List

"""
1) Identify pointer with lesser value
2) Is the pointer value lesser than or equal to max on that side:
        yes -> update max on that side
        no -> get water for pointer value, add total
3) move pointer inwards
4) repeat for the other pointer.
"""
height = [0,1,0,2,1,0,1,3,2,1,2,1]

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        total = 0
        max_l = height[l]
        max_r = height[r]
        while l < r :
            if height[l] <= height[r]:
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    curr = max_l - height[l]
                    total = total + curr
                l += 1
            else:
                if  height[r] > max_r:
                    max_r = height[r]
                else:
                    curr = max_r - height[r]
                    total = total + curr
                r -= 1
        return total

