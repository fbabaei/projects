'''
Created on Mar 17, 2018

@author: fereydounb
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 1
        nums2 = []
        while i <= k:
            nums2.insert(0, nums.pop())
            print nums2
            i = i+1
        return nums2 + nums  
if __name__ == "__main__":  
    S = Solution()
    nums = [1,2,3,4,5,6,7,8,9]
    k = 3
    print S.rotate(nums, k)
    