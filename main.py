from Classes.Engine import HeadHunter
from Classes.DB_Saver import DB_Saver
from Classes.DB_Manager import DB_Manager
import sys

emp_id = ['2492', '5974128', '586', '590', '599', '533', '490', '399', '330', '272', '229', '211', '139', '89',
              '80', '65', '59']
def get_employers_info():
    company_list = []
    for i in emp_id:
        test_company = HeadHunter().get_company_info(i)
        company_list.append(test_company)

    company_tuple = [tuple(d.values()) for d in company_list]
    return company_tuple

def get_vacancies_info():
    vacancies_list = []
    test_company = HeadHunter().get_requests(emp_id)
    for i in test_company['items']:
        vacancies_list.append(i)

    vacancies_tuple = [tuple(d.values()) for d in vacancies_list]
    return vacancies_tuple

print('Привет!')
is_update_employers_data = input('Хотите обновить данные в бд?\n1 - Да\n2 - Нет\n')
if is_update_employers_data == '1':
    DB_Saver().delete_all()
    DB_Saver().write_employers(get_employers_info())
    DB_Saver().write_vacancies(get_vacancies_info())

def main_coise():
    print('')
    main_menu_coise = input('Выберите, какую информацию хотите получить:\n1 - Cписок всех компаний и количество вакансий у каждой компании.\n'
                        '2 - Список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.\n'
                        '3 - Среднюю зарплату по вакансиям.\n'
                        '4 - Список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n'
                        '5 - Список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.\n'
                        '0 - Выход\n')
    return main_menu_coise

main_menu_coise = main_coise()
if main_menu_coise == '1':
    info = DB_Manager().get_companies_and_vacancies_count()
    for i in info:
        print(i)
    main_coise()
elif main_menu_coise == '2':
    info = DB_Manager().get_all_vacancies()
    for i in info:
        print(i)
    main_coise()
elif main_menu_coise == '3':
    info = DB_Manager().get_avg_salary()
    print(f'Средняя зарплата от: {info[0]},\nСредняя зарплата до: {info[1]}')
    main_coise()
elif main_menu_coise == '4':
    info = DB_Manager().get_vacancies_with_higher_salary()
    for i in info:
        print(i)
    main_coise()
elif main_menu_coise == '5':
    vacansy_keyword = input('Введите название вакансии, которую хотите найти: ')
    info = DB_Manager().get_vacancies_with_keyword(vacansy_keyword)
    for i in info:
        print(i)
    main_coise()
elif main_menu_coise == '0':
    sys.exit()

