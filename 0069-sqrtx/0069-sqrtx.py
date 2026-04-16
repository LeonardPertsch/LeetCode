class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i= 0
        guess = x
        if x == 0:
            return 0
        x_prev = 0.5 * (x + guess / x)
        while i != 300:
            x_new = 0.5 * (x_prev + guess / x_prev)
            x_prev= x_new
            i += 1
        return int(x_prev)
