from abc import ABC, abstractmethod


class API(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def connect_to_the_site(self):
        """Абстрактный метод для подключения к сайту"""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Абстрактный метод для получения вакансий"""
        pass


class HeadHunterAPI(API):
    """
    Класс для работы с платформой hh.ru
    """

    def connect_to_the_site(self):
        """Метод для подключения к сайту hh.ru"""
        pass

    def get_vacancies(self):
        """Метод для получения вакансий с сайта hh.ru"""
        pass
