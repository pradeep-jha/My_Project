class Solution:
    def countSubstrings(self, s):

        res=0
        for i in range(len(s)):
            start,end=0,0
            res+=self.expand(s,i,i)
            res+=self.expand(s,i,i+1)
            # print(res)
        return res

    def expand(self,s, left, right):
            count=0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # print(s[left], s[right])
                count+=1
                left -= 1
                right += 1

            return count

    pass


s=Solution()
print(s.countSubstrings("abccba"))