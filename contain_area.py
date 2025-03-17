# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

class Solution(object):
    def maxArea(self, height):
        start = 0
        end = len(height)-1
        area = 0
        while start < end:
            area = max(area, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start +=1
            else:
                end -=1
        return area