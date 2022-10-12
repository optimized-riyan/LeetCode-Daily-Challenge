class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        p3 = n - 3
        p2 = n - 2
        p1 = n - 1
        
        while p3 >= 0 and nums[p2] + nums[p3] <= nums[p1]:
            p1 = p2
            p2 = p3
            p3 -= 1
            
        if p3 < 0:
            return 0
        else:
            return nums[p1] + nums[p2] + nums[p3]