class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        right -=1
        return res

sol=Solution()
print(sol.fourSum([1, 0, -1, 0, -2, 2],0))
print(sol.fourSum([2, 2, 2, 2, 2],8))
print(sol.fourSum([1, 2, 3, 4],100))
print(sol.fourSum([0, 0, 0, 0],0))
print(sol.fourSum([-3, -1, 0, 2, 4, 5],2))