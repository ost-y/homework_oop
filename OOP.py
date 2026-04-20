class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in student.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average_st_grade(self):
        for grade in self.grades.values():
            return sum(grade)/len(grade)

    # self == other
    def __eq__(self, other):
        return self.average_st_grade() == other.average_st_grade()

    # self > other
    def __gt__(self, other):
        return self.average_st_grade() > other.average_st_grade()

    # self < other
    def __lt__(self, other):
        return self.average_st_grade() < other.average_st_grade()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_st_grade():.1f}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}'
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades  = {}

    def average(self):
        for grade in self.grades.values():
            return sum(grade)/len(grade)
    # self == other
    def __eq__(self, other):
        return self.average() == other.average()

    # self > other
    def __gt__(self, other):
        return self.average() > other.average()

    # self < other
    def __lt__(self, other):
        return self.average() < other.average()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average():.1f}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# def average_students(students, course):          # не понимаю, почему не работает...
#     for student in students:
#         av_students = []
#
#         if course in student.grades[course]:
#             av_students.append(student.average_st_grade())
#             return sum(av_students)/len(av_students)
#         print(av_students)


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
some_reviewer = Reviewer('Some','Buddy')
some_lecturer = Lecturer('Some','Buddy')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []


student = Student('Алёхина', 'Ольга', 'Ж')
some_student = Student('Ruoy', 'Eman', 'М')
some_student.finished_courses += ['Введение в программирование']
some_student.courses_in_progress += ['Python', 'Git']
some_lecturer.grades['Python'] = [10,10,10,10,10,10,9]
some_student.grades['Python'] = [10,10,10,10,10,10,9]
student.grades['Python'] = [10,10]
students = [student, some_student]

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
some_lecturer.courses_attached += ['Python']


print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка

print(lecturer.grades)  # {'Python': [7]}
print(some_reviewer)
print(some_lecturer)
print(some_student)
print(student.__eq__(some_student))
print(student.__gt__(some_student))
print(student.__lt__(some_student))
print(lecturer.__eq__(some_lecturer))
print(lecturer.__gt__(some_lecturer))
print(lecturer.__lt__(some_lecturer))
# print(average_students(students, 'Python'))
# print(student.grades)
# print(student.average_st_grade())
# print(some_student.average_st_grade())
# print(students)
