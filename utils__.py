import json
import operator
from zipfile import ZipFile


def opener_zip(filename):
    with ZipFile("operations.zip", mode="r") as operation_json:
        with operation_json.open("operations.json", mode="r") as operation_txt:
            operations_list = (json.loads(operation_txt.read()))
    return operations_list


opener_zip('operations.zip')


def filter_of_executed(operations):
    executed_list = []
    operations = opener_zip('operations.zip')
    for i in operations:
        if (id_key := i.get('state')) and id_key == 'EXECUTED':
            executed_list.append(i)
    return executed_list


filter_of_executed(operations=opener_zip('operations.zip'))


def sort_executed():
    executed_list = filter_of_executed(operations=opener_zip('operations.zip'))
    sort_list = sorted(executed_list, key=operator.itemgetter('date'), reverse=True)
    return sort_list


sort_executed()


def output_5_end_operations():
    ends_operations = sort_executed()
    ends_operations_list = []
    count = 5
    for i in ends_operations:
        if count != 0:
            count -= 1
            ends_operations_list.append(i)
    # return print(ends_operations_list)
    return ends_operations_list


output_5_end_operations()


def get_date():
    necessary_options = output_5_end_operations()
    for i in necessary_options:
        i['date'] = ".".join(i['date'].split('T')[0].split('-')[::-1])
    return necessary_options


get_date()


def get_requisites_view():
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


get_requisites_view()


def get_requisites_view_to():
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


get_requisites_view_to()


def show_to_user():
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


show_to_user()
