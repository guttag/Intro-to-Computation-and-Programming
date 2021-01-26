# -*- coding: utf-8 -*-

# # Code from page 179
class Toy(object):
    def __init__(self):
        self._elems = []
    def add(self, new_elems):
        """new_elems is a list"""
        self._elems += new_elems
    def size(self):
        return len(self._elems)

# print(type(Toy))
# print(type(Toy.__init__), type(Toy.add), type(Toy.size))

# # Code from page 180
# t1 = Toy()
# print(type(t1))
# print(type(t1.add))
# t2 = Toy()
# print(t1 is t2) #test for object identity

# # Code from page 181
# t1 = Toy()
# t2 = Toy()
# t1.add([3, 4])
# t2.add([4])
# print(t1.size() + t2.size())

# # Figure 10-1 from page 182
class Int_set(object):
    """An Int_set is a set of integers"""
    #Information about the implementation (not the abstraction):
      #Value of a set is represented by a list of ints, self._vals.
      #Each int in a set occurs in self._vals exactly once.

    def __init__(self):
        """Create an empty set of integers"""
        self._vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self._vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def get_members(self):
        """Returns a list containing the elements of self._
           Nothing can be assumed about the order of the elements"""
        return self._vals[:]
    
    def union(self, other):
        """other is an Int_set
           mutates self so that it contains exactly the elemnts in self
           plus the elements in other."""

    def __str__(self):
        """Returns a string representation of self"""
        if self._vals == []:
            return '{}'
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}'
  
# # Code from page 183
# s = Int_set()
# s.insert(3)
# print(s.member(3))

# # Code from page 184
# s = Int_set()
# s.insert(3)
# s.insert(4)
# print(str(s))
# print('The value of s is', s)

# # Header for finger exercise on page 184
def union(self, other):
    """other is an Int_set
    mutates self so that it contains exactly the elemnts in self
    plus the elements in other."""

# # Figure 10-2 on page 185
class Toy(object):
    def __init__(self):
        self._elems = []
    def add(self, new_elems):
        """new_elems is a list"""
        self._elems += new_elems
    def __len__(self):
        return len(self._elems)
    def __add__(self, other):
        new_toy = Toy()
        new_toy._elems = self._elems + other._elems
        return new_toy
    def __eq__(self, other):
        return self._elems == other._elems
    def __str__(self):
        return str(self._elems)
    def __hash__(self):
        return id(self)
    
# t1 = Toy()
# t2 = Toy()
# t1.add([1, 2])
# t2.add([3, 4])
# t3 = t1 + t2
# print('The value of t3 is', t3)
# print('The length of t3 is', len(t3))
# d = {t1: 'A', t2: 'B'}
# print('The value', d[t1], 'is associated with the key t1 in d.')

# # Import used for class Person        
import datetime

# # Figure 10-3 from page 189
class Person(object):
    
    def __init__(self, name):
        """Assumes name a string. Create a person"""
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank+1:]
        except:
            self._last_name = name
        self.birthday = None
        
    def get_name(self):
        """Returns self's full name"""
        return self._name
    
    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name
    
    def set_birthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
           Sets self's birthday to birthdate"""
        self._birthday = birthdate
        
    def get_age(self):
        """Returns self's current age in days"""
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days
    
    def __lt__(self, other):
        """Assume other a Person
           Returns True if self precedes other in alphabetical
           order, and False otherwise. Comparison is based on last
           names, but if these are the same full names are
           compared."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name
    
    def __str__(self):
        """Returns self's name"""
        return self._name

# # Code from page 188
# me = Person('Michael Guttag')
# him = Person('Barack Hussein Obama')
# her = Person('Madonna')
# print(him.get_last_name())
# him.set_birthday(datetime.date(1961, 8, 4))
# her.set_birthday(datetime.date(1958, 8, 16))
# print(him.get_name(), 'is', him.get_age(), 'days old')

# # Code from page 190
# p_list = [me, him, her]
# for p in p_list:
#     print(p)
# p_list.sort()
# for p in p_list:
#     print(p)

