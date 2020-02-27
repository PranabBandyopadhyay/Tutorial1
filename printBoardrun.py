def draw(row, column, array):
    h_border = int(row) + 1
    v_border = int(column) + 1

    for i in range(1, h_border):
        print(column * " --- ")
        for j in range(0, v_border-1):
            print("|  " + str(array[i-1][j]) + " ", end ="")
        print("|")
    print(column * " --- ")