class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}

        for i, num in enumerate(nums):
            if target - num in numIndex:
                return numIndex[target-num], i
            numIndex[num] = i