class Solution:
    def isPalindrome(self, s: str) -> bool:
        sen = ''
        for word in s:
            if word.isalpha() :
                sen += word.lower()
            elif word.isdigit():
                sen += word
        back = sen[::-1]
        return sen == back
        