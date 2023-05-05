"""Работа с API"""
from abc import ABC, abstractmethod
from utils.utils import set_correct_salary_from, set_correct_salary_to, set_correct_currency
import requests
import os
import json


class ABCEngine(ABC):

    @abstractmethod
    def __init__(self, url=''):
        pass

    @abstractmethod
    def get_requests(self, vacancy_name):
        pass

    @staticmethod
    @abstractmethod
    def data_formatting(item):
        pass


class HeadHunter(ABCEngine):

    def __init__(self, url=f'https://api.hh.ru/vacancies'):
        self.__url = url

    @property
    def url(self):
        return self.__url


    @staticmethod
    def data_formatting(item):
        """Форматирование данных, полученных по запросу к HeadHunter"""
        item_dict = {}
        item_dict['id'] = item['id']
        item_dict['name'] = item['name']
        item_dict['salary_from'] = set_correct_salary_from(item['salary'])
        item_dict['salary_to'] = set_correct_salary_to(item['salary'])
        item_dict['emlployer_id'] = item['employer']['id']
        item_dict['url'] = item['alternate_url']
        item_dict['currency'] = set_correct_currency(item['salary'])
        item_dict['requirement'] = item['snippet']['requirement']
        item_dict['responsibility'] = item['snippet']['responsibility']
        return item_dict

    def get_requests(self, employers_id):
        """Функция для получения вакансий с HH с заданным поисковым запосом"""
        #self.employers_id = employers_id
        data = {'items':[]}
        for i in range(1, 21):
            response = requests.get(self.url, params = {'User-Agent': 'Mozilla/5.0',
                                                        'area': 113,
                                                        'per_page': 100,
                                                        'employer_id': tuple(employers_id),
                                                        'page': str(i)
                                                        })
            if response.status_code == 200:
                for item in response.json()['items']:
                    data['items'].append(self.data_formatting(item))
        return data

    def get_company_info(self, employers_id):
        response = requests.get(f'https://api.hh.ru/employers/{employers_id}')
        data = {}
        if response.status_code == 200:
            item = response.content.decode()
            response.close()
            jsObj = json.loads(item)
            data['id'] = jsObj['id']
            data['name'] = jsObj['name']
            data['url'] = jsObj['alternate_url']
            data['description'] = jsObj['description']
            return data

