from datetime import datetime, timedelta
from dateutil import parser
import Constant


def confirm_input(key, value):
    confirmed = None
    if ',' in value:
        load_numbers = value.replace(',', ' ').strip().split()
        s = 'The ' + key + ' you entered is: ' + value + '.\n'
        s += 'Total count: ' + str(len(load_numbers)) + ' (Y/N)?'
    else:
        s = 'The ' + key + ' you entered is: ' + value + ' (Y/N)?'
    while confirmed is None:
        confirmation = input(s)
        if confirmation.lower() == 'y':
            confirmed = True
        elif confirmation.lower() == 'n':
            confirmed = False
    return confirmed


def check_date(date_to_check):
    now = datetime.now()
    past = now - timedelta(days=30)
    future = now + timedelta(days=90)
    if past <= date_to_check <= future:
        return date_to_check
    else:
        print('Error: Please enter date from past 30 days to next 90 days.')
        return None


def parse_date(date_to_parse):
    try:
        date_to_parse = parser.parse(date_to_parse)
        return date_to_parse
    except ValueError:
        print('Error: Please enter date in the format of MM/DD/YY.')
        return None


def parse_time(time_to_parse):
    try:
        time_to_parse = parser.parse(time_to_parse)
        return time_to_parse
    except ValueError:
        print('Error: Please enter time in the format of HH:MM.')
        return None


def get_date(date_name):

    parsed_date = None
    while parsed_date is None:
        input_date = input('Please enter ' + date_name + ' (MM/DD/YY): ')
        parsed_date = parse_date(input_date)

        if parsed_date:
            parsed_date = check_date(parsed_date)

        if parsed_date is not None:
            parsed_date = parsed_date.strftime('%m/%d/%Y')
            if not confirm_input(date_name, parsed_date):
                parsed_date = None
    return parsed_date


def get_time(time_name):

    parsed_time = None
    while parsed_time is None:
        input_time = input('Please enter ' + time_name + ' (HH:MM): ')
        parsed_time = parse_date(input_time)

        if parsed_time is not None:
            parsed_time = parsed_time.strftime('%H:%M')
            if not confirm_input(time_name, parsed_time):
                parsed_time = None
    return parsed_time


def get_general_input(input_name):

    completed = False
    confirmed = False
    general_input = ''
    iter_input = ''

    while not confirmed:
        print(Constant.note_entry_guide)
        print('Please enter ', input_name, ':')
        while not completed:
            general_input += iter_input
            iter_input = input()

            if iter_input.lower() == 'y':
                completed = True

        confirmed = confirm_input(input_name, general_input)

        if not confirmed:
            completed = False
            confirmed = False
            general_input = ''
            iter_input = ''

    return general_input


