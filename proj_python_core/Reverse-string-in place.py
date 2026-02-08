def reverseString(s):
    n = len(s)
    left, right = 0, n - 1
    while(left<right):
        # print("------------------")
        # print(s[left], s[right])
        s[left], s[right] = s[right], s[left]
        # print("----================--------------")
        # print(s[left], s[right])
        left += 1
        right -= 1
    return s

print(reverseString(["H", "aq", "prad", "n", "a", "h"]))