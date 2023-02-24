from itertools import permutations

column_full = []
row_full = []
box_full = []

one_row = []
one_box = []

column_num = 9
multi = 0

# Missing Numbers
all_num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
anl_clone = all_num_list
unwanted = []


# Puts your input in columns
for column in range(column_num):
    column_input = input()
    column_list = column_input.split()
    column_full.append(column_list)


# Converts columns in rows
for column_choice in range(column_num):
    one_row.clear()
    for first_index_row in range(column_num):
        one_row.append(column_full[first_index_row][column_choice])

    row_full.append(one_row.copy())


# Converts columns in boxes
for box_columns in range(9):
    one_box.clear()
    for box in range(3):
        for first_index_box in range(3):
            one_box.append(column_full[box][first_index_box + multi])

    box_full.append(one_box.copy())

    if len(box_full) == 3:
        multi = 3

    if len(box_full) == 6:
        multi = 6


for search_for_num in range(len(all_num_list)):
    if anl_clone[search_for_num] in column_full[0]:
        unwanted.append(anl_clone[search_for_num])

for destroy in range(len(unwanted)):
    anl_clone.remove(unwanted[destroy])

print(anl_clone)


# ˇˇA sudoku example ˇˇ
"""
3 X X 8 X 1 X X 2
2 X 1 X 3 X 6 X 4
X X X 2 X 4 X X X
8 X 9 X X X 1 X 6
X 6 X X X X X 5 X
7 X 2 X X X 4 X 9
X X X 5 X 9 X X X
9 X 4 X 8 X 7 X 5
6 X X 1 X 7 X X 3
"""


