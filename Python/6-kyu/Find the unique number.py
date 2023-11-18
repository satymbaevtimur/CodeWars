def find_uniq(arr):
    sorted_arr = sorted(arr)

    if sorted_arr[0] == sorted_arr[1]:
        return sorted_arr[-1]
    else:
        return sorted_arr[0]
