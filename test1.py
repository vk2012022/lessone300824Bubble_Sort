def quick_sort(s):
    if len(s) <= 1:
        return s

    element = s[0]
    left = list(filter(lambda i: i < element, s))
    center = [i for i in s if i == element]
    right = list(filter(lambda i: i > element, s))

    return quick_sort(left) + center + quick_sort(right)


print(quick_sort([5, 2, 9, 0, 1, 5, 3]))

# Результат: [0, 1, 2, 3, 5, 5, 9]