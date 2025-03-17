#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

class Solution(object):
    def trap(self, height):
        left, right = 0, len(height)-1
        leftmax,rightmax = 0,0
        water=0
        while left<right:
            if leftmax>rightmax:
                if height[right]> rightmax:
                    rightmax=height[right]
                else:
                    water+=rightmax-height[right]
                    right-=1
            else:
                if height[left]> leftmax:
                    leftmax=height[left]
                else:
                    water+=leftmax-height[left]
                    left+=1
        print(water)
        return water

    print(trap)

                   
