column_full = []
row_full = []
box_full = []

one_row = []
one_box = []

column_num = 9
multi = 0

#Puts your input in colums
for column in range(column_num):
    column_input = input()
    column_list = column_input.split()
    column_full.append(column_list)

#Converts columns in rows
for column_choice in range(column_num):
    one_row.clear()
    for first_index_row in range(column_num):
        one_row.append(column_full[first_index_row][column_choice])

    row_full.append(one_row.copy())


#Converts columns in boxes
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






