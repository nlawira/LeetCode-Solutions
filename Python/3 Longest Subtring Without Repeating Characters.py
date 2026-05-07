class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_list = list()
        for i in range(0, len(s), 1):
            counter = 1
            for j in range(i, len(s)-1, 1):
                if s[j+1] in s[i:j+1]:
                    break
                else:
                    counter += 1
                    continue
            count_list.append(counter)
        return 0 if s == "" else max(count_list)
