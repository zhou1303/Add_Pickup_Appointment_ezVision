import Constant


def config_transport_pickup_appt(csrf, load_numbers):
    data_dict = Constant.transport_by_report_format_dict.copy()
    data_dict['_csrf'] = csrf

    data_dict['col1'] = Constant.field_pri_ref
    data_dict['filterfield0'] = Constant.field_pri_ref
    data_dict['filtercrit0'] = Constant.filter_in
    data_dict['filtervalue0'] = load_numbers

    return data_dict


def config_update_pickup_appt(csrf, load_numbers, appt_date, appt_time):

    data_dict = Constant.post_data_update_appt.copy()

    data_dict['_csrf'] = csrf
    data_dict['sAptDateModifyOption'] = 'firstPickup'

    selected_objs = ','.join(str(i) for i in range(len(load_numbers)))
    check_sids = ['checkSid' + str(i) for i in range(len(load_numbers))]

    data_dict['SelectedObjs'] = selected_objs + ','

    for i, check_sid in enumerate(check_sids):
        data_dict[check_sid] = load_numbers[i] + ' (null)'

    data_dict['dateupdateApptTimeEarly'] = appt_date
    data_dict['hoursupdateApptTimeEarly'] = appt_time[:2]
    data_dict['minutesupdateApptTimeEarly'] = appt_time[-2:]
    data_dict['dateupdateApptTimeLate'] = appt_date
    data_dict['hoursupdateApptTimeLate'] = appt_time[:2]
    data_dict['minutesupdateApptTimeLate'] = appt_time[-2:]

    return data_dict


def config_update_delivery_appt(csrf, load_number, appt_date, appt_time):
    data_dict = config_update_pickup_appt(csrf, load_number, appt_date, appt_time)
    data_dict['sAptDateModifyOption'] = 'lastDrop'

    return data_dict
