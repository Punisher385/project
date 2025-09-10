class Denys:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_course(self):

        if self.birth_year is None:
            return None
        current_year = 2025
        age = current_year - self.birth_year
        course = max(1, age - 14)
        return course

    def full_name_list(self):
        return [self.first_name, self.last_name]

student = Denys("Денис", "Васюхник", 2008)
print("Курс:", student.calculate_course())
print("Список імені та прізвища:", student.full_name_list())
