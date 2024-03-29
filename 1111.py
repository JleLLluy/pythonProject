class Profile:
    def __init__(self, profession_name):
        self.profession_name = profession_name

    def info(self):
        return ''

    def describe(self):
        print(self.profession_name, self.info())


class Vacancy(Profile):
    def __init__(self, profession_name, salary):
        super().__init__(profession_name)
        self.salary = salary

    def info(self):
        return f'Предлагаемая зарплата: {self.salary}'


class Resume(Profile):
    def __init__(self, profession_name, work_experience):
        super().__init__(profession_name)
        self.work_experience = work_experience

    def info(self):
        return f"Стаж работы: {self.work_experience}"
