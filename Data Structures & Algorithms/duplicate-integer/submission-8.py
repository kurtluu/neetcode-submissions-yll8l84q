class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = set()

        for n in nums:
            if n not in prev:
                prev.add(n)
            else:
                return True
        return False