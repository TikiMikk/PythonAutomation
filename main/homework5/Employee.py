from main.homework5.Person import Person


class Employee(Person):

    def __init__(self, full_name, birth_year, position, work_experience, salary):
        super().__init__(full_name, birth_year)
        self.position = position
        if work_experience >= 0:
            self.work_experience = work_experience
        else:
            raise ValueError('Invalid work experience')
        if salary >= 0:
            self.salary = salary
        else:
            raise ValueError('Invalid salary')

    def __str__(self):
        return f"{super().__str__()} \n" \
               f"Position: {self.position} \n" \
               f"Work experience: {self.work_experience} \n" \
               f"Salary: {self.salary}"

    def find_out_position_level(self):
        if self.work_experience < 3:
            level = 'Junior '
        elif 3 <= self.work_experience <= 6:
            level = 'Middle '
        elif self.work_experience > 6:
            level = 'Senior '
        else:
            level = ''
        return f"{level}" \
               f"{self.position}"

    def add_salary(self, amount):
        self.salary += amount


if __name__ == '__main__':
    u = Employee('Snoop Dog', 1971, 'Smoker', 35, 10000)
    print(u)
    print(u.find_out_position_level())
    u.add_salary(20000)
    print(u)
