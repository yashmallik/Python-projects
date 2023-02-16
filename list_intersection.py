def intersection(nums1, nums2):
    list_intersected = []
    for num in nums1:
        if num in nums2:
            list_intersected.append(num)
            nums2.remove(num)
    return list_intersected


num1 = [1, 2, 3, 4, 5, 4]
num2 = [1, 2, 2, 4, 4]
print(intersection(num1, num2))
