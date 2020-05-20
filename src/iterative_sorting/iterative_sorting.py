# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for t in range(i, len(arr)):
            print(arr)
            if(arr[smallest_index] > arr[t]):
                smallest_index = t

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr) - 1):
            print(arr)
            if (arr[j] > arr[j+1]):
                x = arr[j]
                arr[j] = arr[j + 1]
                arr[j+1] = x
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    if len(arr) == 0:
        return arr

    if maximum == -1:
        maximum = max(arr)

    buckets = [0 for i in range(maximum+1)]

    for x in arr:
        if x < 0:
            return "Error, negative not allowed"
        buckets[x] += 1
    j = 0
    for i in range(len(buckets)):
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1
