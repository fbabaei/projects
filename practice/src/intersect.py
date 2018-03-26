'''
Created on Mar 19, 2018

@author: fereydounb
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """ 
        nums3 = []
        n1 = [x for x in nums1 if x in nums2] 
        n2 = [x for x in nums2 if x in nums1]
        for i in list(set(n1)):
            if nums1.count(i) > nums2.count(i):
                for j in range(nums2.count(i)):
                    nums3.append(i)
            else:
                for j in range(nums1.count(i)):
                    nums3.append(i)                
        return nums3
s = Solution()
nums1 = [1,2,3,4,5,2,3,4,5,6]
nums2 = [2,3,4,2,3,4,5,2,3]
print s.intersect(nums1, nums2)