dim1_size = int(input("Enter dimension 1 length: "))
dim2_size = int(input("Enter dimension 2 length: "))
dim3_size = int(input("Enter dimension 3 length: "))
dim1_index = int(input("Enter index for dimension 1: "))
dim2_index = int(input("Enter index for dimension 2: "))
dim3_index = int(input("Enter index for dimension 3: "))

print(dim2_size * dim3_size * dim1_index + dim3_size * dim2_index + dim3_index)
