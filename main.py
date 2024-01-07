with open('integer_list.txt') as data_file:
    nbr_array = []
    for i in data_file.readlines():
        nbr_array.append(int(i.strip('\n')))

inversions_count = 0


def count_inversions(array: list[int]) -> list[int]:
    global inversions_count

    arr_len = len(array)
    half_len = arr_len // 2
    if arr_len < 2:
        return array

    a = count_inversions(array[:half_len])
    b = count_inversions(array[half_len:])

    sorted_list = []

    for j in range(arr_len):
        if len(b) == 0 or (len(a) != 0 and a[0] <= b[0]):
            sorted_list.append(a[0])
            a.pop(0)
        else:
            sorted_list.append(b[0])
            inversions_count += len(a)
            b.pop(0)

    return sorted_list


# Answer = 2407905288
print(count_inversions(nbr_array))
print(inversions_count)
