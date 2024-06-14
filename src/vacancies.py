class Vacancies:
    """"Класс для работы с вакансиями"""

    # id: str
    name: str
    published_at: str
    salary_from: int
    salary_to: int
    currency: str
    # has_test: bool
    # requirement: str
    alternate_url: str

    def __init__(self, name, published_at, salary_from, salary_to, currency, alternate_url):
        """Конструктор для инициализации объекта"""
        self.name = name
        self.published_at = published_at
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.alternate_url = alternate_url

        self.validate_salary_from()

    def validate_salary_from(self):
        """
        Метод валидации нижней границы заработной платы, если значение не указано,
        то выставляется значение заработной платы - 0
        :return: установленная заработная плата
        """
        if not self.salary_from:
            self.salary_from = 0
        return self.salary_from

    def __repr__(self):
        """
        Метод для отображения информации об объекте класса в режиме отладки
        :return: отображение информации об объекте класса
        """
        return f'{self.name}, {self.salary_from}, {self.currency}, {self.alternate_url}'

    def __gt__(self, other):
        """
        Метод сравнения вакансий по зарплате
        :param other: зарплаты указанные в вакансиях
        :return: True если зарплата рабочей вакансии больше, чем зарплата сравниваемой вакансии
        """
        return self.salary_from > other.salary_from

    def __lt__(self, other):
        """
        Метод сравнения вакансий по зарплате
        :param other: зарплаты указанные в вакансиях
        :return: True если зарплата рабочей вакансии меньше, чем зарплата сравниваемой вакансии
        """
        return self.salary_from < other.salary_from
