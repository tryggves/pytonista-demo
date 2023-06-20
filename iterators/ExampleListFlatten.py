#
# Flatten list of lists
#

def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list

my_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

fl = flatten_extend(my_matrix)
print(fl)