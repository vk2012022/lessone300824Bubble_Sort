a = [-3, 5, 0, -8, 1, 10]

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insert_sort(a)
print(a)
# Результат: [-8, -3, 0, 1, 5, 10]