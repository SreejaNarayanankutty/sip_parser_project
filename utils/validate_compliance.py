import re

from utils import constants
from utils.sip_details import FetchSIPMessageDetails


def check_for_missing_header(sip_headers_in_message):
    missing_headers_list = []
    missing_headers = ''
    for i in constants.MANDATORY_HEADERS:
        presence_flag = False
        for j in sip_headers_in_message:
            if i.lower() == j.lower():
                presence_flag = True
                continue
        if not presence_flag:
            missing_headers_list.append(i)
            missing_headers = ','.join(missing_headers_list)
    return missing_headers


def validate_sip_message(file_path):
    fetch_sip_details_obj = FetchSIPMessageDetails(file_path)
    sip_headers = fetch_sip_details_obj.get_sip_header()
    request_uri = fetch_sip_details_obj.get_request_uri()

    sip_headers_in_message = sip_headers.keys()
    missing_headers = check_for_missing_header(sip_headers_in_message)

    validation_flag = True

    if not missing_headers:
        sip_headers_lowercase = {key.lower(): value for key, value in sip_headers.items()}
        to_header_val = sip_headers_lowercase.get(constants.TO_HEADER)
        from_header_val = sip_headers_lowercase.get(constants.FROM_HEADER)

        domain_name_in_to_header = re.findall(constants.DOMAIN_NAME_PATTERN, to_header_val)[0]

        if request_uri and re.search(constants.REGISTER_REQ_URI, request_uri):
            pass
        elif request_uri and re.search(
                rf'{constants.OTHER_METHOD_NAME_PATTERN}\s{re.escape(domain_name_in_to_header)}\s{constants.SIP_PROTOCOL_PATTERN}',
                request_uri):
            pass
        else:
            validation_flag = False
            print(f'\"""\nThe verification of the request failed due to the following reason(s):\n'
                  f'Error: The Request-URI is not valid, as required by "RFC3261 Section 8.1.1.1"\n'
                  f'\""".')

        if re.search(constants.TO_HEADER_VALUE_PATTERN, to_header_val, re.IGNORECASE):
            pass
        else:
            validation_flag = False
            print(f'\"""\nThe verification of the request failed due to the following reason(s):\n'
                  f'Error: The To header is not valid, as required by "RFC3261 Section 8.1.1.2"\n'
                  f'\""".')

        if re.search(constants.FROM_HEADER_VALUE_PATTERN, from_header_val, re.IGNORECASE):
            pass
        else:
            validation_flag = False
            print(f'\"""\nThe verification of the request failed due to the following reason(s):\n'
                  f'Error: The From header is not valid, as required by "RFC3261 Section 8.1.1.3"\n'
                  f'\""".')

    else:
        validation_flag = False
        print(f'\"""\nThe verification of the request failed due to the following reason(s):\n'
              f'Error: The \"{missing_headers}\" header is missing, as required by "RFC3261 Section 8.1.1"\n'
              f'\""".')

    if validation_flag:
        print(f'\"""\nThe request has been verified and no issues were found.\n'
              f'\"""')
