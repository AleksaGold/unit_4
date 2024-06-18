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
    __url: str

    def __init__(self, url):
        self.__url = url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_url):
        self.__url = new_url

    def connect_to_the_site(self):
        """Метод для подключения к сайту hh.ru"""
        return requests.get(self.__url).status_code == 200

    def __str__(self):
        if self.connect_to_the_site() is True:
            return f'Подключение выполнено успешно'
        raise KeyError('Введен неверный url адрес для отправки запроса')

    def get_vacancies(self, **kwargs):
        """Метод для получения вакансий с сайта hh.ru"""
        params = {**kwargs}
        response = requests.get(self.__url, params).json()
        vacancies = response['items']
        return vacancies
