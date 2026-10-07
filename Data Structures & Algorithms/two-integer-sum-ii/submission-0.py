class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers)-1
        while a < b:
            twosum = numbers[a] + numbers[b]
            if twosum == target:
                return [a+1,b+1]
            elif twosum > target:
                b-=1
            else:
                a+=1