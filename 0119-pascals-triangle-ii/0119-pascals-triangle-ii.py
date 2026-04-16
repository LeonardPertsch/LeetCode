class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        numRows = rowIndex + 1

        result = [[1]]

        for i in range(1, numRows):
            prev = result[-1]
            nextRow = [1]

            for j in range(len(prev) - 1):
                nextRow.append(prev[j] + prev[j + 1])

            nextRow.append(1)
            result.append(nextRow)

        return result[-1]