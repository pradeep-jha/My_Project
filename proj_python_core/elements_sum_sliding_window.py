nums=[5,2,8,14,10,-2,50,-29,100,4,25]
k=3
def sum_elements(l,k):
    sorted_nums=sorted(nums)
    print(sorted_nums)
    max_sum =0

    for i in range(len(sorted_nums)-k+1):

        # print(i,sorted_cars[i])
        # print(sorted_cars[i+k-1],sorted_cars[i])
        #below commented code is the solution,if we need to sum all the element of given window size k***********-----
        print("window-",i+1)
        sumofele = 0
        j=i
        while (j<=i+k-1):
            sumofele+=sorted_nums[j]
            j+=1
        print("sum of elements", sumofele)

        # tmp=sorted_nums[i+k-1]-sorted_nums[i]
        # print("tmp-->",tmp)
        if(sumofele>max_sum):
            max_sum=sumofele
    return ("maximum sum of element in window of size K --->",max_sum)

print(sum_elements(nums,k))