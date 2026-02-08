class Solution:
    def reverseWords(self, s):
        s_new=s.split()
        n=len(s_new)
        s_revered=[]
        # print(s_new)
        # print(" ".join(s.split()[::-1]))
        # Method-2#################less effcient
        # for i in range(n-1,-1,-1):
        #     if s_new[i]=='':
        #         continue
        #     s_revered.append(s_new[i])


        return (" ".join(s.split()[::-1]))
        pass



sol=Solution()
print(sol.reverseWords("the sky is blue"))
print(sol.reverseWords(" hello world "))