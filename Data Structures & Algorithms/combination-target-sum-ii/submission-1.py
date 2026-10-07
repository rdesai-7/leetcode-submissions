class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, total, nums):
            if total == target:
                res.append(list(nums))
                return
            if i >= len(candidates) or total > target:
                return
            # total < target. need to add some numbers.
            # lets add candidates[i], but removing duplicate work.
            num = candidates[i]
            frequency = freq[num]
            for j in range(0, frequency + 1):
                # add j nums and run dfs. move pointer to next number.
                tup = tuple(num for _ in range(j))
                dfs(i + frequency, total + num * j, nums + tup)

        res = []
        candidates.sort()
        freq = {}
        for c in candidates:
            freq[c] = freq.get(c, 0) + 1
        dfs(0, 0, ())
        return res
