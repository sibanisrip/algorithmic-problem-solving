class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for nums in nums1:
            if nums in nums2:
                result.append(nums)
                nums2.remove(nums)
        return result