def merge_sort(arr):
    if len(arr) > 1:
        # Находим середину массива
        mid = len(arr) // 2

        # Делим массив на две половины
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивно сортируем обе половины
        merge_sort(left_half)
        merge_sort(right_half)

        # Индексы для итерации по подмассивам и исходному массиву
        i = j = k = 0

        # Слияние отсортированных половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Добавляем оставшиеся элементы левой половины, если они есть
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Добавляем оставшиеся элементы правой половины, если они есть
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


# Пример использования
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Отсортированный массив:", sorted_arr)
