class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_course(self, course_name):
        if course_name not in self.courses_in_progress:
            self.courses_in_progress.append(course_name)

    def fin_course(self, course_name):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)
            self.finished_courses.append(course_name)

    def leave_course(self, course_name):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 0 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _rating_hw_(self):
        grades = []
        for i in self.grades.values():
            grades += i
        if len(grades) > 0:
            return sum(grades) / len(grades)
        else:
            return 0

    def __str__(self):
        courses_in_progress = '' + ', '.join(self.courses_in_progress)
        finished_courses = '' + ', '.join(self.finished_courses)
        raiting_hw = round(self._rating_hw_(), 1)
        return(
            f'Имя: {self.name}\n' +
            f'Фамилия: {self.surname}\n' +
            f'Средняя оценка за домашние задания: {raiting_hw}\n' +
            f'Курсы в процессе изучения: {courses_in_progress}\n' +
            f'Завершенные курсы: {finished_courses}')

    def _rang_(self):
        all_grades = []
        for val in self.grades.values():
            all_grades += val
        return round(sum(all_grades) / len(all_grades), 1)

    def __cmp__(self, other):
        if isinstance(other, Student):
            if self._rang_() > other._rang_():
                return f'{self.name} {self.surname} успешнее, чем {other.name} {other.surname}'
            elif self._rang_() < other._rang_():
                return f'{self.name} {self.surname} слабее, чем {other.name} {other.surname}'
            else:
                return f'Успехи {self.name} {self.surname} сопоставимы с успехами {other.name} {other.surname}'
        else:
            return f'Нельзя сравнить {self.name} {self.surname} и {other.name} {other.surname}'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_courses(self, course_name):
        self.courses_attached.append(course_name)


class Lecturer(Mentor):
    def __init__(self, *args):
        Mentor.__init__(self, *args)
        self.grades = {}

    def _rating_lec_(self):
        grades = []
        for i in self.grades.values():
            grades += i
        if len(grades) > 0:
            return sum(grades) / len(grades)
        else:
            return 0

    def __str__(self):
        raiting_lec = round(self._rating_lec_(), 1)
        grades = []
        for i in self.grades.values():
            grades += i
        if len(grades) > 0:
            rating = sum(grades) / len(grades)
        else:
            rating = 0
        return(
            f'Имя: {self.name}\n' +
            f'Фамилия: {self.surname}\n' +
            f'Средняя оценка за лекции: {raiting_lec}')
    
    def _rang_(self):
        all_grades = []
        for val in self.grades.values():
            all_grades += val
        return round(sum(all_grades) / len(all_grades), 1)

    def __cmp__(self, other):
        if isinstance(other, Lecturer):
            if self._rang_() > other._rang_():
                return f'{self.name} {self.surname} успешнее, чем {other.name} {other.surname}'
            elif self._rang_() < other._rang_():
                return f'{self.name} {self.surname} слабее, чем {other.name} {other.surname}'
            else:
                return f'Успехи {self.name} {self.surname} сопоставимы с успехами {other.name} {other.surname}'
        else:
            return f'Нельзя сравнить {self.name} {self.surname} и {other.name} {other.surname}'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return(
            f'Имя: {self.name}\n' +
            f'Фамилия: {self.surname}')

# Функция подсчета средней оценки по курсам


def rate_it(lst, name_course, type):
    all_rates = []
    if isinstance(lst, list):
        for i in lst:
            if isinstance(i, type):
                if name_course in i.grades:
                    all_rates += i.grades[name_course]
    elif isinstance(lst, type):
        if name_course in lst.grades:
            all_rates += lst.grades[name_course]
    else:
        return 'Object type not supported'
    if len(all_rates) > 0:
        return round(sum(all_rates) / len(all_rates), 1)
    else:
        return 0


def rate_students(students, name_course):
    return rate_it(students, name_course, Student)


def rate_lecturers(lecturers, name_course):
    return rate_it(lecturers, name_course, Lecturer)


# Создание экземпляров и накидывание методов
lecturer_1 = Lecturer('Volodimir', 'Pushkin')
lecturer_1.add_courses('Python')
lecturer_1.add_courses('Ruby')
lecturer_1.add_courses('TypeScript')

lecturer_2 = Lecturer('Ibrahim', 'Popov')
lecturer_2.add_courses('Html')
lecturer_2.add_courses('JavaScript')
lecturer_2.add_courses('Rust')


reviewer_1 = Reviewer('Ivan', 'Petrov')
reviewer_1.courses_attached += ['Python', 'Html', 'JavaScript']

reviewer_2 = Reviewer('Alex', 'Novak')
reviewer_2.courses_attached += ['Ruby', 'TypeScript', 'Rust']


student_1 = Student('Ruoy', 'Eman', 'Gender')
student_1.courses_in_progress += ['Python', 'JavaScript']
student_1.finished_courses += ['Html']
student_1.add_course('TypeScript')
student_1.fin_course('TypeScript')

student_2 = Student('Gordan', 'Freeman', 'Binary')
student_2.courses_in_progress += ['Python', 'Ruby', 'Html']
student_2.finished_courses += ['Rust']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Ruby', 7)
reviewer_2.rate_hw(student_2, 'Ruby', 5)

student_1.rate_lec(lecturer_1, 'Python', 9)
student_1.rate_lec(lecturer_1, 'Python', 7)
student_2.rate_lec(lecturer_1, 'Python', 10)

student_2.rate_lec(lecturer_2, 'Html', 3)
student_2.rate_lec(lecturer_2, 'Html', 3)
student_1.rate_lec(lecturer_2, 'JavaScript', 5)

# Вывод некоторых методов
print()
print(lecturer_1, '\n')
print(reviewer_1, '\n')
print(student_1, '\n')

print(rate_students([student_1, student_2], 'Python'), '\n')

print(rate_lecturers([lecturer_1, lecturer_2], 'JavaScript'), '\n')
print(rate_lecturers([lecturer_1, lecturer_2], 'Python'), '\n')
print(rate_lecturers(lecturer_2, 'Html'), '\n')

print(rate_lecturers([lecturer_1, 'lecturer_2'], 'Python'), '\n')
print(rate_lecturers(lecturer_2, 'Java'), '\n')
print(rate_lecturers('lecturer_2', 'Java'), '\n')



print(student_1.__cmp__(student_2))
print(student_1.__cmp__(student_1))
print(student_2.__cmp__(student_1))


print(lecturer_1.__cmp__(lecturer_2))
print(lecturer_1.__cmp__(lecturer_1))
print(lecturer_2.__cmp__(lecturer_1))

print(lecturer_1.__cmp__(student_2))
