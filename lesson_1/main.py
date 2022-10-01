class Car: # Чертеж
                   # входящие параметры
    def __init__(self, model, year, color): # Конструктор
        self.model = model #self.model -  атрибуты обьектов (поля)
        self.year = year
        self.color = color
        
        
    def drive(self, sity):
        print(f"Машина {self.model} едет в {sity} ")
    
    def change_color(self, new_color):
        self.color = new_color


volvo = Car("Volvo s90", 1990, "Green") # объект
tesla = Car("Tesla Model X", 2022, "white")

print(f"Model: {volvo.model} Year: {volvo.year} Color: {volvo.color}")


volvo.color = "Black"
tesla.change_color("Red")
# print(volvo)
print(f"Model: {volvo.model} Year: {volvo.year} Color: {volvo.color}")
print(f"Model: {tesla.model} Year: {tesla.year} Color: {tesla.color}")

volvo.drive("Бишкек")
tesla.drive("Ош")


