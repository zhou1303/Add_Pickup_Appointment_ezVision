import Constant


def get_transport_report_by_report_format(session_requests, data_dict):
    response = session_requests.post(
        Constant.url_post_transport_report_format,
        data_dict
    )

    html_script = response.text
    urls = Constant.re_pattern_url_transport_report_format.findall(html_script)
    for url in urls:
        session_requests.get(Constant.url_tms_root + url)

    response = session_requests.get(Constant.url_get_transport_report_format0)
    html_script = response.text
    urls = Constant.re_pattern_url_transport_report_format.findall(html_script)
    for url in urls:
        session_requests.get(Constant.url_tms_root + url)

    response = session_requests.get(Constant.url_get_transport_report_format1)

    return response


def group_load_numbers(load_numbers):
    load_numbers = load_numbers.replace(',', ' ').strip().split()
    load_number_list = [load_numbers[i:i + 100] for i in range(0, len(load_numbers), 100)]
    return load_number_list


def read_login_credentials():
    login_userid = open('username.txt', mode='r')
    login_password = open('password.txt', mode='r')

    Constant.login_userid = login_userid.read()
    Constant.login_password = login_password.read()

    print('User credentials read successfully.')
