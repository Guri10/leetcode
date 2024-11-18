class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1Pointer = m-1
        # nums2Pointer = n-1
        # inputPointer = m+n-1

        # # if m == 0:
        # #     nums1[inputPointer] = nums2[nums2Pointer]

        # while nums2Pointer >= 0 and nums1Pointer >= 0:

        #     if nums1[nums1Pointer] > nums2[nums2Pointer]:
        #         nums1[inputPointer] = nums1[nums1Pointer]        
        #         nums1Pointer -=1
        #     else:
        #         nums1[inputPointer] = nums2[nums2Pointer]
        #         nums2Pointer -=1
        #     inputPointer -=1

        # while nums2Pointer >= 0:
        #     nums1[inputPointer] = nums2[nums2Pointer]
        #     nums2Pointer, inputPointer = nums2Pointer- 1, inputPointer-1












        nums1pt,nums2pt, inpt = m-1,n-1,m+n-1

        while nums1pt>=0 and nums2pt >= 0:
            if nums1[nums1pt] > nums2[nums2pt]:
                nums1[inpt] = nums1[nums1pt]
                nums1pt -=1
            elif nums1[nums1pt] <= nums2[nums2pt]:
                nums1[inpt] = nums2[nums2pt]
                nums2pt -=1
            inpt -=1
        while nums2pt >= 0:
            nums1[inpt] = nums2[nums2pt]
            inpt,nums2pt = inpt-1, nums2pt-1


















