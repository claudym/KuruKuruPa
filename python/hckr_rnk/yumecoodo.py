class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __repr__(self):
        return f'Person({self.name}, {self.last_name})'

import datetime

class Student(Person):
    def __init__(self, name, last_name, birth_year, birth_month, birth_day):
        super().__init__(name, last_name)
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
    
    def adult(self):
        date_now = datetime.date.today()
        birthdate = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        delta = date_now - birthdate
        if delta.days//365 >= 18:
            return True
        return False
    
    def age(self):
        date_now = datetime.date.today()
        birthdate = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        delta = date_now - birthdate
        return delta.days//365

    def __repr__(self):
        return f'Student({self.name}, {self.last_name}, {self.birth_year}-{self.birth_month}-{self.birth_day})'


class Professor(Person):
    def __init__(self, name, last_name, salary):
        super().__init__(name, last_name)
        self.salary = salary

    def __repr__(self):
        return f'Professor({self.name}, {self.last_name}, {self.salary})'

# app or test
if __name__ == '__main__':
    jason = Student('Jason', 'Mars', 1980, 12, 4)
    students = []
    students.append(jason)
    students.append(Student('Carl', 'Max', 1990, 7, 3))
    students.append(Student('Joy', 'Smith', 2015, 3, 2))

    adult_students = [student for student in students if student.adult()]
    adult_students.sort(key=lambda student: (student.age(), student.name, student.last_name), reverse=True)
    print(adult_students)
