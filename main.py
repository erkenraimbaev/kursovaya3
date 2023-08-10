from utils__ import opener_zip, filter_of_executed, sort_executed, output_5_end_operations, get_date
from utils__ import get_requisites_view, get_requisites_view_to, show_to_user

opener_zip(filename='operations.zip')
filter_of_executed(operations=opener_zip(filename='operations.zip'))
sort_executed()
output_5_end_operations()
get_date()
get_requisites_view()
get_requisites_view_to()
show_to_user()