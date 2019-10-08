import re

root_path = 'C:\\Users\\Zhou_Charles\\Desktop\\'

login_userid = None
login_password = None

time_format_military = '%m/%d/%Y %H:%M'
process_name = 'Mass Update PU Appt'
note_entry_guide = '''
Note:
1. You must use comma "," as the separator if there are multiple entries.
2. Start a new line and enter "Y" once you complete.\n
'''


url_tms_login = 'https://dsclogistics.mercurygate.net/MercuryGate/login/LoginProcess.jsp'
url_list_transports = 'https://dsclogistics.mercurygate.net/MercuryGate/transport/listTransports.jsp'
url_list_shipments = 'https://dsclogistics.mercurygate.net/MercuryGate/shipment/listShipment.jsp'
url_tms_root = 'https://dsclogistics.mercurygate.net'
url_update_controller = 'https://dsclogistics.mercurygate.net/MercuryGate/transport/updateController.jsp'

url_post_transport_report_format = 'https://dsclogistics.mercurygate.net/MercuryGate/report/ReportFormat_process.jsp?' \
                              'type=Transport&summary=false'
url_get_transport_report_format0 = 'https://dsclogistics.mercurygate.net/MercuryGate/transport/listTransports.jsp?' \
                                   'sidAction=&action=&type=Transport&full=&nSetNumber=1&sReturnURL='
url_get_transport_report_format1 = 'https://dsclogistics.mercurygate.net/MercuryGate/transport/listTransports.jsp?' \
                                   'norefresh=&sidAction=&action=&type=Transport&full=&nSetNumber=1&sReturnURL='


g_sheets_workbook_id_log = '1Yudm7JfKSgL82zyHXnDKUjJfoI5VGoEsPHgysPXcZ4g'
g_sheets_worksheet_id_log = 0

re_pattern_csrf = re.compile('\<meta name\=\"_csrf\" content\=\"([\w\-]*)\" \/\>')
re_pattern_menu_value = re.compile('\<a href\=\"\.\.\/mainframe\/menuLHS\.jsp\?sMenuValue\=([\d\(\)\,]*)'
                                  '\&sMenuSelected\=\*\-\%3EDetail')
re_pattern_oid = re.compile('OID\' class\=\"DetailBodyTableRowOdd \"\>([\d]*)\<\/td\>')
re_pattern_load_ref = re.compile('Load Reference\' class\=\"DetailBodyTableRowOdd \"\>([\d]*) \(Load Number')
re_pattern_owner = re.compile('Owner\' class\=\"DetailBodyTableRowOdd \"\>([\s\w]*)\<\/td\>')
re_pattern_type = re.compile('Type\' class\=\"DetailBodyTableRowOdd \"\>([\sa-zA-Z]*)\<\/td\>')
re_pattern_origin_code = re.compile('Origin Code\' class\=\"DetailBodyTableRowOdd \"\>([\w\&\;\s]*)\<\/td\>')
re_pattern_dest_code = re.compile('Dest Code\' class\=\"DetailBodyTableRowOdd \"\>([\w\&\;\s]*)\<\/td\>')
re_pattern_trade = re.compile('Trade\' class\=\"DetailBodyTableRowOdd \"\>([\w]*)\<\/td\>')
re_pattern_carrier_mode = re.compile('Carrier Mode\' class\=\"DetailBodyTableRowOdd \"\>([\w]*)\<\/td\>')
re_pattern_actual_ship = re.compile('Actual Ship\' class\=\"DetailBodyTableRowOdd \"\>([\w\/\:\s]*)\<\/td\>')
re_pattern_url_transport_report_format = re.compile('\<script src\=\"([\/\w\.\?\=\-]*)\"')
re_pattern_pri_ref = re.compile('Primary Reference\' class\=\"DetailBodyTableRowOdd \"\>([\w]*) \(Load')


field_origin_code = 'OriginLocation.LocationCode'
field_create_date = 'CreateDate'
field_type = 'Type'
field_origin_state = 'OriginLocation.State'
field_origin_city = 'OriginLocation.City'
field_origin_name = 'OriginLocation.Name'
field_oid = 'Oid'
field_location_code = 'LocationCode'
field_name = 'Name'
field_city = 'City'
field_state = 'State'
field_address1 = 'Address1'
field_address2 = 'Address2'
field_postal_code = 'PostalCode'
field_country = 'Country'
field_status = 'Status'
field_agent_number = 'Ref: 16697125400'
field_batch = 'Ref: 53580617477'
field_bid_board = 'Ref: 54674644540'
field_bol = 'Ref: 1200'
field_customer_code = 'Ref: 61133800'
field_customer_ref_number = 'Ref: 4427918800'
field_del_appt = 'Ref: 4750584900'
field_del_late_party = 'Ref: 51370999000'
field_del_late_reason= 'Ref: 42601492700'
field_dsc_special_services = 'Ref: 40532775900'
field_first_tender = 'Ref: 54451972337'
field_item_not_matched = 'Ref: 16743044800'
field_load_number = 'Ref: 1174978200'
field_dest_not_matched = 'Ref: 17085562600'
field_origin_not_matched = 'Ref: 16743044900'
field_shipment_type = 'Ref: 4492548900'
field_tri = 'Ref: 54192117830'
field_trade= 'Ref: 19217908000'
field_subtrade = 'Ref: 54144713184'
field_assigned_to = 'AssignedTo'
field_carrier_scac = 'FirstSelectedChargeSheet.CarrierSCAC'
field_pri_ref = 'PrimaryReference'

filter_equal = 'Equal'
filter_in = 'In'
filter_not_in = 'Not In'
filter_not_equal = 'Not Equal'
filter_from_today = 'From Today'
filter_begins_with = 'Begins With'
filter_not_begins_with = 'Not Begin With'

# oid_enterprise = 16682284300 #Legacy
oid_enterprise = 54775198209 #ezVision

html_equivalence_and = '&amp;'

re_pattern_dict = {
    'oid': re_pattern_oid
}

transport_by_report_format_dict = {
    '_csrf': '',
    'sourceurl': '',
    'sReturnURL': '',
    'full': '',
    'action': '     Use     ',
    'col0': 'Oid',
    'col1': '',
    'col2': '',
    'col3': '',
    'col4': '',
    'col5': '',
    'col6': '',
    'col7': '',
    'col8': '',
    'col9': '',
    'col10': '',
    'filterfield0': '', 'filtercrit0': '', 'filtervalue0': '',
    'filterfield1': '', 'filtercrit1': '', 'filtervalue1': '',
    'filterfield2': '', 'filtercrit2': '', 'filtervalue2': '',
    'filterfield3': '', 'filtercrit3': '', 'filtervalue3': '',
    'filterfield4': '', 'filtercrit4': '', 'filtervalue4': '',
    'filterfield5': '', 'filtercrit5': '', 'filtervalue5': '',
}

set_assign_to_dict = {
    '_csrf': '',
    'sidOwner': '',
    'sReturnURL': '',
    'sAssignTo': ''
}


post_data_update_appt = {
    '_csrf': '',
    'sCancelURL': '',
    'sidAction': '',
    'SelectedObjs': '',
    'redirectURL': '',
    'investigateValue': '',
    'AssignedTo': '',
    'sAction': 'UpdateAptTime',
    'sAptDateModifyOption': '',
    'dateupdateApptTimeEarly': '',
    'hoursupdateApptTimeEarly': '',
    'minutesupdateApptTimeEarly': '',
    'dateupdateApptTimeLate': '',
    'hoursupdateApptTimeLate': '',
    'minutesupdateApptTimeLate': ''
}