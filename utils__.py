import json
import operator
from zipfile import ZipFile


def opener_zip(filename):
    """
    Эта функция выгружает данные из zip
    :param filename: 'operations.zip'
    :return: список с банковскими операциями
    """
    with ZipFile("operations.zip", mode="r") as operation_json:
        with operation_json.open("operations.json", mode="r") as operation_txt:
            operations_list = (json.loads(operation_txt.read()))
    return operations_list


def filter_of_executed():
    """
    Эта функция сортирует данные по ключу EXECUTED
    :return: список с выполненными банковскими операциями
    """
    executed_list = []
    operations = opener_zip('operations.zip')
    for i in operations:
        if (id_key := i.get('state')) and id_key == 'EXECUTED':
            executed_list.append(i)
    return executed_list


def sort_executed():
    """
    Эта функция сортирует данные по дате, ставя последние операции в начало списка
    :return: отфильтрованный список
    """
    executed_list = filter_of_executed()
    sort_list = sorted(executed_list, key=operator.itemgetter('date'), reverse=True)
    return sort_list


def output_5_end_operations():
    """
    Эта функция выводит 5 последних операций совершенных клиентом
    :return: список из 5 последних операций
    """
    ends_operations = sort_executed()
    ends_operations_list = []
    count = 5
    for i in ends_operations:
        if count != 0:
            count -= 1
            ends_operations_list.append(i)
    return ends_operations_list


def get_date():
    """
    Эта функция переделывает отображение даты совершения операции в нужном виде
    :return: список с новым значением ключа date
    """
    necessary_options = output_5_end_operations()
    for i in necessary_options:
        i['date'] = ".".join(i['date'].split('T')[0].split('-')[::-1])
    return necessary_options


def get_requisites_view():
    """
    Эта функция меняет отображение счета и карты в нужном виде
    :return: список с новым значением ключа from
    """
    operations_list = get_date()
    for i in operations_list:
        if i.get('from') is None:
            i['from'] = ''
        elif i.get('from', '')[:4] == 'Счет':
            i['from'] = i['from'][:4] + ' ' + '*' * 2 + i['from'][-4:]
        else:
            number_card = i['from'].split(' ')
            number_card_ = number_card[-1]
            number_card_ = number_card_[0:3] + ' ' + number_card_[4:6] + '*' * 2 + ' ' + '*' * 4 + ' ' + number_card_[
                                                                                                         12:]
            if len(number_card) == 2:
                i['from'] = number_card[0] + ' ' + number_card_
            else:
                i['from'] = number_card[0] + ' ' + number_card[1] + ' ' + number_card_

    return operations_list


def get_requisites_view_to():
    """
    Эта функция меняет отображение номера счета и карты в нужном виде
    :return: список с новыми значениями ключа to
    """
    operations_list = get_requisites_view()
    for i in operations_list:
        if i.get('to') is None:
            i['to'] = ''
        elif i.get('to', '')[:4] == 'Счет':
            i['to'] = i['to'][:4] + ' ' + '*' * 2 + i['to'][-4:]
        else:
            number_card = i['to'].split(' ')
            number_card_ = number_card[-1]
            number_card_ = number_card_[0:3] + ' ' + number_card_[4:6] + '*' * 2 + ' ' + '*' * 4 + ' ' + number_card_[
                                                                                                         12:]
            if len(number_card) == 2:
                i['to'] = number_card[0] + ' ' + number_card_
            else:
                i['to'] = number_card[0] + ' ' + number_card[1] + ' ' + number_card_

    return operations_list


def show_to_user():
    """
    Эта функция выводит пользователю информацию в нужном виде согласно заданию
    :return: значения нужных параметров в последовательности по заданию
    """
    operations_list_end = get_requisites_view_to()
    for i in operations_list_end:
        date_finish = i['date']
        description_finish = i['description']
        from_finish = i['from']
        to_finish = i['to']
        sum_finish = i['operationAmount']['amount']
        code_finish = i['operationAmount']['currency']['name']
        print(f'{date_finish} {description_finish}')
        print(f'{from_finish} -> {to_finish}')
        print(f'{sum_finish} {code_finish}')
        print("")

