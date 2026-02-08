class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        print(nums1)
        print(nums2)
        i = j = 0
        res=[]
        while i < len(nums1) and j < len(nums2):
            if nums1[i]==nums2[j]:
                if not res or res[-1]!=nums1[i]:
                 res.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return res
        pass
sol=Solution()
print(sol.intersection([4,9,5],[9,4,9,8,4]))