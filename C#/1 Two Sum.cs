public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var result = new Dictionary<int, int>{};

        // With c = target
        // Given that a + b = c, then a = c - b
        // If a, with its index, has been added to 'result',
        // Then c - b verifies that a is in 'result'

        // Hence, we have the index of a in 'result'
        // And get the index of b which we found by verifying
        // that a is in 'result'.
        for (int i = 0; i < nums.Length; i++){
            if (result.ContainsKey(target - nums[i])){
                return [result[target - nums[i]],i];
            }
            result[nums[i]] = i;
        }
        return null;
    }
}