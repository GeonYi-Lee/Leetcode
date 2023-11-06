class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        word_list = []
        for i in range(len(s)):
            if s[i] not in word_list:
                word_list.append(s[i])
            else:
                ans = max(ans, int(len(word_list)))
                word_list.append(s[i])
                word_list = word_list[word_list.index(s[i])+1:]
        ans = max(ans, int(len(word_list)))
        return ans






        
        
        