row_size = int(input("Enter the number of rows: "))
col_size = int(input("Enter the number of columns: "))
index = int(input("Enter index: "))

print("({}, {})".format(index // col_size, index % col_size))
