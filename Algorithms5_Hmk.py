# Sorting
# Selection Sort
# O(n2)


test_list = [11, 4, 7, 1, 2, 3, 5, 14]


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print('\n')
new_list_s = selection_sort(test_list)
print("Selection sorted list********************************************** ")
print("Original:", test_list)
print("Selection Sorted: ", new_list_s)
print("Descending order: ", new_list_s[::-1])


# Bubble Sort
# O(n2)
test_list2 = [11, 2, 4, 7, 3, 9, 1, 8]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print("Bubble Sort***********************************************************")
print("Original:", test_list2)
new_list_b = bubble_sort(test_list2)
print("Bubble Sorted: ", new_list_b)
print("Descending order: ", new_list_b[::-1])
# print("Bubble Sorted: ", bubble_sort(test_list2))


# Insertion Sort
test_list3 = [2, 7, 4, 1, 9, 8, 3, 5]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


result = insertion_sort(test_list3)
print("Insertion sort********************************************************")
print("Original: ", test_list3)
print("Insertion sorted: ", result)
print("Descending order: ", result[::-1])

# Merge Sort

test_list4 = [2, 4, 1, 6, 8, 3, 7, 5]


def merge_arrays(left_arr, right_arr):
    merged_array = []
    i = j = 0

    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j += 1
            continue
        if j == len(left_arr):
            merged_array.append(left_arr[i])
            i += 1
            continue
        if left_arr[i] <= right_arr[j]:
            merged_array.append(left_arr[i])
            i += 1
        else:
            merged_array.append(right_arr[j])
            j += 1
    return merged_array


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


new_list_m = merge_sort(test_list4)
print("Merge Sort***********************************************************")
print("Original: ", test_list4)
print("Merge Sorted: ", new_list_m)
print("Descending order: ", new_list_m[::-1])

# Quick example of recursion
# def recursion(number):
#    if number == 0:
#        return
#    print(number)
#    number -= 1
#    recursion(number)
# recursion(10)
