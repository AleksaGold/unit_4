class Vacancy:
    """"Класс для работы с вакансиями"""

    id: str
    name: str
    published_at: str
    salary: str
    salary_from: int
    salary_to: int
    currency: str
    salary_gross: str
    alternate_url: str

    def __init__(self, id, name, published_at, alternate_url, salary):
        """Конструктор для инициализации объекта"""
        self.id = id
        self.name = name
        self.published_at = published_at
        self.alternate_url = alternate_url
        self.salary = salary

        self.salary_from = None
        self.salary_to = None
        self.salary_currency = None
        self.salary_gross = None

        self.validate_salary()

    def validate_salary(self):
        """
        Метод валидации данных
        :return: 'Зарплата не указана' если в вакансии не указана зарплата,
        распаковывает данные по зарплате если зарплата указана
        """
        if self.salary is None:
            self.salary = 'Зарплата не указана'
        else:
            salary = self.salary
            self.salary_from = salary['from']
            self.salary_to = salary['to']
            self.salary_currency = salary['currency']
            self.salary_gross = salary['gross']

    def __repr__(self):
        """
        Метод для отображения информации об объекте класса в режиме отладки
        :return: отображение информации об объекте класса
        """
        return f'{self.id}, {self.published_at}, {self.name}, {self.salary}, {self.salary_from}, {self.salary_to}, {self.salary_currency}, {self.salary_gross}'

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



# написать статик метод для сортировки вакансий
