'''
Created on Mar 18, 2018

@author: fereydounb
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums2 = list(set(nums))
        print nums2
        if nums == nums2:
            print nums, "\n", nums2
            return False
        else:
            return True
s = Solution()
nums = [1,2,3,4,5,6,6]
print s.containsDuplicate(nums)
