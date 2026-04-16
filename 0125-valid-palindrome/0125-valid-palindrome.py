class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = s.strip()
        s = "".join(ch for ch in s if ch.isalnum())

        reverse = s[::-1]
        return s == reverse
