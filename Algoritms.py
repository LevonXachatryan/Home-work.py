def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

array = [64 ,34 ,66, 12, 69]
sort_array = buble_sort(array)
print(sort_array)

#Task 2
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
array_selection = [33, 55, 76, 2, 64]
sort_array_selection = selection_sort(array_selection)
print(sort_array_selection)