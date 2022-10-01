
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
        
    def show(self):
        print(f"Fullname: {shahzod.fullname}\nAge: {shahzod.age} \nIs_married!: {shahzod.is_married}")
    
class Student(Person):
    marks = {
        "Алгебра": 5,
        "Русский язык": 5,
        "Кыргызский язык": 5,
        "Информатика": 5,
        "История": 5,
        "Биология": 5,
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
        a = Student("Bekbashec Adilet", 12, True)
        res.append(a)
    return res
for i in create_students():
    i.show()
    print(i.math_mid())
          
shahzod = Person("Ahmadov Shahzod",15, "No married")

a = Student("Ahmadov Shahzod",15, "No married")
# print(f"Fullname: {shahzod.fullname}\nAge: {shahzod.age} \nIs_married!: {shahzod.is_married}")
shahzod.show()

print(f"Средний балл:\n{a.math_mid()}" )

a = Teacher("Ahmadov Shahzod", 12, True, 2000, 5)

a.full_salary()


