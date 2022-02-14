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
  lt[:1]  #returns ['cake']
  lt[1:3] #returns ['cookie', 'cracker']
  lt[1:]  #returns ['cookie', 'cracker', 'crouton']

  #copying a list
  lt_foods= ['pizza', 'falafel', 'rice']
  lt_foods_copy= lt_foods[:]  #a slice without indices
  
  #nesting
  #list of list
  lt_of_lst = [[1,2], [3,4]]
  #list of dictionaries
  lt_dict = [{'name': 'billy', 'age': 8}, {'name': 'mandy', 'age': 10}]


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


4>'Dictionaries':
  #a set of key: value pairs, with the keys being unique (within one dict.)
  appleDict= {
    'color': 'green',
    'flavor': 'sweet'
  }
  
  #empty dict assignment
  emptyDict = {}

  #accessing (throws KeyError exception if key is not in dict)
  appleDict['flavor']          #returns value 'sweet'
  #accesing with get()
  appleDict.get('flavah')      #returns None
  appleDict.get('flavah', 'TT')#returns 'TT'

  #modifying
  appleDict['flavor'] = 'tart'  #{'color': 'green', 'flavor': 'tart'}
  #adding elements:
  appleDict['weight'] = 125     #{'color': 'green', 'flavor': 'tart', 'weight': 125}
  #removing elements:
  del appleDict['weight']       #{'color': 'green', 'flavor': 'tart'} 

  #in keyword
  >>> 'blue' in appleDict       # or 'blue' in appleDict.keys()
  False

  #nesting
  #list in dict
  pizza = {
    'crust': 'thick',
    'toppings': ['pineapple', 'ham']
  }
  #dict in dict
  users = {
    'efermi': {
      'first': 'enrico',
      'last': 'fermi'
    },
    'aeinstein': {
      'first': 'albert',
      'last': 'einstein'
    }
  }


5>'Sets':
  #an unordered collection with unique items
  s_lang = {'english', 'portuguese', 'latin'}
  #empty
  s_lang = set()  # {} is a empty dict


6>'Looping':
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
  #combine the for loop and the creation of new elements into one line 
  #and automatically append each new element
  >>> [val**2 for val in range(1, 11)]
  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

  #dictionaries
  user = {
    'username': 'yurameshi',
    'first': 'yusuke',
    'last': 'urameshi'
  }
  #looping through all key:value pairs
  for key, value in user.items():
    print(f'\nKey: {key}')
    print(f'\nValue: {value}')
  #looping through all keys
  for key in user:   # or: for key in user.keys():
    print(f'key: {key}')
  #looping through all values
  for value in user.values():
    print(f'value: {value}')
  
  #while
  message = ''
  while message != 'quit':  #this will run while message is not equal to 'quit'
    message = input('Give me your message!')
    print(message)
  #break
  while True:
    print("I'm infinite")
    wish = input('Do you wanna quit? (yes/no)? ')
    if wish.lower() == 'yes':
      break   #this will exit the loop
  #continue
  num = 0
  while num < 10:
    num += 1
    if num % 2 == 0:
      continue  #loop will go to the next iteration
    print(num)

  #remove all instances of specific values from a list
  while 'cat' in pets:
    pets.remove('cat')

7>'Conditional testing':
  #if statements provide a conditional test
  if conditional_test:
    do_something
  elif conditional_test_2:
    do_another_thing
  else:
    do_something_else
  
  #boolean operators:
  and, or, not
  #comparison operators:
  ==, !=, <, <=, >, >=

  #in keyword
  #check if value inside list
  lt=['cat', 'dog', 'rat']
  if 'rat' in lt:
    print('so nasty xD')
  #check if value not inside list
  if 'rat' not in lt:
    print('clean!')
  

8>'User input':
  #input() pauses the program and waits for the user to enter some text
  name = input('Please enter your name: ')

  #explicit casting
  height= int('9') #converts it to an integer


