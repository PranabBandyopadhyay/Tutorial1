def draw(row, column):
    h_border = int(row) + 1
    v_border = int(column) + 1

    for i in range(1, h_border):
        print(column * " --- ")
        print(v_border * "|    ")
    print(column * " --- ")
