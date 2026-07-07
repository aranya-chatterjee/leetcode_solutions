class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = m - 1
        r1 = m + n - 1
        r2 = n - 1

        while l >= 0 and r2 >= 0:
            if nums1[l] > nums2[r2]:
                nums1[r1] = nums1[l]
                l -= 1
            else:
                nums1[r1] = nums2[r2]
                r2 -= 1
            r1 -= 1

        while r2 >= 0:
            nums1[r1] = nums2[r2]
            r1 -= 1
            r2 -= 1