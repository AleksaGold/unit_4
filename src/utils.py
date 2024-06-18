from src.vacancy import Vacancy


def get_vacancy_objects(vacancies):
    """
    Функция создания объектов вакансий с учетом введенных пользователем параметров
    :param vacancies: список вакансий с учетом введенных пользователем параметров
    :return: список объектов
    """
    user_vacancies = []
    for vacancy in vacancies:
        vac = Vacancy(
            id=vacancy['id'],
            name=vacancy['name'],
            published_at=vacancy["published_at"],
            salary=vacancy["salary"],
            alternate_url=vacancy["alternate_url"],
        )
        user_vacancies.append(vac)
    return user_vacancies


def get_top_user_vacancies(all_vacancies, top_index):
    """
    Функция получения ТОП-вакансий по запросу пользователя
    :param all_vacancies:список всех вакансий по запросу пользователя
    :param top_index: количество вакансий запрошенных пользователем
    :return: список запрошенных пользователем вакансий
    """
    top_user_vacancies = []
    for vacancy in all_vacancies[:top_index]:
        top_user_vacancies.append(vacancy)
    return top_user_vacancies
