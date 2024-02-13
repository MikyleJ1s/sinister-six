# Python | Cloning or Copying a list
def clone_a_list(arraylist):
    return arraylist.copy()

# Python | Count occurrences of an element in a list
def number_of_occurrences_in_a_list(n, arraylist):
    return arraylist.count(n)
    
# Python | Remove empty tuples from a list
def remove_empty_tuples_from_list(arraylist):
    output = []
    for i in arraylist:
        if len(i) != 0:
            output.append(i)
    return output

# Python | Program to print duplicates from a list of integers
def remove_duplicates_from_list(original):
    duplicates = []
    uniques = []
    
    for i in original:
        if i not in uniques:
            uniques.append(i)
        else:
            if i not in duplicates:
                duplicates.append(i)
    return duplicates
