# 3 tüüpi muutujaid/funktsioone klassis: visibility:
# 1. public, nt variable
# 2. protected, nt _variable
# 3. private, nt __variable
class MyClass:
    variable = 'Muutuja'
    _state = 'IDLE'
    __token = ''

    def __init__(self):
        self.old_variable = self.variable
        self.variable = 'Uuendatud'

    def set_variable(self, value):
        self.variable = value

    # lisada meetod, mis tagastab funktsiooni saadetud parameetri väärtuse koos klassi muutuja väärtusega
    # 'Tere' => '{Tere} Uuendatud'
    def return_some_text_with_class(self, text):
        return f"{text}, {self.variable}"

    def set_state(self, state):
        print(f"{self._state} -> {state}")
        self._state = state


class Child(MyClass):
    __internal_time = None

    def set_state(self, new_state):
        super().set_state(new_state)
        # self._state = new_state

    def __init__(self):
        self.__set_internal_time(123)

    def __set_internal_time(self, time = None):
        self.__internal_time = time

    def get_internal_time(self):
        return self.__internal_time

my_class = MyClass()
# print(my_class.__token) # viskab vea kuna proovime private muutjat pärida
# my_class.set_state('IN_PROGRESS')
# print(my_class._state)

child = Child()
child.set_state('IN_PROGRESS')
print(child._state)

# child.__set_internal_time(123454)
print(child.get_internal_time())






# print(type(my_class))
# print(my_class.old_variable)
# print(my_class.variable)

# # my_class.variable = 'test'
# my_class.set_variable('test1')
# # kutsume siin välja, siis tagastab 'Tere test1'
# print(my_class.return_some_text_with_class('Tere')) # prindib 'Tere, test1'
# print(my_class.return_some_text_with_class('Head aega')) # prindib 'Head aega, test1'
# print(my_class.variable)



if __name__ == '__main__':
    MyClass()
    # print(__name__)