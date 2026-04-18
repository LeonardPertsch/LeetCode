class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        unique_values = list(set(nums))
        for i in range(len(unique_values)):
            counter = 0
            for j in range(len(nums)):
                if unique_values[i] == nums[j]:
                    counter +=1
            if counter > len(nums)/2:
                return unique_values[i]
        return 0