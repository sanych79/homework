class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lector_name, course, grade):
        if isinstance(lector_name, Lecturer) and \
                (course in self.finished_courses or course in self.courses_in_progress)\
                and course in lector_name.courses_attached:
            if course in lector_name.grades:
                lector_name.grades[course] += [grade]
            else:
                lector_name.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_calc(self):
        caounter = 0
        res = 0
        for x in self.grades.values():
            caounter += 1
            res += sum(x)/len(x)
        return res/len(self.grades)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f' not a member of the class <Student>')
            return
        return self._avg_calc() < other._avg_calc()

    def __str__(self):
        avg = self._avg_calc()
        courses_in_p = ','.join(self.courses_in_progress)
        courses_f = ','.join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя Оценка за домашнее задание:{avg}' \
              f'\nКурсы в процессе обучения:{courses_in_p}\nЗавершенные курсы:{courses_f}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avg_calc(self):
        caounter = 0
        res = 0
        for x in self.grades.values():
            caounter += 1
            res += sum(x)/len(x)
        return res/len(self.grades)

    def __str__(self):
        avg = self._avg_calc()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя Оценка за лекции:{avg}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print(f'{other} is not a member of the class <Mentor>')
            return
        return self._avg_calc() < other._avg_calc()


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}.'
        return res


def StudentsRate(Studets_list, Course):
    """Функция рассчета средней оценки студентов Studets_list по курсу Course"""
    res = 0
    count = 0
    for x in Studets_list:
        for y, z in x.grades.items():
            if y == Course:
                res += sum(z)/len(z)
                count += 1
    if count != 0:
        res /= count
    else:
        print(f'У выбранных студентов нет оценок за курс {Course}')
    return res


def MentorsRate(Mentors_list, Course):
    """Функция рассчета средней оценки Лекторов Mentors_list по курсу Course"""
    res = 0
    count = 0
    for x in Mentors_list:
        for y, z in x.grades.items():
            if y == Course:
                res += sum(z)/len(z)
                count += 1
    if count != 0:
        res /= count
    else:
        print(f'У выбранных лекторов нет оценок за курс {Course}')
    return res


student1 = Student('Ivan', 'Ivanov', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['SQL']
student1.finished_courses += ['MatCad']

student2 = Student('Anna', 'Petrova', 'female')
student2.courses_in_progress += ['MatCad']
student2.courses_in_progress += ['SQL']
student2.finished_courses += ['Python']

mentor_rev1 = Reviewer('Petr', 'Samoylov')
mentor_rev1.courses_attached += ['Python']
mentor_rev1.courses_attached += ['SQL']

mentor_rev2 = Reviewer('Stepan', 'Razin')
mentor_rev2.courses_attached += ['MatCad']

mentor_l1 = Lecturer('Kiril', 'Sidorov')
mentor_l1.courses_attached += ['MatCad']

mentor_l2 = Lecturer('Olga', 'Stepanova')
mentor_l2.courses_attached += ['Python']

mentor_rev1.rate_hw(student1, 'Python', 10)
mentor_rev1.rate_hw(student1, 'Python', 8)
mentor_rev1.rate_hw(student1, 'SQL', 10)

mentor_rev2.rate_hw(student2, 'MatCad', 7)
mentor_rev2.rate_hw(student2, 'MatCad', 10)
mentor_rev2.rate_hw(student2, 'MatCad', 9)
mentor_rev1.rate_hw(student2, 'SQL', 9)
mentor_rev1.rate_hw(student2, 'SQL', 9)

student1.rate_hw(mentor_l1, 'MatCad', 8)
student1.rate_hw(mentor_l1, 'MatCad', 7)
student1.rate_hw(mentor_l1, 'MatCad', 9)
student1.rate_hw(mentor_l2, 'Python', 10)
student1.rate_hw(mentor_l2, 'Python', 9)
student1.rate_hw(mentor_l2, 'Python', 10)

student2.rate_hw(mentor_l1, 'MatCad', 10)
student2.rate_hw(mentor_l1, 'MatCad', 9)

print('----Студенты----')
print(student1)
print(student1.grades)
print(student2)
print(student2.grades)
if student1 > student2:
    print(f'{student1.name} учиться лучше чем {student2.name}')
else:
    print(f'{student2.name} учиться лучше чем {student1.name}')

print('----Преподаватели Лекторы----')

print(mentor_l1)
print(mentor_l1.grades)
print(mentor_l2)
print(mentor_l2.grades)

if mentor_l1 > mentor_l2:
    print(f'{mentor_l1.name} читает лекции лучше чем {mentor_l2.name}')
else:
    print(f'{mentor_l2.name} читает лекции лучше чем {mentor_l1.name}')

print('----Преподаватели проверяющие ДЗ----')

print(mentor_rev1)
print(mentor_rev2)

Student_list = list()
Student_list.append(student1)
Student_list.append(student2)

Course = 'SQL'

print(f'Средняя оценка студентов по курсу {Course} составляет {StudentsRate(Student_list, Course)}')

Mentors_list = list()
Mentors_list.append(mentor_l1)
Mentors_list.append(mentor_l2)

Course = 'MatCad1'

print(f'Средняя оценка лекторов по курсу {Course} составляет {MentorsRate(Mentors_list, Course)}')