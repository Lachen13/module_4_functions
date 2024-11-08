import re


def get_reg_data():
    return [r'^[a-zA-Zа-яА-ЯёЁ]+$', r'[a-zA-Zа-яА-ЯёЁ]+$', r'\+\d{1,3}\(\d{2}\)\d{7}$', r'[a-zA-Z0-9]\w*@yandex\.ru$']

def check_unique_data(user_data, data_to_check):
    return user_data in data_to_check

def reg_check(user_data, reg_pattern, users_list, data_to_check=None):
    if not re.match(reg_pattern, user_data):
        print(f'\nОшибка! Данные "{user_data}" не соответствуют паттерну.')
        return None

    if users_list:
        data_to_check = [user_data[2] for user_data in users_list] + [user_data[3] for user_data in users_list]
        if check_unique_data(user_data, data_to_check):
            print(f'\nОшибка! {user_data} уже существует.')
            return None

    return user_data



