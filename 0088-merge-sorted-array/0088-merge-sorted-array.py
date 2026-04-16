class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) > m:
            nums1.pop()
        while len(nums2) > n:
            nums2.pop()

        # Bubblesort
        nums1.extend(nums2)
        sorted = False
        if len(nums1) <= 1:
            return nums1
        i = 0
        while i < len(nums1) -1 :
                if nums1[i] > nums1[i + 1]:
                    nums1[i], nums1[i + 1] = nums1[i + 1], nums1[i]
                    i = 0
                else:
                    i = i +1

        return nums1