#coding=utf-8

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        # for i in range(k):
        #     temp = nums[-1]
        #     for j in range(len(nums)-1, -1, -1):
        #         nums[j] = nums[j-1]
        #     nums[0] = temp
        # return nums

        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        return nums

if __name__ == '__main__':
    s = Solution()
    aa = [1,2,3,4,5,6,7]
    print s.rotate(aa, 3)