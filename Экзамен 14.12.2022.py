# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

# def a(b):
#     return '*' * len(b[:-4])+ b[-4:]
# print(a(input('введите номер карты: ')))


# 2. Напишите функцию, которая проверяет: является ли слово палиндромом

# def pal(a):
#     return a[::-1] == a
# while True:
#     a = input("Введите слово: ")
#     print(f"{a} это палиндром!" if pal(a) else "это не палиндром")


# 3. Решите задачу

#
# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)

class Tomato:
    states = {0: "зеленый", 1: "малочный", 2: "розовый", 3: "спелый"}
    def __init__(self, index):
        self._index = index
        self._state = 0
    def grow(self):
        if self._state < 3:
           self._state += 1
           self._print_state()
    def _print_state(self):
        print(f'Tomato {self, _index} is {Tomato.states[self. _state]}')
    def is_ripe(self):
        if self._state == 3:
            return True
        return False


# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая

class TomatoBush:
    def __init__(self, num, index):
        self.tomatoes = [Tomato(index) for index in range(0, num)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
    def give_away_all(self):
        self.tomatoes = []


# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.


class Gardener:
    def __init__ (self, name, plant):
        self.name = name
        self._plant = plant
    def work(self):
        print('Садовник работает...')
        self._plant.grow_all()
        print('Садовник закончил')
    def harvest(self):
        print('Садовник собирает урожай...')
        if self._plant.all_are_ripe():
           self._plant.give_away_all()
           print('Сбор урожая завершен')
        else:
           print('растение зеленое и не созрело.')
    @staticmethod
    def knowledge_base():
        print('''Время сбора урожая томатов в идеале должно наступать, когда плоды
                является зрелым зеленым, а затем ему дают созреть на лозе.
                Это предотвращает расщепление или образование синяков,
                мера контроля над процессом созревания.''')
if __name__ == '__main__' :
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Mikl', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()






