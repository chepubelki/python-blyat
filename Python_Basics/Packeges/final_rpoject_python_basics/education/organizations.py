import csv
# from users import Teacher
# from users import Student


class School():
    def __init__(self, name=None, address=None, phone=None, num_stud=None, num_teachers=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.num_stud = num_stud
        self.num_teachers = num_teachers
        self.students = []
        self.teachers = []

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email

    def set_num_stud(self, num_stud):
        self.num_stud = num_stud

    def set_num_teachers(self, num_teachers):
        self.num_teachers = num_teachers

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)

    def get_info(self):  # возвращает словарь с информацией про школу без личной информации студентов / преподавателей
        return {
            'school name': self.name,
            'address': self.address,
            'phone': self.phone,
            'num_stud': self.num_stud,
            'num_teachers': self.num_teachers
        }

    def get_report(self):
        report = []

        # School information
        school_info = [
            self.name,
            self.address,
            self.phone,
            self.num_stud,
            self.num_teachers
        ]
        report.append(school_info)

        # Student information
        for student in self.students:
            student_info = [
                student.name,
                student.familyname,
                student.age,
                student.gender,
                student.nationality,
                student.school,
                ', '.join(student.subjects)
            ]
            report.append(student_info)

        # Teacher information
        for teacher in self.teachers:
            teacher_info = [
                teacher.name,
                teacher.familyname,
                teacher.age,
                teacher.gender,
                teacher.nationality,
                teacher.school,
                ', '.join(teacher.subjects)
            ]
            report.append(teacher_info)

        file_name = f'{self.name}.csv'
        with open(file_name, 'w', newline='') as file:
            df = csv.writer(file)
            df.writerows(report)

            df.close()

        return file_name


# Student(name="John", familyname="Wick", age=35, gender="male",
#         nationality="USA", school="NIS", subjects='Programming, Gym')
# Teacher(name="Nill", familyname="Wolker", age=23, gender="male",
#         nationality="UK", school="№23", subjects='Math, Chemistry')

# 1-5 школа
# -----------
# 6-10 студент
# -----------
# 11-15 учитель
# school1 = School(name="AUPET", address="Almaty, Kazakhstan",
#                  phone="999999", num_stud=1000, num_teachers=50)

# student1 = Student(name="Aldik", familyname="Aidarov", age=20, gender="male",
#                    nationality="Kazakh", school="AUPET", subjects=['Math', 'Programming'])
# student2 = Student(name="Berik", familyname="Yespaev", age=21, gender="male",
#                    nationality="Kazakh", school="AUPET", subjects=['Math', 'Programming'])
# student3 = Student(name="Erbik", familyname="Redjep", age=21, gender="male",
#                    nationality="Kazakh", school="AUPET", subjects=['Math', 'Programming'])
# student4 = Student(name="Timik", familyname="Begzhanov", age=21, gender="male",
#                    nationality="Kazakh", school="AUPET", subjects=['Math', 'Programming'])
# student5 = Student(name="Madik", familyname="Abdizhamal", age=20, gender="male",
#                    nationality="Kazakh", school="AUPET", subjects=['Math', 'Programming'])
# student6 = Student(name="Madik", familyname="Abdizhamal", age=20, gender="male",
#                    nationality="Kazakh", school="AUPET", subjects=['Math', 'Programming'])


# teacher1 = Teacher(name="Jhon", familyname="Smith", age=44, gender="male",
#                    nationality="Kazakh", school="AUPET", subjects=['Chemistry', 'Math'])
# teacher2 = Teacher(name="Jane", familyname="Jhons", age=33, gender="female",
#                    nationality="Russian", school="AUPET", subjects=['Chemistry', 'Math'])
# teacher3 = Teacher(name="Flick", familyname="Flak", age=19, gender="male",
#                    nationality="Russian", school="AUPET", subjects=['Chemistry', 'Math'])
# teacher4 = Teacher(name="Gibi", familyname="Gaba", age=77, gender="female",
#                    nationality="Kazakh", school="AUPET", subjects=['Chemistry', 'Math'])
# teacher5 = Teacher(name="Huba", familyname="Buba", age=55, gender="male",
#                    nationality="Chinese", school="AUPET", subjects=['Chemistry', 'Math'])
# teacher6 = Teacher(name="Huba", familyname="Buba", age=55, gender="male",
#                    nationality="Chinese", school="AUPET", subjects=['Chemistry', 'Math'])


# school1.add_student(student1)
# school1.add_student(student2)
# school1.add_student(student3)
# school1.add_student(student4)
# school1.add_student(student5)
# school1.add_teacher(teacher1)
# school1.add_teacher(teacher2)
# school1.add_teacher(teacher3)
# school1.add_teacher(teacher4)
# school1.add_teacher(teacher5)

# print(school1)

# report_filename = school1.get_report()
# print(f"Report saved to: {report_filename}")
