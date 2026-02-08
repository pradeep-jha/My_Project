def removeDuplicates(A):
        seen = dict
        {}
        res = []
        for i in range(len(A)):
            if i > 0 and A[i] == A[i - 1]:
                continue
            else:
                res.append(A[i])
        return len(res)

print(removeDuplicates([1, 1, 2,2,2,3,3,3,4,4]))