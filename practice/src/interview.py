'''
Created on Mar 16, 2018

@author: fereydounb
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)+1):
            if nums[i] == nums[i-1]:
                nums.pop(i-1)
                print nums
        return len(nums)
    
if __name__ == '__maine__':
    nums = [1,1,2]
    s = Solution()
    s.removeDuplicates(nums)
    print nums