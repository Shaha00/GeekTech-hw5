class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        pass

    def __str__(self):
        return (f"Cpu: {self.cpu}, memory: {self.memory}")

    def __gt__(self, other):
        return self.memory > other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __eq__(self, other):
        return self.memory == other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    @staticmethod
    def call(sim_card_number, call_to_number):
        print(f"Идёт звонок на номер {call_to_number} с сим-карты {sim_card_number}")

    def __str__(self):
        return (f"Sim cards list: {self.sim_cards_list}")


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    @staticmethod
    def use_gps(location):
        print(f"Построен маршрут до пункта {location}")

    def __str__(self):
        return (f"Cpu: {self.cpu}, memory: {self.memory}, sim list: {self.sim_cards_list}")


hp = Computer(cpu="intel i5", memory=512)

phone = Phone(sim_cards_list=["Beeline", "MegaCom", "O!"])

iphone = SmartPhone(cpu="A16 Bionic", memory=512, sim_cards_list=["Beeline", "MegaCom", "O!"])
xiaomi = SmartPhone(cpu="Snapdragon Gen1+", memory=1024, sim_cards_list=["Beeline", "MegaCom", "O!"])


print(hp)
print(phone)
print(iphone)
print(xiaomi)

phone.call(call_to_number="+996-774-040-090",sim_card_number="2-Beeline")

iphone.use_gps(location="Kyzyl-Kia")

print(hp > iphone)
print(iphone > xiaomi)
print(xiaomi != hp)
print(hp <= xiaomi)