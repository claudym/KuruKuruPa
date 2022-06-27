def oper(fct, s):
  return fct(s)

def diag_1_sym(s):
  return pretty_print(diag_1_sym_matrix(s))

def diag_1_sym_matrix(s):
  matrix = build_matrix(s)
  new_matrix = []
  elem = []

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      elem.append(matrix[j][i])
    new_matrix.append(elem)
    elem = [] 
  return new_matrix

def rot_90_clock(s):
  return pretty_print(rot_90_clock_matrix(s))

def rot_90_clock_matrix(s):
  matrix = build_matrix(s)
  new_matrix = []
  elem = []
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      elem.append(matrix[-j-1][i])
    new_matrix.append(elem)
    elem = []
  return new_matrix

def selfie_and_diag1(s):
  selfie_matrix = build_matrix(s)
  diag_matrix = diag_1_sym_matrix(s)
  new_matrix = []
  elem = []

  for i in range(len(selfie_matrix)):
    for ch in selfie_matrix[i]:
      elem.append(ch)
    elem.append('|')
    for ch in diag_matrix[i]:
      elem.append(ch)
    new_matrix.append(elem)
    elem = []
  return pretty_print(new_matrix)

def build_matrix(s):
  matrix = []
  elem= []
  for i in range(len(s)):
    if s[i] != '\n':
      elem.append(s[i]) 
    else:
      matrix.append(elem)
      elem= []
  matrix.append(elem)
  return matrix

def pretty_print(matrix):
  str_line = ''
  str_matrix = []
  for elem in matrix:
    str_line = ''.join(elem)
    str_matrix.append(str_line)
 
  return '\n'.join(str_matrix)
  

s = "abcd\nefgh\nijkl\nmnop"
# print(s)

# print(rot_90_clock(s))
# print(diag_1_sym(s))
# print(selfie_and_diag1(s))
print(oper(diag_1_sym, s))
print(oper(rot_90_clock, s))
print(oper(selfie_and_diag1, s))