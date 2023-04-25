# 1. Write a Python program to remove the intersection of two sets from one set.

set1 = {6, 7, 8, 9}
set2 = {8, 8, 10, 11}
set1 = set1.difference(set2)
print(set1)


# 2. Write a Python program to find the union of two sets.  

list = [{2, 4, 3, 1,}, {3, 6, 8, 7, 2}, {1, 10, 6, 11}]
print("original is : " + str(list))
ans = set()
 
for s in list:
    ans.update(s)
 
print("The union is:", ans)


# 3. Write a Python program to count the number of occurrences of an element in a tuple.

tuple = (12, 43, 40, 56, 43, 12, 31, 34, 65, 12)
x = [i for i in tuple if i == 12]
print("12 occurs", len(x), "times")


# 4. Write a Python program to find the maximum and minimum element in a set.

def Max (set):
    return(max(set))
x = set([23, 75, 34, 43, 21, 65])
print(Max(x))


def Min(set):
    return (min(set))
a = set([12, 9, 13, 11, 5])
print(Min(a))

# 5. Write a Python function to find the common elements between two tuples.

def common (a, b):
    ans = [i for i in a if i in b]
    return ans
a = [2, 5, 6, 4, 8]
b = [9, 1, 8, 10]
print(common(a, b))



#                             takeaway keys
# 1. You can access elements of a tuple using indexing or slicing.

# 2. Sets can only contain unique elements, which means they automatically remove duplicates.

# 3. Sets are often used for removing duplicates from a list, or for checking if two lists have any common elements.
