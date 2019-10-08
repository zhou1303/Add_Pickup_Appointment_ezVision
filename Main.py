import Constant
import Post_Data
import Get_Data
import Config_Post_Data
import time
import G_API
import Input_Collection as Input


if __name__ == '__main__':

    # READ USER LOGIN CREDENTIALS FROM TEXT FILE.
    Get_Data.read_login_credentials()

    # GET INPUT FROM USER.
    input_load_number = 'load number'
    input_pickup_appointment_date = 'pickup appointment date'
    input_pickup_appointment_time = 'pickup appointment time'

    load_numbers = Input.get_general_input(input_load_number)
    pickup_appointment_date = Input.get_date(input_pickup_appointment_date)
    pickup_appointment_time = Input.get_time(input_pickup_appointment_time)

    # START COUNTING RUNNING TIME
    start = time.time()

    print('Pickup appointment', pickup_appointment_date, pickup_appointment_time, 'will be added to load(s):',
          load_numbers, '.')

    # LOGIN TMS
    session_requests, csrf = Post_Data.login_tms()
    count = 0

    print('Adding pickup appointment...')

    # GROUP LOAD NUMBERS.
    load_number_list = Get_Data.group_load_numbers(load_numbers)

    # LOOP 100 LOADS EACH TIME.
    for loads in load_number_list:
        concatenated_loads = ','.join(i for i in loads)
        transport_report_data_dict = Config_Post_Data.config_transport_pickup_appt(csrf, concatenated_loads)

        Get_Data.get_transport_report_by_report_format(session_requests, transport_report_data_dict)

        # ADD PU APPT
        appt_update_data_dict = Config_Post_Data.config_update_pickup_appt(csrf, load_numbers=loads,
                                                                           appt_date=pickup_appointment_date,
                                                                           appt_time=pickup_appointment_time)

        Post_Data.update_appt(session_requests, appt_update_data_dict)

    # END TIME
    end = time.time()

    # UPDATE LOG REPORT ON GOOGLE SHEETS
    duration = end - start
    workbook_log = G_API.get_workbook_by_id(Constant.g_sheets_workbook_id_log)
    worksheet_log = G_API.get_worksheet_by_id(workbook_log, Constant.g_sheets_worksheet_id_log)
    Post_Data.log_event(worksheet_log, duration)

    print('Pickup appointment has been successfully added.')
    time.sleep(10)

# save_file = open(Constant.root_path + 'test.html', 'w+')
# save_file.write(html_script)
# save_file.close()