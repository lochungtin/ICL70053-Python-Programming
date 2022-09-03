def compute_cumulative_sum(numbers):
    curSum = 0
    rt = []

    for number in numbers:
        curSum += number
        rt.append(curSum)

    return rt


print(compute_cumulative_sum([5, 2, 1, 7, 3, 8]))
