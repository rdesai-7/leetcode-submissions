class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def total(a,b,c):
            return nums[a]+nums[b]+nums[c]
        nums.sort()
        sols = []
        for i in range(len(nums)):
            num = nums[i]
            if i == 0 or num != nums[i-1]:
                
                j = i+1
                k = len(nums)-1
 

                while j < k:  
                    t = total(i,j,k)
                    if t < 0:
                        j += 1
                    elif t > 0: 
                        k -= 1
                    else:
                        sol = [nums[i],nums[j],nums[k]]
                        sols.append(sol)
                        j += 1
                        while j<k and nums[j] == nums[j-1]:
                            j += 1

        return sols