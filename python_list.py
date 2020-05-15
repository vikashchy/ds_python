samplelist = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
# Operations on list
samplelist.insert(9, 6)  # insert an element in list at the specified index
print(samplelist)
print(samplelist.index(1))  # return the index of the value and raise value error if the element is not available
seclist = ['p', 'q', 'r', 'a']
samplelist.extend(seclist)  # extend the list
print(samplelist)
samplelist.remove(1)  # remove value
samplelist.count(2)  # get the count of the element in the list
seclist.sort()  # sort the list
print(samplelist)
samplelist.reverse()  # reverse the list
print(samplelist)
sample_copy = samplelist.copy()  # copy the content of the list
samplelist.clear()  # clear the content of the list
print(samplelist)
print(sample_copy)
print(sample_copy.pop(0))  # pop a element using index
print(sample_copy.pop())  # pop the last element
