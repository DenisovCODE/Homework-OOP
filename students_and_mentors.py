class Student:
     
    def __init__(self, name, surname, gender): # инициализация
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
          
    def rate_lecture(self, lecturer, course, grade):
        '''Метод выставления оценки лекторам'''            
        if (not isinstance(lecturer, Lecturer) 
            or not isinstance(grade, int) or grade < 1 or grade > 10):
            return 'Ошибка'
             
        if (course in self.courses_in_progress
            and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
              
    def __str__(self): # Приводим отображение к более удобному выводу
        avg_grade = self.calc_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задание: {avg_grade:.1f}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')
    
    def calc_average_grade(self):
        '''Метод подсчета средней оценки за домашние задания'''
        if not self.grades:
            return 0.0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades) if all_grades else 0.0
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка сравнения'
        return self.calc_average_grade() < other.calc_average_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка сравнения'
        return self.calc_average_grade() == other.calc_average_grade()
          
class Mentor:
    
    def __init__(self, name, surname): # Инициализация
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
        
    def rate_hw(self, student, course, grade):
        '''Метод выставления оценки студентам курса''' 
        if (isinstance(student, Student) and course
            in self.courses_attached and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self): # Приводим отображение к более удобному выводу
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calc_average_grade(self):
        '''Метод подсчета средней оценки от студентов'''
        if not self.grades:
            return 0.0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades) if all_grades else 0.0
        
    def __str__(self):
        avg_grade = self.calc_average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg_grade:.1f}')    
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка сравнения'
        return self.calc_average_grade() < other.calc_average_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка сравнения'
        return self.calc_average_grade() == other.calc_average_grade()

student1 = Student('Ivan', 'Ivanov', 'M')
student1.courses_in_progress += ['Python', 'GIT']
student1.finished_courses += ['Introduction to programming']
    
student2 = Student('Maria', 'Petrova', 'F')
student2.courses_in_progress += ['SQL', 'GIT']
student2.finished_courses += ['Web design']

reviewer1 = Reviewer('Oleg', 'Olegov')
reviewer1.courses_attached += ['Python', 'SQL']

reviewer2 = Reviewer('Vasiliy', 'Vasiliev')
reviewer2.courses_attached += ['GIT', 'Python']

lecturer1 = Lecturer('Maxim', 'Maximov')
lecturer1.courses_attached += ['Python', 'GIT']

lecturer2 = Lecturer('Aleksandr', 'Aleksandrov')
lecturer2.courses_attached += ['SQL', 'Python']

student1.rate_lecture(lecturer2, 'Python', 5)
student1.rate_lecture(lecturer1, 'GIT', 9)
student1.rate_lecture(lecturer1, 'GIT', 6)
student1.rate_lecture(lecturer1, 'Python', 4)
student1.rate_lecture(lecturer2, 'Python', 4)
student2.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer1, 'Python', 5)
student2.rate_lecture(lecturer2, 'SQL', 7)
student2.rate_lecture(lecturer2, 'SQL', 8)
print(student1.rate_lecture(lecturer1, 'SQL', 10)) # ОШИБКА: У лектора нет курса SQL

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 7)
reviewer2.rate_hw(student1, 'GIT', 6)
reviewer2.rate_hw(student1, 'GIT', 9)
reviewer1.rate_hw(student2, 'SQL', 8)
reviewer1.rate_hw(student2, 'SQL', 4)
reviewer2.rate_hw(student2, 'GIT', 8)
reviewer2.rate_hw(student2, 'GIT', 6)
print(reviewer1.rate_hw(student1, 'SQL', 10)) # ОШИБКА: У студента нет курса SQL

print('===НАШИ СТУДЕНТЫ===')
print(student1)
print()
print(student2)
print()
print('===НАШИ ПРОВЕРЯЮЩИЕ===')
print(reviewer1)
print()
print(reviewer2)
print()
print('===НАШИ ЛЕКТОРЫ===')
print(lecturer1)
print()
print(lecturer2)

print(f"\n{student1.name} > {student2.name}: {student1 > student2}")
print(f"{student1.name} < {student2.name}: {student1 < student2}")

print(f"\n{lecturer1.name} > {lecturer2.name}: {lecturer1 > lecturer2}")
print(f"{lecturer1.name} < {lecturer2.name}: {lecturer1 < lecturer2}")

def average_grade_for_students(students_list, course_name):
    '''
    Подсчет средней оценки за домашние задания всех студентов на конкретном курсе
    '''
    total_grades = []
    for student in students_list:
        if course_name in student.grades:
            total_grades.extend(student.grades[course_name])
    
    if not total_grades:
        return 0.0
    return sum(total_grades) / len(total_grades)

def average_grade_for_lecturers(lecturers_list, course_name):
    '''
    Подсчет средней оценки за лекции всех лекторов на конкретном курсе
    
    '''
    total_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            total_grades.extend(lecturer.grades[course_name])
    
    if not total_grades:
        return 0.0
    return sum(total_grades) / len(total_grades)

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]
course_python = average_grade_for_students(students_list, 'Python')
course_sql = average_grade_for_students(students_list, 'SQL')
course_git = average_grade_for_students(students_list, 'GIT')

print(f"\nСредняя оценка студентов на курсе Python: {course_python:.1f}")
print(f"\nСредняя оценка студентов на курсе SQL: {course_sql:.1f}")
print(f"\nСредняя оценка студентов на курсе GIT: {course_git:.1f}")

lecturer_course_python = average_grade_for_lecturers(lecturers_list, 'Python')
lecturer_course_sql = average_grade_for_lecturers(lecturers_list, 'SQL')
lecturer_course_git = average_grade_for_lecturers(lecturers_list, 'GIT')

print(f"\nСредняя оценка лекторов на курсе Python: {lecturer_course_python:.1f}")
print(f"\nСредняя оценка лекторов на курсе SQL: {lecturer_course_sql:.1f}")
print(f"\nСредняя оценка лекторов на курсе GIT: {lecturer_course_git:.1f}")