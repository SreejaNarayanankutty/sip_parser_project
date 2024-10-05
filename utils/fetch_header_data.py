from utils.sip_details import FetchSIPMessageDetails

def verify_and_fetch_header_data(header_name_to_verify, file_path):
    fetch_sip_details_obj = FetchSIPMessageDetails(file_path)
    header_name_to_verify = header_name_to_verify.lower()
    header_presence_flag = False
    header_value = ''
    sip_headers_from_file = fetch_sip_details_obj.get_sip_header()
    for key in sip_headers_from_file.keys():
        if key.lower() == header_name_to_verify:
            header_presence_flag = True
            header_value = ''.join([header_value, f'\t{key}: {sip_headers_from_file[key]}\n'])

    if header_presence_flag:
        print(f'\"{header_name_to_verify}\" header is present in SIP request as below:\n{header_value}')
    else:
        print(f'\"{header_name_to_verify}\" header is not present in SIP Request.')
