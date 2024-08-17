def send_email(msg: str, recipient: str, *, sender="university.help@gmail.com"):
    is_domain_r = False
    is_domain_s = False
    for domain in ['.ru', '.com', '.net']:
        if domain in recipient:
            is_domain_r = True
    for domain in ['.ru', '.com', '.net']:
        if domain in sender:
            is_domain_s = True
        else:
            continue

    # if (is_domain_r == False) or (is_domain_s == False):
    if not is_domain_r or not is_domain_s:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    elif ("@" not in recipient) or ("@" not in sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    elif sender == recipient:
        print('Невозможно отправить письмо самому себе')
        return
    elif sender == "university.help@gmail.com":
        print(f'Письмо будет успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    print(msg)


send_email('it was 1st test, valid data:', 'vasya@iuh.ru')
send_email('it was 2nd test, valid data:', 'vasya@iuh.ru', sender='valid@diff.com')
send_email('it was 3rd test, inv recipient, valid sender:', 'durovwall.ru', sender='vkgroup@vk.net')
send_email('it was 4th test, valid recipient, inv sender:', 'good@sleep.com', sender='allweneed@love.is')
send_email('it was 5th test, inv recipient, inv sender:', 'cycles@without.', sender='hesitation.net')
send_email('it was 6th test, inv recipient, inv sender:', 'goodsleep.com', sender='allweneedlove.ru')

# noinspection SpellCheckingInspection
"""
Цель: закрепить знания о параметрах по умолчанию и именованных аргументах.

Задача "Рассылка писем":
Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же пользователя(администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.
Попробуем реализовать функцию с подробной логикой.

Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
Внутри функции реализовать следующую логику:
Проверка на корректность e-mail отправителя и получателя.
Проверка на отправку самому себе.
Проверка на отправителя по умолчанию.
Пункты задачи:
Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.
"""