# # Figure 10-4 from page 192
class MIT_person(Person):
    
    _next_id_num = 0 #identification number
    
    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1
        
    def get_id_num(self):
        return self._id_num
    
    def __lt__(self, other):
        return self._id_num < other._id_num

# # Code from page 192
# p1 = MIT_person('Barbara Beaver')
# print(str(p1) + '\'s id number is ' + str(p1.get_id_num()))

# # Code from page 193
p1 = MIT_person('Mark Guttag')
p2 = MIT_person('Billy Bob Beaver')
p3 = MIT_person('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')

# print('p1 < p2 =', p1 < p2)
# print('p3 < p2 =', p3 < p2)
# print('p4 < p1 =', p4 < p1)

# print('p1 < p4 =', p1 < p4)

# Finger exercise from page 194
class Politician(Person):
    """ A politician is a person that can belong to a political party"""
    
    def __init__(self, name, party = None):
        """name and party are strings"""
    
    def get_party(self):
        """returns the party to which self belongs"""
    
    def might_agree(self, other):
        """returns True if self and other belong to the same part
             or at least one of then does not belong to a party"""
    
# # Figure 10-5 from page 194
class Student(MIT_person):
    pass

class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self._year = class_year
    def get_class(self):
        return self._year
    
class Grad(Student):
    pass

# # Code from page 195
# p5 = Grad('Buzz Aldrin')
# p6 = UG('Billy Beaver', 1984)
# print(p5, 'is a graduate student is', type(p5) == Grad)
# print(p5, 'is an undergraduate student is', type(p5) == UG)

# # Code from page 195 -- Should be added to class MIT_Person
def is_student(self):
    return isinstance(self, Student)

# print(p5, 'is a student is', p5.is_student())
# print(p6, 'is a student is', p6.is_student())
# print(p3, 'is a student is', p3.is_student())

# # Code from page 196
class Transfer_student(Student):

    def __init__(self, name, from_school):
        MIT_person.__init__(self, name)
        self._from_school = from_school

    def get_old_school(self):
        return self._from_school

# # Figure 10-6 from page 198
class Grades(object):

    def __init__(self):
        """Create empty grade book"""
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self._students:
            raise ValueError('Duplicate student')
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False

    def add_grade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def get_grades(self, student):
        """Return a list of grades for student"""
        try:
            return self._grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')

    def get_students(self):
        """Return a sorted list of the students in the grade book"""
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        return self._students[:]
    
    # def get_students(self): #new version from later in chapter
    #     """Return the students in the grade book one at a time
    #        in alphabetical order"""
    #     if not self._is_sorted:
    #         self._students.sort()
    #         self._is_sorted = True
    #     for s in self._students:
    #         yield s

# # Code from page 197
# course = Grades()
# course.add_student(Grad('Bernie'))
# all_students = course.get_students()
# all_students.append(Grad('Liz'))

# # Figure 10-7 from page 199        
def grade_report(course):
    """Assumes course is of type Grades"""
    report = ''
    for s in course.get_students():
        tot = 0.0
        num_grades = 0
        for g in course.get_grades(s):
            tot += g
            num_grades += 1
        try:
            average = tot/num_grades
            report = f"{report}\n{s}'s mean grade is {average}"
        except ZeroDivisionError:
            report = f"{report}\n{s} has no grades"
    return report

# ug1 = UG('Jane Doe', 2021)
# ug2 = UG('Pierce Addison', 2041)
# ug3 = UG('David Henry', 2003)
# g1 = Grad('Billy Buckner')
# g2 = Grad('Bucky F. Dent')
# six_hundred = Grades()
# six_hundred.add_student(ug1)
# six_hundred.add_student(ug2)
# six_hundred.add_student(g1)
# six_hundred.add_student(g2)
# for s in six_hundred.get_students():
#     six_hundred.add_grade(s, 75)
# six_hundred.add_grade(g1, 25)
# six_hundred.add_grade(g2, 100)
# six_hundred.add_student(ug3)
# print(grade_report(six_hundred))
       
