def identity_matrix_fun(rows,cols):
  """
  The function generates an identity matrix of a specified size.
  
  :param rows: The `rows` parameter specifies the number of rows in the identity matrix. In the provided code snippet, the `identity_matrix_fun` function is creating a square identity matrix based on the `rows` parameter
  :param cols: The `cols` parameter in the `identity_matrix_fun` function represents the number of columns in the identity matrix that the function generates. In the provided code snippet, the function is called with `cols=3`, which means it will create a 3x3 identity matrix
  :return: The code defines a function `identity_matrix_fun` that generates an identity matrix based on the input dimensions `rows` and `cols`. The function creates a list `matrix` and populates it with 1's on the diagonal and 0's elsewhere.
  """
  matrix = []
  c = 0
  for i in range(rows):
    for j in range(cols):
      if c==j:
        matrix.append(1)
      else:
        matrix.append(0)
    c+=1
  return matrix


rows = int(input("Enter Number of Rows: "))
cols = int(input("Enter Number of Rows: "))
if rows!=cols:
  print("Error!! Enter a square matrix")
else:
  identity_matrix = identity_matrix_fun(3,3)
  print(identity_matrix)