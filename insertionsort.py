# implementing insertion sort
def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j - 1]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1
    return items


items = [5, 3, 8, 1, 9, 2]
print(insertion_sort(items))
