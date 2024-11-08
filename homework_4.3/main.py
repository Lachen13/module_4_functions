from utils import get_reg_data, reg_check

user_input = [
    'Введите имя пользователя: ',
    'Введите фамилию пользователя: ',
    'Введите телефон в формате +***(**)*******: ',
    'Введите email на яндексе: ',
]

users_list = []
patterns = get_reg_data()

while len(users_list) < 3:
    user_data_list = []

    for i in range(4):

        while True:
            user_questions = input(user_input[i])
            # Проверка данных пользователя с помощью функции reg_check
            if reg_check(user_questions, patterns[i], users_list):
                user_data_list.append(user_questions)
                break

    # Если уникальность подтверждена, добавляем пользователя в список
    users_list.append(user_data_list)

    print()
    if len(users_list) < 3:
        print('Введите данные следующего пользователя:')


for user_data in users_list:
    print(user_data)
