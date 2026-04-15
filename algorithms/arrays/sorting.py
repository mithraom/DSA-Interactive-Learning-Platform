def bubble_sort_steps(arr):

    arr = arr.copy()
    states = []

    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):

            states.append(arr.copy())

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

                states.append(arr.copy())

    return states


def insertion_sort_steps(arr):

    arr = arr.copy()
    states = []

    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:

            arr[j+1] = arr[j]
            j -= 1
            states.append(arr.copy())

        arr[j+1] = key
        states.append(arr.copy())

    return states


def selection_sort_steps(arr):

    arr = arr.copy()
    states = []

    n = len(arr)

    for i in range(n):

        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        states.append(arr.copy())

    return states