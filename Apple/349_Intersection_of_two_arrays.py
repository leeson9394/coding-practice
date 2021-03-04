# leetcode 349. Intersection of Two Arrays

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # use python set function to remove duplicate elements
        res = []
        set1 = set(nums1)
        set2 = set(nums2)
        for item in set1:
            if item in set2:
                res.append(item)
        return res

        # use python dict to remove duplicate elements
        # kv1 = {}
        # kv2 = {}
        # res= []
        # for item in nums1:
        #     kv1[item] = "exist"
        # for item in nums2:
        #     if item in kv1.keys():
        #         kv2[item] = "exist"
        
        # for k in kv2.keys():
        #     res.append(k)
        # return res

nums1 = [4,9,5] 
nums2 = [9,4,9,8,4]
sol = Solution()
result = sol.intersection(nums1,nums2)
print(result)