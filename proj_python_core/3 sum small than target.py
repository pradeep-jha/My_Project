class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n-2):
            # if i>0 and nums[i]==nums[i-1]:
            #     continue
            left,right=i+1,n-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                # if total==target:
                #     left+=1
                #     right-=1
                #     while(left<right) and nums[left]==nums[left-1]:
                #         left+=1
                #     while (left<right) and nums[right]==nums[right+1]:
                #         right-=1
                if total<target:
                    for j in range(right,left,-1):
                        res.append([nums[i],nums[left],nums[j]])
                    left+=1
                    # while (left < right) and nums[left] == nums[left - 1]:
                    #         left += 1
                elif total>=target:
                    right-=1
                    # while (left<right) and nums[right]==nums[right+1]:
                    #     right-=1
        return len(res)

        pass
sol=Solution()
print(sol.threeSumSmaller([0, 0, 0, 0],1))