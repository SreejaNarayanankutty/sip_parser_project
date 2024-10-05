from utils.sip_details import FetchSIPMessageDetails

def print_sip_message_details(file_path):
    fetch_sip_details_obj = FetchSIPMessageDetails(file_path)
    request_uri = fetch_sip_details_obj.get_request_uri()
    sip_headers = fetch_sip_details_obj.get_sip_header()
    sip_body = fetch_sip_details_obj.get_sip_body()
    method_name = fetch_sip_details_obj.get_method_name()

    header_data = ''
    body_data = ''

    for key in sip_headers.keys():
        header_data = ''.join([header_data, f'\t{key}: {sip_headers[key]}\n'])

    for data in sip_body:
        body_data = ''.join([body_data, data])

    print(f'\"""\nThe given SIP message is a request with:\n'
          f'request-uri: {request_uri}\n'
          f'method: {method_name}\n'
          f'headers:\n{header_data}'
          f'and body:\n\t{body_data}\n\"""')


