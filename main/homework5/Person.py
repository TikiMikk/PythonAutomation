from datetime import datetime


class Person:

    def __init__(self, full_name, birth_year):
        if len(full_name.split(' ')) == 2:
            self.full_name = full_name
        else:
            raise TypeError('Invalid full name')
        if datetime.now().year >= birth_year >= 1900:
            self.birth_year = birth_year
        else:
            raise ValueError('Invalid birth date')

    def __str__(self):
        return f"Full name: {self.full_name} \n" \
               f"Birth year: {self.birth_year}"

    def get_name_from_full_name(self):
        return self.__split_full_name()[0]

    def get_surname_from_full_name(self):
        return self.__split_full_name()[1]

    def age_in(self, year=None):
        if year is None:
            return datetime.now().year - self.birth_year
        else:
            return year - self.birth_year

    def __split_full_name(self):
        return self.full_name.split(' ')


if __name__ == '__main__':
    name = 'Bob Marley'
    arr = name.split(' ')

    u = Person(name, 2021)
    print(u.age_in())
    print(u.full_name)
    print(u.get_name_from_full_name())
    print(u.get_surname_from_full_name())
    print(u)
