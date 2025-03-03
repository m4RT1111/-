import abc
from typing import Any

class AbstractClass1(abc.ABC):
    def __init__(self, attribute1: float, attribute2: str):
        """
        Инициализация объекта AbstractClass1.

        :param attribute1: Числовое значение, описывающее объект.
        :param attribute2: Строковое значение, описывающее объект.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    @abc.abstractmethod
    def method1(self) -> Any:
        """
        Метод, описывающий действие 1.

        >>> obj = AbstractClass1(1.0, "test")
        >>> obj.method1()
        'Result of method1'
        """
        ...

    @abc.abstractmethod
    def method2(self, param1: int) -> Any:
        """
        Метод, описывающий действие 2.

        :param param1: Целочисленный параметр для метода.

        >>> obj = AbstractClass1(1.0, "test")
        >>> obj.method2(5)
        'Result of method2 with param1=5'
        """
        ...

class AbstractClass2(abc.ABC):
    def __init__(self, attribute1: int, attribute2: bool):
        """
        Инициализация объекта AbstractClass2.

        :param attribute1: Целочисленное значение, описывающее объект.
        :param attribute2: Логическое значение, описывающее объект.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    @abc.abstractmethod
    def method1(self) -> Any:
        """
        Метод, описывающий действие 1.

        >>> obj = AbstractClass2(10, True)
        >>> obj.method1()
        'Result of method1'
        """
        ...

    @abc.abstractmethod
    def method2(self, param1: float) -> Any:
        """
        Метод, описывающий действие 2.

        :param param1: Параметр с плавающей точкой для метода.

        >>> obj = AbstractClass2(10, True)
        >>> obj.method2(3.14)
        'Result of method2 with param1=3.14'
        """
        ...

class AbstractClass3(abc.ABC):
    def __init__(self, attribute1: str, attribute2: list):
        """
        Инициализация объекта AbstractClass3.

        :param attribute1: Строковое значение, описывающее объект.
        :param attribute2: Список, описывающий объект.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    @abc.abstractmethod
    def method1(self) -> Any:
        """
        Метод, описывающий действие 1.

        >>> obj = AbstractClass3("example", [1, 2, 3])
        >>> obj.method1()
        'Result of method1'
        """
        ...

    @abc.abstractmethod
    def method2(self, param1: dict) -> Any:
        """
        Метод, описывающий действие 2.

        :param param1: Параметр-словарь для метода.

        >>> obj = AbstractClass3("example", [1, 2, 3])
        >>> obj.method2({'key': 'value'})
        'Result of method2 with param1={'key': 'value'}'
        """
        ...

# Пример использования
class ConcreteClass1(AbstractClass1):
    def method1(self) -> str:
        return 'Result of method1'

    def method2(self, param1: int) -> str:
        return f'Result of method2 with param1={param1}'

class ConcreteClass2(AbstractClass2):
    def method1(self) -> str:
        return 'Result of method1'

    def method2(self, param1: float) -> str:
        return f'Result of method2 with param1={param1}'

class ConcreteClass3(AbstractClass3):
    def method1(self) -> str:
        return 'Result of method1'

    def method2(self, param1: dict) -> str:
        return f'Result of method2 with param1={param1}'

# Тестирование
if __name__ == "__main__":
    obj1 = ConcreteClass1(1.0, "test")
    print(obj1.method1())
    print(obj1.method2(5))

    obj2 = ConcreteClass2(10, True)
    print(obj2.method1())
    print(obj2.method2(3.14))

    obj3 = ConcreteClass3("example", [1, 2, 3])
    print(obj3.method1())
    print(obj3.method2({'key': 'value'}))