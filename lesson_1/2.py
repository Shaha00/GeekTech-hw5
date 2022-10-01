class Person():
    def __init__(self,fullname,age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(f'I am {self.fullname}, my age: {self.age}, my status: {self.is_married}')
class Student(Person):
    marks ={
        "eng":4,
        'rus':5,
        "math": 5,
    }
    def math_mid(self):
        res = 0
        count = 0
        for v in self.marks.values():
            res += v
            count +=1
        return res / count

class Teacher(Person):
    def __init__(self, fullname, age, is_married,salary,experience):
        super().__init__(fullname, age, is_married)
        self.salary = salary
        self.experience = experience
    def full_salary(self):
        if self.experience > 3:
            self.salary += self.salary* 0.05
        print(self.salary)
        
def create_students():
    res = []
    for i in range(3):
        a = Student("Ysman Nazarbaev", 12, True)
        res.append(a)
    return res
for i in create_students():
    i.introduce_myself()
    print(i.math_mid())
        

shahzod = Person("Ahmadov Shahzod",15,False)

a = Teacher("Bayjigitov Erbol", 15, True, 2000, 5)

shahzod.introduce_myself()

a.full_salary()
a.introduce_myself()
