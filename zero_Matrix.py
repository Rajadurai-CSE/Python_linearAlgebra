def zero_matrix_fun(rows,cols):
  """
  The function creates a zero matrix of a specified number of rows and columns.
  
  :param rows: The `rows` parameter in the `zero_matrix_fun` function represents the number of rows in the matrix that you want to create. It is used to specify the size of the matrix along the vertical dimension
  :param cols: The `cols` parameter in the `zero_matrix_fun` function represents the number of columns in the matrix that will be created. It is used to specify the width of the matrix
  :return: A matrix filled with zeros of size rows x cols is being returned.
  """
  
  matrix = []
  for i in range(rows):
    for j in range(cols):
      matrix.append(0)
  return matrix

rows = int(input("Enter Number of Rows: "))
cols = int(input("Enter Number of Rows: "))
if rows!=cols:
  print("Error!! Enter a square matrix")
else:
  zero_matrix = zero_matrix_fun(rows,cols)
  print(zero_matrix)
