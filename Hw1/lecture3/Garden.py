from abc import  ABC, abstractmethod

VEGETABLES = []
FRUITS = []

class GardenMetaClass(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return  cls._instances[cls]
class Garden(metaclass=GardenMetaClass):
    def __init__(self, vegetables, fruits):
        self.vegetables = vegetables
        self.fruits = fruits

class Vegetables(ABC):
    def __init__(self, vegetable_type):
        self.plant_type = vegetable_type

        states = {0: 'None', 1: 'flowering', 2: 'green', 3: 'red'}
     @property
    def plant_type(self):
        return  self.plant_type

    def plant_type(self, plant_type):
        if plant_type.lower() in VEGETABLES:
            self._plant_type = plant_type
        else:
            raise Exception(f"There is no such vegetable in the list. Your vegetable:{plant_type}")

    @abstractmethod
    def grow(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('You missed me.')


class Fruits(ABC):
    def __init__(self, fruit_type):
        self.plant_type = fruit_type

    states = {0: 'None', 1: 'flowering', 2:'almost_ripe', 3:'ripe'}

    @abstractmethod
    def grow(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('You missed me.')

class Tomato(Vegetables):
    def __init__(self, index, vegetable_type):
        super(Tomato,self).__init__(vegetable_type)
        self.index = index
        self.state = 0
        self.vegetable_type = vegetable_type
    def grow(self):


    def is_ripe(self):
        if self.state == 3 :
            return True
        return False


    def _change_state(self):
        if self.state < 3 :
            self.state += 1

    def print_state(self):
        print(f"{self.vegetable_type} {self.index} is {Tomato.states[self.state]}")

class Aplles(Fruits):
    def __init__(self, index, fruit_type):
        super(Aplles, self).__init__(fruit_type)

    def grow(self):
        pass
    def is_ripe(self):
        pass


class TomatoBush():
    def __init__(self, num):
        self.tomatos = [Tomato(index, 'Red_tomato') for index in range(0, num -1)]

    def gorw_all(self):
        for tomato in self.tomatos:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe] for tomato in self.tomatos)

    def give_away_all(self):
        self.tomatos = []



class AplleTree():
    pass

class Gardener():
    pass