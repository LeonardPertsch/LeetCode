class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        flip = s[::-1]
        index = flip.find(" ")
        if index == -1:
            return len(s)
        loesung = flip[0:index]
        return len(loesung[::-1])