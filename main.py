from src.API import HeadHunterAPI
from src.file_saver import JsonSaver
from src.user import User
from src.utils import get_vacancy_objects, get_top_user_vacancies
from src.vacancy import Vacancy


def main():
    """
    Функция для запуска основного кода программы
    :return:
    """

    hh_object = HeadHunterAPI('https://api.hh.ru/vacancies')
    hh_object.connect_to_the_site()
    print(hh_object)

    print("\nПосле ответа на вопросы вам будет предложен список вакансий с учетом введенных вами параметров\n"
          "Регион поиска вакансий - Россия, если вам необходимы вакансии по другим регионам, обратитесь к "
          "администратору\n"
          "Для просмотра более подробной информации по вакансии, перейдите по ссылке\n")

    user_name = input("Введите ваше имя: ")
    filter_words = input("Введите ключевые слова для поиска вакансии: ")

    user = User(user_name, filter_words)

    salary_index = input("Если вы хотите просмотреть только вакансии с указанной заработной платой, введите - 1\n"
                         "Если хотите просмотреть все вакансии, введите любой символ: ")

    user.only_with_salary(salary_index)

    vacancies_received = hh_object.get_vacancies(text=user.filter_words,
                                                 only_with_salary=user.vacancies_with_salary,
                                                 area=user.area)

    vacancies_json = JsonSaver('vacancies.json')
    vacancies_json.add_vacancies(vacancies_received)
    vacancies_from_json = vacancies_json.get_vacancies()

    try:
        top_index = int(input("Введите количество вакансий для отображения по возрастанию заработной платы: "))
    except ValueError as e:
        print("\nВведенное значение должно быть целым числом, попробуйте повторить запрос")
    else:
        all_vacancies = get_vacancy_objects(vacancies_from_json)
        top_user_vacancies = get_top_user_vacancies(all_vacancies, top_index)
        sorted_user_vacancies = Vacancy.sort_vacancies_by_salary_from(top_user_vacancies)
        for vacancy in sorted_user_vacancies:
            print(f'{vacancy}\n')


if __name__ == '__main__':
    main()
