from main.homework5.Employee import Employee


class ITEmployee(Employee):

    def __init__(self, full_name, birth_year, position, work_experience, salary):
        super().__init__(full_name, birth_year, position, work_experience, salary)

    def __str__(self):
        return f"{super().__str__()}"

    def add_skill(self):
        pass

    def add_skills(self):
        pass

