class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        max_len = 0
        left = 0

        # Record the most recent occurence of each 'char' in string 's' along with its
        # most recent index into 'last_seen'.
        # The length of the substring with no repeating characters is stored in
        # 'substring_len'.
        # Code will only check for the length of the next unique substring, i.e. 'substring_len'
        # when the same character is found in 'last_seen'.
        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                # We add 1 to 'left' here because when the for loop restarts,
                # It checks for the next index in 'right'
                left = last_seen[char] + 1

            # Input character into 'last_seen' along with its index
            # For example, if "a" was seen at index 2, then another "a" is
            # seen at index 5, it will override the previous entry.
            # So, "a" most recent occurence is at index 5.
            last_seen[char] = right

            # Calculate the length of the unique substring each time.
            # If it is greater than 'max_len', override its value.
            # We add 1 to the subtraction between 'right' and 'left'
            # to account for the 1 added in the if statement above.
            substring_len = right - left + 1
            if substring_len > max_len:
                max_len = substring_len

        return max_len