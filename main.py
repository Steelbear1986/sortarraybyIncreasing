class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)[::-1]
        nums = Counter(nums)
        h = max(nums.values())
        g = 0
        ansver = []
        while g <= h:
            for k, v in nums.items():
                if v == g:
                    ansver += [k] * v
            g += 1
        return ansver