9>'Functions':
  #named blocks of code designed to do one specific job

  #function definition
  def greetings(username):  #username is the parameter
    """Greet a user"""  #doctring comment: describe what the function does
    print(f'Hola {username}')  
  #function call  
  greetings('alexa')  #'alexa' is the argument

  #positional arguments
  def describe_pet(pet_name, animal_type):
    print(f"My {animal_type}'s name is {pet_name.title()}.")
  describe_pet('lengo', 'cat')  #prints  `My cat's name is Lengo`
  #positional arguments - arbitrary number: *args
  def make_pizza(*toppings): #makes an empty tuple and packs all values there
  print('\nMaking a pizza with the following toppings:')
  for topping in toppings:
    print(f'- {topping}')
  #mixing positional and arbitrary arguments
  def make_pizza(size, *toppings) #*toppings must go at the end

  #keyword arguments
  describe_pet(animal_type='dog', pet_name='freya') #prints `My dog's name is Freya`
  #keyboard arguments - arbitrary number: *kwargs
  #accept as may key=value pairs as the calling statement provides
  def build_profile(first, last, **user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user
  user_profile = build_profile('albert', 'einstein', 
                                location='princeton' 
                                field='physics')
  
  #default values
  def describe_pet(pet_name, animal_type='dragon'): #default values at end of function
  print(f"My {animal_type}'s name is {pet_name.title()}.")
  describe_pet(pet_name='freya')  #prints `My dragon's name is Freya`

  #return values
  def get_formatted_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()
  musician = get_formatted_name('rick', 'sanchez')
  print(musician) 

  #send copy of a list
  def function_name(list_name[:])

  #modules: functions stored in a separate file
  #########
  #importing an entire module
  import module   #use: module.function()
  #importing specific function(s)
  from module import function_0, function_1
  #import with alias in module
  import module as mod  #use: mod.function()
  #import with alias in function
  from module import function as func   #use: func() 
  #import all functions in a module
  from module import *  #use function name (discouraged)


10>'Classes (OOP)':
  #In object-oriented programming you write classes that represent real-world
  #things and situations, and you create objects based on these classes

  #class name in PascalCase
  class Dog:
    
    #runs automatically whenever a new instance of the class Dog is created
    def __init__(self, name, age):  #self is passed automatically
      self.name = name  #attributes: self.name and self.age will be available
      self.age = age    #to every method in the class and instantiated objects
      self.fav_food = 'chicken' #default value for attribute
    
    def sit(self):  #methods
      print(f'{self.name} is now sitting.')
    def roll_over(self):
      print(f'{self.name} rolled over!')
    def update_fav_food(self, fav_food):
      self.fav_food = fav_food

  #making an instance
  doggie = Dog('billie', 3)
  #accessing attributes
  doggie.name
  #calling methods
  doggie.sit()
  #modifying attribute directly
  doggie.fav_food = 'burger'
  #modifying attribute through a method
  doggie.update_fav_food('falafel')

  #inheritance
  ############
  #__init__() method for a child class
  class Car: #parent class (car.py)
    def __init__(self, make, model, year):
    #...
    def fill_gas_tank(self):
    #fill gas tank
  class Battery:
    #...
    def describe_battery(self, battery_size=75):
      #battery description
  class ElectricCar(Car): #child class
    def __init__(self, make, model, year):
      super().__init__(make, model, year) #calls __init__() from parent class
      self.battery = Battery()  #has-a relationship (composition)
    def fill_gas_tank() #method overriding
    #do nothing at all with gas
  
  #importing classes
  from car import Car, ElectricCar

  #property and setter decorators (pythonic way):
  class OurClass:
      def __init__(self, a):
          self.OurAtt = a
      @property
      def OurAtt(self):
          return self.__OurAtt
      @OurAtt.setter
      def OurAtt(self, val):
          if val < 0:
              self.__OurAtt = 0
          elif val > 1000:
              self.__OurAtt = 1000
          else:
              self.__OurAtt = val
  x = OurClass(10)
  print(x.OurAtt)

11>'Files':
  #reading
  ########
  #reading entire file
  with open('file_name') as file_object:
    contents = file_object.read()
  print(contents) #this would print contents of whole file
  #reading line by line
  with open('file_name') as file_object:
    for line in file_object:
      print(line.rstrip())
  #reading to list of lines
  with open('file_name') as file_object:
    lines = file_object.readlines()
  
  #writing
  ########
  #writing to an empty file
  with open('file_name', 'w') as file_object:
    file_object.write("I love programming")
  #writing multiple lines
  with open('file_name', 'w') as file_object:
    file_object.write('programmingが好き!\n')
    file_object.write('ゲームも好き\n')

  #appending
  ##########
  with open(filename, 'a') as file_object:
    file_object.write('machine learning too\n')
    file_object.write("and don't forget the backend xD\n")

  #json dumping
  #############
  import json

  numbers = [2, 3, 5, 7, 11, 13]
  with open('numbers.json', 'w') as f:
    json.dump(numbers, f)
  
  #json loading
  #############
  with open('numbers.json') as f:
    numbers = json.load(f)


12>'Exceptions':
  #special objects to manage errors that arise during a program's execution

  #ZeroDivisionError Exception
  try:
    print(3/0)
  except ZeroDivisionError:
    print("that's a no no")

  #FileNotFoundError Exception
  filename = 'alice.txt'
  try:  #only include code that might throw an exception
    with open(filename, encoding='utf-8') as f:
      contents = f.read()
  except FileNotFoundError: #exception handling
    print(f"sorry TT {filename} file doesn't exist") 
  else: #the rest of the code where no exception might happen
    print(f"The file {filename} has about {len(contents.split())} words.")


13>'Testing':

}