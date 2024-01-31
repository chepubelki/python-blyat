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

        return file_name
