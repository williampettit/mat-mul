#
#
#

def mat_mul(a, b):
  n = len(a)
  m = len(b[0])
  c = [ [0 for _ in range(m)] for _ in range(n) ]
  for row in range(n):
    u = a[row]
    for col in range(n):
      v = [ b[i][col] for i in range(len(b)) ]
      c[row][col] = sum([ x * y for (x, y) in zip(u, v) ])
  return c

#
#
#

def _get_longest_cell_len(matrix) -> int:
  n = len(matrix)
  m = len(matrix[0])
  longest_cell_len = 0
  for row in range(n):
    for col in range(m):
      cell_str_len = len(str(matrix[row][col]))
      if cell_str_len > longest_cell_len:
        longest_cell_len = cell_str_len
  return longest_cell_len
#
#
#

def mat_str(matrix) -> str:
  n = len(matrix)
  m = len(matrix[0])
  s = ''
  longest_cell_len = _get_longest_cell_len(matrix)
  for row in range(n):
    s += '[ '
    for col in range(m):
      s += f'{matrix[row][col]:{longest_cell_len}}'
      if col < m - 1:
        s += ', '
    s += ' ]'
    if row < n - 1:
        s += '\n'
  return s

#
#
#
    
def main() -> None:
  A = [
  [1, 2, 3],
  [4, 5, 6],
]

  B = [
    [7,  8 ],
    [9,  10],
    [11, 12],
  ]

  C = mat_mul(A, B)

  print(f'A =\n{mat_str(A)}\n')
  print(f'B =\n{mat_str(B)}\n')
  print(f'C =\n{mat_str(C)}\n')

  print('done')

#
#
#
  
if __name__ == '__main__':
  main()
