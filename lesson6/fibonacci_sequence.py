def generate_fibonacci(length):
    rt = []
    for i in range(length):
        if i < 2:
            rt.append(i)
        else:
            rt.append(rt[i - 1] + rt[i - 2])

    return rt


print(generate_fibonacci(10))
