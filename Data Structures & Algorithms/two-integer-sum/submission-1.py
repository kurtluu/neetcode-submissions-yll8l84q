class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashT = {}
        for i, num in enumerate(nums):
            complement = target - num
            print("i: ", i, num, complement)
            print(hashT) 

            if complement in hashT:
                return [hashT[complement], i]
            hashT[num] = i