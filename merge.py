def merge_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError('list1 and list2 must be of type list')
    merged = list1 + list2

    for i in range(len(merged)):
        for j in range(0, len(merged) - i - 1):
            if merged[j] > merged[j + 1]:
                merged[j], merged[j + 1] = merged[j + 1], merged[j]

    return merged







