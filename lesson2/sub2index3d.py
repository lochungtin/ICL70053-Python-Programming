dim1_size = int(input("Enter dimension 1 length: "))
dim2_size = int(input("Enter dimension 2 length: "))
dim3_size = int(input("Enter dimension 3 length: "))
index = int(input("Enter index: "))

dim1_area = dim2_size * dim3_size
dim1_plane_index = index % dim1_area

print(
    "({}, {}, {})".format(
        index // dim1_area,
        dim1_plane_index // dim3_size,
        dim1_plane_index % dim3_size,
    )
)
