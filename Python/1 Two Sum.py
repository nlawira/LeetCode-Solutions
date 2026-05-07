class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}

        # With c = target
        # Given that a + b = c, then a = c - b
        # If a, with its index, has been added to 'result',
        # Then c - b verifies that a is in 'result'

        # Hence, we have the index of a in 'result'
        # And get the index of b which we found by verifying
        # that a is in 'result'.
        for i, num in enumerate(nums):
            if target - num in numIndex:
                return numIndex[target-num], i
            numIndex[num] = i