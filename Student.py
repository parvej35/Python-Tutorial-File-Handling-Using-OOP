class Student:

    total_student = 0

    id = 0
    first_name = ""
    last_name = ""
    age = ""
    country = ""

    def __init__(self, first_name, last_name, age, country):

        # print("1 total_student : " + str(self.total_student))
        Student.total_student += 1

        # print("2 total_student : " + str(self.total_student))

        Student.id = Student.total_student

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_country(self):
        return self.country

    def get_total(self):
        return self.total_student