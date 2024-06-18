class User:
    """Класс для работы с пользователем"""
    user_name: str
    filter_words: str
    vacancies_with_salary: bool
    __area: int

    def __init__(self, user_name, filter_words):
        """Конструктор для инициализации объекта"""
        self.user_name = user_name
        self.filter_words = filter_words
        self.vacancies_with_salary = True
        self.__area = 1

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        if isinstance(value, int):
            self.__area = value
        else:
            raise ValueError("Код региона должен быть int")

    def __repr__(self):
        """
        Метод для отображения информации об объекте класса в режиме отладки
        :return: отображение информации об объекте класса
        """
        return f'{self.user_name}, {self.filter_words}, {self.vacancies_with_salary}'

    def only_with_salary(self, index):
        """
        Метод для установления флага "vacancies_with_salary"
        :param index: ввод пользователя
        :return: True если ввод пользователя == '1', False для любого другого ввода
        """
        if index == '1':
            self.vacancies_with_salary = True
        else:
            self.vacancies_with_salary = False
