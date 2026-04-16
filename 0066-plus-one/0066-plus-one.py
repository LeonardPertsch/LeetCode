class Solution(object):
    def plusOne(self, digits):
        flip = digits[::-1]
        flip[0] += 1

        for i in range(len(flip)):
            if flip[i] == 10:
                flip[i] = 0
                if i + 1 < len(flip):
                    flip[i + 1] += 1
                else:
                    flip.append(1)

        return flip[::-1]