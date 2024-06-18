class Vacancy:
    """"Класс для работы с вакансиями"""

    id: str
    name: str
    published_at: str
    salary: str
    salary_from: int
    salary_to: int
    currency: None
    salary_gross: None
    alternate_url: str

    def __init__(self, id, name, published_at, alternate_url, salary):
        """Конструктор для инициализации объекта"""
        self.id = id
        self.name = name
        self.published_at = published_at
        self.alternate_url = alternate_url
        self.salary = salary

        self.salary_from = 0
        self.salary_to = 0
        self.salary_currency = None
        self.salary_gross = None

        self.validate_salary()
        self.check_salary_from()

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

    def check_salary_from(self):
        """
        Метод для проверки распакованного значения атрибута "salary_from"
        :return: если значение атрибута - "None", то выставляется 0,
        если значение не "None", то остается распакованное значение
        """
        if self.salary_from is None:
            self.salary_from = 0

    def __str__(self):
        """
        Метод для вывода информации пользователю
        :return: строковое представление информации для пользователя
        """
        if self.salary == 'Зарплата не указана':
            return (f'\nНазвание вакансии: {self.name}\n'
                    f'{self.salary}\n'
                    f'Ссылка на вакансию: {self.alternate_url}')
        if self.salary_from == 0:
            return (f'\nНазвание вакансии: {self.name}\n'
                    f'Зарплата до {self.salary_to} {self.salary_currency}\n'
                    f'Ссылка на вакансию: {self.alternate_url}')
        else:
            return (f'\nНазвание вакансии: {self.name}\n'
                    f'Зарплата от {self.salary_from} {self.salary_currency}\n'
                    f'Ссылка на вакансию: {self.alternate_url}')

    def __repr__(self):
        """
        Метод для отображения информации об объекте класса в режиме отладки
        :return: отображение информации об объекте класса
        """
        return (f'{self.id}, {self.published_at}, {self.name}, {self.salary}, '
                f'{self.salary_from}, {self.salary_to}, {self.salary_currency}, {self.salary_gross}')

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

    @staticmethod
    def sort_vacancies_by_salary_from(user_vacancies):
        return sorted(user_vacancies)
