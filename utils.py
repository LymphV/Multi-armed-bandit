def lower_bound (array, value):
    first = 0
    length = len(array)
    while length > 0:
        half = length >> 1
        middle = first + half
        if array[middle] < value:
            first = middle + 1
            length = length - half - 1
        else: length = half
    return first

def upper_bound (array, value):
    first = 0
    length = len(array)
    while length > 0:
        half = length >> 1
        middle = first + half
        if value < array[middle]: length = half
        else:
            first = middle + 1
            length = length - half - 1
    return first
