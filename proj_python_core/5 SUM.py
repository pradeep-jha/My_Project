class Solution:
    # nums = [1,0,-1,0,-2,2,3], target = 3, k = 5
    # # Output: [[-2,-1,0,2,4], [-2,0,0,1,4], ...]  # compute all unique 5-number sums

    def fiveSum(self, nums: [int], target: int) -> [[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-4):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-3):
                if j> i+1 and nums[j] == nums[ j- 1]:
                    continue
                for k in range(j+1,n-2):
                    if k> j+1 and nums[k] == nums[ k- 1]:
                        continue
                    left,right=k+1,n-1
                    while left<right:
                        total=nums[i]+nums[j]+nums[k]+nums[left]+nums[right]
                        if total==target:
                            res.append([nums[i],nums[j],nums[k],nums[left],nums[right]])
                            left+=1
                            right-=1
                            while left<right and nums[left]==nums[left-1]:
                                left+=1
                            while left<right and nums[right]==nums[right+1]:
                                    right-=1
                        elif total<target:
                            left+=1
                        else:
                            right-=1
        return res
sol=Solution()
print(sol.fiveSum([1,0,-1,0,-2,2,3],3))
