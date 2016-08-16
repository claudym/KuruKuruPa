class Student(Person):
  def __init__(self, firstName, lastName, idNumber, scores):
    self.firstName = firstName
    self.lastName = lastName
    self.idNumber = idNumber
    self.scores = scores

  def calculate(self):
    av = 0
    for arr_i in self.scores:
      av += arr_i
    av /= len(self.scores)

    if(av < 40):
      return "T"
    elif(av < 55):
      return "D"
    elif(av < 70):
      return "P"    
    elif(av < 80):
      return "A"    
    elif(av < 90):
      return "E"    
    else:
      return "O"