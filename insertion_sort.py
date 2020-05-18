def insertion_sort(elements):
    for i in range(len(elements)):
        value = elements[i]
        while elements[i - 1] > value and i > 0:
            elements[i] = elements[i - 1]
            i -= 1
            elements[i] = value
    return elements


ele = [23, 35, 6, 42, 1, 4, 6, 97, 10]
print(insertion_sort(ele))
