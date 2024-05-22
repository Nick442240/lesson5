class MyClass:
    def __init__(self, value):
        self.value = value  # Атрибут экземпляра класса

    def show_value(self):
        print(self.value)  # Доступ к атрибуту экземпляра через self

obj1 = MyClass(10)
obj2 = MyClass(20)

obj2.show_value()
obj1.show_value()