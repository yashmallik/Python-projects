def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    new = []
    for i in range(len(nums1)):
        pos = False
        for j in nums2[nums2.index(nums1[i])+1:]:
            if nums1[i] < j:
                new.append(j)
                pos = True
                break
        if not pos:
            new.append(-1)
    return new
