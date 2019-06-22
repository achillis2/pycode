# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
#              or index number 5 where the peak element is 6.
# Note:
#
# Your solution should be in logarithmic complexity.


def findPeakElement(nums):
    #
    # Write your code here.
    #
    val = -1
    for i in range(0,len(nums)):
        if i>=0 and i<len(nums)-1:
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                val = i
                break

    if val == -1:
        return 'not found'
    else:
        return val
    # left, right = 0, len(nums) - 1
    #
    # while left < right:
    #     mid = int(left + (right - left)/2)
    #     if nums[mid] > nums[mid + 1]:
    #         right = mid
    #     else:
    #         left = mid + 1

    # return left

if __name__ == '__main__':

    # nums = [1,2,3,1,4,5,6,5,3,7,6,9]
    nums = [1,2,3,4]
    result = findPeakElement(nums)
    print(result)
