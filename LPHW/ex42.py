## Animal is-a object (yes, sort of confusing) Look at the extra credit
class Animal(object):
  pass

## Dog is-a animal
class Dog(Animal):

  def __init__(self, name):
    self.name = name

## Cat is-a Animal
class Cat(Animal):

  def __init__(self, name):
    self.name = name

## Person is-a object
class Person(object):

  def __init__(self, name):
    self.name = name
    self.pet = None

## 
class Employee(Person):

  def __init__(self, name, salary):
    ## ?? hmm what is this strange magic?
    super(Employee, self).__init__(name)
    self.salary = salary

## Fish is-a object
class Fish(object):
  pass

## Salmon is-a fish
class Salmon(Fish):
  pass

## Halibut is-a fish
class Halibut(Fish)
  pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## fran is-a Employee and has-a salary of 120000
frank = Employee("Frank", 120000)

## fran has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
