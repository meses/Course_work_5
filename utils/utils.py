import requests
import json
import time


def set_correct_salary_from(salary_original):
    """Приводит к единому виду зарплату от с hh"""
    if salary_original is None:
        correct_salary_from = None
    elif salary_original['from'] is None:
        correct_salary_from = None
    else:
        correct_salary_from = str(salary_original['from'])
    return correct_salary_from

def set_correct_salary_to(salary_original):
    """Приводит к единому виду зарплату до с hh"""
    if salary_original is None:
        correct_salary_to = None
    elif salary_original['to'] is None:
        correct_salary_to = None
    else:
        correct_salary_to = str(salary_original['to'])
    return correct_salary_to

def set_correct_currency(salary_original):
    """Приводит к единому виду валюту зарплаты с hh"""
    if salary_original is None:
        correct_currency = None
    else:
        correct_currency = str(salary_original['currency'])
    return correct_currency

def getEmployers():
    """Функция для получения id компаний с hh"""
    req = requests.get('https://api.hh.ru/employers')
    data = req.content.decode()
    req.close()
    count_of_employers = json.loads(data)['found']
    employers = []
    i = 0
    j = count_of_employers
    while i < j:
        req = requests.get('https://api.hh.ru/employers/' + str(i + 1))
        data = req.content.decode()
        req.close()
        jsObj = json.loads(data)
        try:
            employers.append([jsObj['id'], jsObj['name']])
            i += 1
            print([jsObj['id'], jsObj['name']])
        except:
            i += 1
            j += 1
        if i % 200 == 0:
            time.sleep(0.2)
    return employers

