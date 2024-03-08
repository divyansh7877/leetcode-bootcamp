class Solution:
    def maxArea(self, height: list[int]) -> int:
        '''
        Problem Link: https://leetcode.com/problems/container-with-most-water/description/
        Solved using two pointers.
        '''
        lef=0
        rig=len(height)-1
        max_area=0

        while lef<rig:
            temp_area=(rig-lef)*min(height[lef],height[rig])        #Calculate the area possible
            #rig-left is the base of rectangle area, minimum height is height of 
            if temp_area>max_area:
                max_area=temp_area

            if height[lef]<height[rig]:
                lef+=1
            else:
                rig-=1
        
        return max_area

