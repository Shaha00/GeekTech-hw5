

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
        return self.__cpu + self.__memory
        

    def __str__(self):
        return f'Параметры: cpu = {self.__cpu}, memory = {self.__memory}'

    def gt(self, other):  # >
        return self.memory > other

    def lt(self, other):  # <
        return self.memory < other
    
    def eq(self, other):  # ==
        return self.memory == other

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
        sim_card_number = "Beeline"
        print(f"Идет звонок на номер {call_to_number} с сим-карты -1-{sim_card_number}.")
        
class SmartPhone(Computer, Phone):
        def __init__(self, cpu, memory):
            super().__init__(cpu, memory) 
            
        def use_gps(location):
            

        


с = Phone(1)

print(с.call(2,996774040990))


a = Computer(2,8)
print(a)
print(a.make_computations())