# # Figure 10-8 from page 201
class info_hiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__also_visible__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'    
        
    def print_visible(self):
        print(self.visible)
        
    def print_invisible(self):
        print(self.__invisible)
        
    def __print_invisible(self):
        print(self.__invisible)
        
    def __print_invisible__(self):
        print(self.__invisible)

# # Code from page 201
# test = info_hiding()
# print(test.visible)
# print(test.__also_visible__)
# print(test.__invisible)

# test = info_hiding()
# test.print_invisible()
# test.__print_invisible__()
# test.__print_invisible()

# # Code from page 202
class Sub_class(info_hiding):
    def new_print_invisible(self):
        print(self.__invisible)       

# test_sub = Sub_class()
# test_sub.new_print_invisible()

# # Figure 10-9 from page 204 is embedded as a comment in code for Figue 10-7

# # Code from page 205 
# book = Grades()
# book.add_student(Grad('Julie'))
# book.add_student(Grad('Lisa'))
# for s in book.get_students():
#     print(s)

# # Finger exercise from page 205
def get_students_above(self, grade):
    """Return the students a mean grade > g one at a time"""

# # Figure 10-10 from page 208
def find_payment(loan, r, m):
    """Assumes: loan and r are floats, m an int
       Returns the monthly payment for a mortgage of size
       loan at a monthly rate of r for m months"""
    return loan*((r*(1+r)**m)/((1+r)**m - 1))
    
class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""
    def __init__(self, loan, ann_rate, months): 
        """Assumes: loan and ann_rate are floats, months an int
        Creates a new mortgage of size loan, duration months, and
        annual rate ann_rate"""
        self._loan = loan
        self._rate = ann_rate/12
        self._months = months
        self._paid = [0.0]
        self._outstanding = [loan]
        self._payment = find_payment(loan, self._rate, months)
        self._legend = None #description of mortgage
        
    def make_payment(self):
        """Make a payment"""
        self._paid.append(self._payment)
        reduction = self._payment - self._outstanding[-1]*self._rate
        self._outstanding.append(self._outstanding[-1] - reduction)
        
    def get_total_paid(self):
        """Return the total amount paid so far"""
        return sum(self._paid)
        
    def __str__(self):
        return self._legend

# Figure 10-11 from page 211
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self._legend = f'Fixed, {r*100:.1f}%'
        
class Fixed_with_pts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self._pts = pts
        self._paid = [loan*(pts/100)]
        self._legend = f'Fixed, {r*100:.1f}%, {pts} points'

class Two_rate(Mortgage):
    def __init__(self, loan, r, months, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self._teaser_months = teaser_months
        self._teaser_rate = teaser_rate
        self._nextRate = r/12
        self._legend = (f'{100*teaser_rate:.1f}% for ' +
                f'{self._teaser_months} months, then {100*r:.1f}%')
        
    def make_payment(self):
        if len(self._paid) == self._teaser_months + 1:
            self._rate = self._nextRate
            self._payment = find_payment(self._outstanding[-1],
                                self._rate,
                                self._months - self._teaser_months)
        Mortgage.make_payment(self)

def compare_mortgages(amt, years, fixed_rate, pts, pts_rate,
                     var_rate1, var_rate2, var_months):
    tot_months = years*12
    fixed1 = Fixed(amt, fixed_rate, tot_months)
    fixed2 = Fixed_with_pts(amt, pts_rate, tot_months, pts)
    two_rate = Two_rate(amt, var_rate2, tot_months, var_rate1,
                      var_months)
    morts = [fixed1, fixed2, two_rate]
    for m in range(tot_months):
        for mort in morts:
            mort.make_payment()
    for m in morts:
        print(m)
        print(f' Total payments = ${m.get_total_paid():,.0f}')

# # Code from page 210
# compare_mortgages(amt=200000, years=30, fixed_rate=0.035,
#                   pts = 2, pts_rate=0.03, var_rate1=0.03,
#                   var_rate2=0.05, var_months=60)
