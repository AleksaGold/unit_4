import json
from abc import ABC, abstractmethod


class FileSaver(ABC):
    """Абстрактный класс, для работы с файлом"""

    @abstractmethod
    def add_vacancies(self, vacancies):
        """Метод добавления вакансий в файл"""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Метод получения вакансий из файла"""
        pass

    @abstractmethod
    def del_vacancies(self, index):
        """Метод удаления вакансий из файла"""
        pass


class JsonSaver(FileSaver):

    def __init__(self, file_name):
        """Конструктор для инициализации объекта"""
        self.file_name = file_name

    def add_vacancies(self, vacancies):
        """
        Метод добавления полученных с сайта вакансий в json файл
        :param vacancies: вакансии полученные с помощью API сервиса
        :return: json файл с вакансиями
        """
        with open(self.file_name, 'w') as file:
            return json.dump(vacancies, file, indent=3, ensure_ascii=False)

    def get_vacancies(self):
        """
        Метод получения вакансий из json файла
        :return: список вакансий
        """
        with open(self.file_name, 'r') as file:
            return json.load(file)

    def del_vacancies(self, index):
        pass
#        """
#        Метод удаления вакансий из json файла
#        :param index: индекс удаляемой строки
#        :return: обновленный список
#        """
#        vacancies = self.get_vacancies()
#        del vacancies[index]
#        return vacancies
