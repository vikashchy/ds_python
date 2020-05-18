def selection_sort(elements):
    for i in range(len(elements) - 1):
        min_index = i
        for j in range(i + 1, len(elements)):
            if elements[min_index] > elements[j]:
                min_index = j
        elements[i], elements[min_index] = elements[min_index], elements[i]
    return elements


ele = [23, 35, 6, 42, 1, 4, 6, 97, 10]
print(selection_sort(ele))
