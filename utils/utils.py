

def set_correct_salary_hh(salary_original) -> dict:
    """Приводит к единому виду зарплату с hh"""
    if salary_original is None:
        correct_salary = {"from": 0,
                          "to": 0,
                          "currency": "RUR",
                          "gross": False}
    elif salary_original['from'] is None:
        salary_original['from'] = 0
        correct_salary = salary_original
    elif salary_original['to'] is None:
        salary_original['to'] = 0
        correct_salary = salary_original
    else:
        correct_salary = salary_original
    return correct_salary

def set_correct_salary_from(salary_original):
    """Приводит к единому виду зарплату с hh"""
    if salary_original is None:
        correct_salary_from = None
    else:
        correct_salary_from = salary_original['from']
    return correct_salary_from

def set_correct_salary_to(salary_original):
    """Приводит к единому виду зарплату с hh"""
    if salary_original is None:
        correct_salary_to = None
    else:
        correct_salary_to = salary_original['to']
    return correct_salary_to

def set_correct_currency(salary_original):
    """Приводит к единому виду зарплату с hh"""
    if salary_original is None:
        correct_currency = None
    else:
        correct_currency = salary_original['currency']
    return correct_currency

