class Solution:
    def calculateCompressedMean(self, quantities:[int]) -> float:
        n=len(quantities)
        # window_sum=sum(quantities[::])
        # print(window_sum)
        # return window_sum/n
        res=[]
        for q in quantities:
            if res and res[-1]==q:
                #print("______________")
                #print(q)
                print(res)
                print("=============")
                res.pop()
            else:
                print("+++++++++========")
                res.append(q)
                print(res)
        print(res)
        if not res:
            return 0.0
        return sum(res) / len(res)
        pass

sol=Solution()

print(sol.calculateCompressedMean([2, 2, 3, 3, 4, 5, 5, 4]))