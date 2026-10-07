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
                        while j < len(nums) and nums[j-1] == nums[j]:
                            j += 1
                        
                    else:
                        if t == 0:
                            sol = [nums[i],nums[j],nums[k]]
                            sols.append(sol)
                        k -= 1
                        while k>0 and nums[k+1] == nums[k]:
                            k -= 1

        return sols