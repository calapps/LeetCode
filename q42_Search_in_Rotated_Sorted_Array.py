# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)

        left = self.binarySearch(nums[:pivot+1], target)
        right = self.binarySearch(nums[pivot:], target)

        right = right+pivot if right != -1 else -1

        return max(left, right)
            

    def binarySearch(self, nums, target):
        left = 0
        right = len(nums)-1
        print(nums)
        while left <= right:
            mid = left + (right-left) // 2

            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return mid

        return -1

    def findPivot(self, nums):
        # we want to compare everything to the rightmost value in nums becuase that is the comparison wall
        left = 0
        right = len(nums) - 1
        mid = 0
        
        while left <= right:
            mid = left + (right-left) // 2
            
            if nums[mid] < nums[-1]:
                right = mid-1
            
            if nums[mid] > nums[-1]:
                left = mid+1

            if nums[mid] == nums[-1]:
                return mid
        
        return mid


