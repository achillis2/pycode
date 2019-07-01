# 33. 搜索旋转排序数组
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return -1

        l = 0
        r = size - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[r]:
                # nums[mid + 1:r] 包括左右区间端点有序
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # nums[l:mid - 1] 包括左右区间端点有序
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
