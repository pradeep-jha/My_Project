class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        res = []
        n = len(people)
        left, right = 0, n - 1
        while left <= right:
           if people[left] + people[right] <= limit:
                res.append([people[left], people[right]])
                left += 1
                right -= 1

           elif people[right] <= limit:
               res.append([people[right]])
               right -= 1
           else:right-=1
        return len(res)
        pass
sol=Solution()
print(sol.numRescueBoats([2, 1,4,1,3],3))