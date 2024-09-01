def selection_sort(arr):
    # Проходим по каждому элементу массива
    for i in range(len(arr)):
        # Предполагаем, что текущий элемент минимальный
        min_idx = i
        # Проходим по оставшейся части массива для поиска минимального элемента
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем местами текущий элемент с найденным минимальным элементом
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Пример использования
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Отсортированный массив:", sorted_arr)
