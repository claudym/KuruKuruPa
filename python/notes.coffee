<Python Crash Course>{

1>'Variables and data types':
  #Think of variables as labels you can assign to values
  #A variable references a certain value

  #strings
  msg= "I'm a string"
  msg= 'I am "your father" string'
  msg_f= f"I'm a f-string: {msg}"
  #integers
  num_int= 3
  large_number= 35_000_000 #underscore is ignored while saving value
  #float
  fl= 3.14

  #multiple assignment
  x, y, z = 1, 2, 3

2>'Lists':
  #ordered collection of items
  lt= ['soy', 'una', 'lista']

  #modify elements
  lt[1]= 'otra'
  #add elements
  lt.append('nueva')          #appends element at the end of the list
  lt.insert(index, 'listica') #inserts element at specified index
  #remove elements
  del lt[index]     #delete element at index
  lt.pop()          #delete and return last element
  lt.pop(index)     #delete and return element at index
  lt.remove(value)  #delete element with value
  #sorting
  lt.sort()             #sorts the list lt (changes lt initial reference)
  lt.sort(reverse=True) #sorts lt in reverse order
  new_lt= sorted(lt)    #sorted() returns a sorted list
  #reversing
  lt.reverse()  #reverses the order of lt without sorting
  #length
  len(lt) #len()

  #slicing
  lt= ['cake', 'cookie', 'cracker', 'crouton']
  lt[:1]  #returns ['cake', 'cookie']
  lt[1:2] #returns ['cookie', 'cracker']
  lt[1:]  #returns ['cookie', 'cracker', 'crouton']

3>'Tuples':
  #immutable lists
  tp_single= ('alone',) #single tupple needs a comma
  tp= ('se', 'tiro', 'el', 'COBA')

  #accessing
  >>> tp[3]
  'COBA'
  #only count() and index() methods
  >>> tp.count('COBA')
  1
  >>> tp.index('COBA')
  3

4>'Looping':
  trees= ['cherry', 'apple', 'pear']
  #for loop:
  for tree in tree: #for every `tree` in `trees`
    print(tree)
  
  #range(start, end, increment)
  range(1, 5)     #returns list [1, 2, 3, 4]
  range(2, 11, 2) #returns list [2, 4, 6, 8, 10] 
  #for with range()
  for value in range(1, 5):
    print(value)
  
  #list comprehensions
  #combine the for loop and the creation of new elements into one line and automatically append each new element
  >>> [val**2 for val in range(1, 11)]
  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

  #copying a list
  lt_foods= ['pizza', 'falafel', 'rice']
  lt_foods_copy= lt_foods[:]  #a slice without indices
}