# implementing bubble sotr
def bubble_sort(items):
    n = len(items)
    for i in range(n):
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


items = [5, 3, 8, 1, 9, 2]
sorted_items = bubble_sort(items)
print(sorted_items)
