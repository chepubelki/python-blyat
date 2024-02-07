class Human:
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None):
        self.name = name
        self.familyname = familyname
        self.age = age
        self.gender = gender
        self.nationality = nationality

    def __eq__(self, other):
        if type(other) is type(self):
            return (
                self.name == other.name and
                self.familyname == other.familyname and
                self.age == other.age and
                self.gender == other.gender and
                self.nationality == other.nationality
            )
        else:
            return False

    def __hash__(self):
        return hash(self.name, self.familyname, self.age, self.gender, self.nationality)

    def set_name(self, name=None):
        self.name = name

    def set_family(self, familyname=None):
        self.familyname = familyname

    def set_age(self, age=None):
        self.age = age

    def set_gender(self, gender=None):
        self.gender = gender

    def set_nationality(self, nationality=None):
        self.nationality = nationality

    @staticmethod
    def get_info():
        return 'This class created a Human'


class Student(Human):
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, subjects=None):
        super().__init__(
            name=name,
            familyname=familyname,
            age=age,
            gender=gender,
            nationality=nationality
        )
        self.school = school
        self.subjects = subjects

    def __eq__(self, other):
        if type(other) is type(self):
            return (
                self.name == other.name and
                self.familyname == other.familyname and
                self.age == other.age and
                self.gender == other.gender and
                self.nationality == other.nationality and
                self.school == other.school and
                self.subjects == other.subjects
            )
        else:
            return False

    def __hash__(self):
        return hash(
            self.name,
            self.familyname,
            self.age,
            self.gender,
            self.nationality,
            self.school,
            tuple(self.subjects) if self.subjects else None
        )

    def set_school(self, school=None):
        self.school = school

    def add_subject(self, subjects=None):
        self.subjects = subjects

    @staticmethod
    def get_info():
        return 'This class created a Student'


class Teacher(Human):
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, subjects=None):
        super().__init__(
            name=name,
            familyname=familyname,
            age=age,
            gender=gender,
            nationality=nationality
        )
        self.school = school
        self.subjects = subjects

    def __eq__(self, other):
        if type(other) is type(self):
            return (
                self.name == other.name and
                self.familyname == other.familyname and
                self.age == other.age and
                self.gender == other.gender and
                self.nationality == other.nationality and
                self.school == other.school and
                self.subjects == other.subjects
            )
        else:
            return False

    def __hash__(self):
        return hash(
            self.name,
            self.familyname,
            self.age,
            self.gender,
            self.nationality,
            self.school,
            tuple(self.subjects) if self.subjects else None
        )

    def set_school(self, school=None):
        self.school = school

    def add_subject(self, subjects=None):
        self.subjects = subjects

    @staticmethod
    def get_info():
        return 'This class created a Teacher'


print('Module is imported')
