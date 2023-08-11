from utils__ import opener_zip, filter_of_executed, sort_executed, output_5_end_operations, get_date
from utils__ import get_requisites_view, get_requisites_view_to, show_to_user

#Загружаем данные из zip
opener_zip(filename='operations.zip')
#Вытаскиваем выполненные операции
filter_of_executed()
#Сортируем по дате, последние вверху списка
sort_executed()
#Выводим последние5
output_5_end_operations()
#Меняем отображение даты
get_date()
#Меняем отображение реквизитов from
get_requisites_view()
#Меняем отображение реквизитов to
get_requisites_view_to()
#Выводим информацию пользователю
show_to_user()
