def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # левый = 2*i + 1
    right = 2 * i + 2  # правый = 2*i + 2

    # Если левый дочерний элемент больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый дочерний элемент больше корня
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # меняем местами

        # Рекурсивно heapify поддерево
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # перемещаем текущий корень в конец
        heapify(arr, i, 0)  # вызываем heapify на уменьшенной куче

    return arr

# Пример использования
arr = [12, -11, -13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("Отсортированный массив:", sorted_arr)
