class Solution:
    # nums = [2, 7, 11, 15]
    # target = 9
    def twoSum(self, nums: [int], target: int) -> [[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        res = []
        left,right=0,n-1
        while left<right:
            total=nums[left]+nums[right]
            if total==target:
                res.append([nums[left],nums[right]])
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]:
                        left+=1
                while left<right and nums[left]==nums[right+1]:
                        right-=1
            elif total<target:
                    left+=1
            else:
                right-=1
        return res

sol=Solution()
print(sol.twoSum([2, 7, 11, 15,4,5,3,6,1,8],11))