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
        
        return (f'Имя:{self.name}\n'
                f'Фамилия:{self.surname}\n'
                f'Средняя оценка за домашнее задание:{avg_grade:.1f}\n'
                f'Курсы в процессе изучения:{courses_in_progress}\n'
                f'Завершенные курсы:{finished_courses}')
    
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
                f'Фамилия {self.surname}')

class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calc_average_grade(self):
        '''Метод подсчета средней оценки от студентов по курсу'''
        if not self.grades:
            return 0.0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades) if all_grades else 0.0
        
    def __str__(self):
        avg_grade = self.calc_average_grade()
        return (f'Имя:{self.name}\n'
                f'Фамилия:{self.surname}\n'
                f'Средняя оценка за лекции:{avg_grade:.1f}')    
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка сравнения'
        return self.calc_average_grade() < other.calc_average_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка сравнения'
        return self.calc_average_grade() == other.calc_average_grade()
