def quicksort(list_quick):
    less = []
    big = []
    pivot_list = []
    if len(list_quick) <= 1:
        return list_quick
    else:
        pivot = list_quick[0]
        for x in list_quick:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                big.append(x)
            else:
                pivot_list.append(x)

    return quicksort(less) + pivot_list + quicksort(big)


if __name__ == '__main__':
    list_quick = [18, 8, 123, 556, 2, 95, 10, 52, 295, 25, 126, 2]
    list_quick = quicksort(list_quick)
    print(list_quick)
