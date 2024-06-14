from abc import ABC, abstractmethod

import requests


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
    url: str

    def __init__(self, url):
        self.url = url

    def connect_to_the_site(self):
        """Метод для подключения к сайту hh.ru"""
        if requests.get(self.url).status_code == 200:
            return f'Подключение выполнено успешно, введите параметры запроса'  # склеить с запросом пользователя
        return f'Введен неверный url адрес для отправки запроса'

    def get_vacancies(self, **kwargs):
        """Метод для получения вакансий с сайта hh.ru"""
        param = {**kwargs}
        response = requests.get(self.url, param)
        vacancies = response.json()['items']
        return vacancies
