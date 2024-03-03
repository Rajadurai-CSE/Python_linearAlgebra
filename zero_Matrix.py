def zero_matrix_fun(rows,cols):
  matrix = []
  for i in range(rows):
    for j in range(cols):
      matrix.append(0)
  return matrix

rows = int(input("Enter Number of Rows: "))
cols = int(input("Enter Number of Rows: "))
Zero_Matrix = zero_matrix_fun(rows,cols)
print(Zero_Matrix)

