def missing_number(nums: list[int]):
    lenght = len(nums)
    actual_value = lenght*(lenght+1)/2
    original_value = sum(nums)
    missing = actual_value-original_value
    return int(missing)


print(missing_number([0, 2, 3, 4, 5, 6]))
