class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[c]:
                    return False

        return stack == []