import re
import argparse
import string


def parse_sip_file(file_path):
    with open(file_path, 'r') as sip_file:
        lines = sip_file.readlines()
        return lines


def fetch_sip_message_details(file_path):
    lines = parse_sip_file(file_path)
    sip_headers = {}
    sip_body = []
    request_uri = lines[0].strip()
    sip_message_details = {}
    for line in lines[1:]:
        line = line.strip()
        if re.search(r'.*:\s.*', line):
            [header, value] = re.split(r':\s', line)
            sip_headers[header] = value
        if not line or not re.search(r'.*:\s.*', line):
            sip_body.append(line)
    sip_message_details['request_uri'] = request_uri
    sip_message_details['headers'] = sip_headers
    sip_message_details['body'] = sip_body

    return sip_message_details


def print_sip_message_details(file_path):
    sip_message_details = fetch_sip_message_details(file_path)
    request_uri = sip_message_details['request_uri']
    sip_headers = sip_message_details.get('headers')
    sip_body = sip_message_details.get('body')
    header_data = ""
    body_data = ""
    method_name = re.split(r'\ssip:', sip_message_details.get('request_uri'))[0]
    for key in sip_headers.keys():
        header_data = ''.join([header_data, f'\t{key}: {sip_headers[key]}\n'])
    for data in sip_body:
        body_data = ''.join([body_data, data])

    print(f'\"""\nThe given SIP message is a request with:\n'
          f'request-uri: {request_uri}\n'
          f'method: {method_name}\n'
          f'headers:\n{header_data}'
          f'and body:\n\t{body_data}\n\"""')


def verify_and_fetch_header_data(header_name_to_verify, file_path):
    header_name_to_verify = header_name_to_verify.lower()
    header_presence_flag = False
    header_value = ''
    sip_headers_from_file = fetch_sip_message_details(file_path).get('headers')
    for key in sip_headers_from_file.keys():
        if key.lower() == header_name_to_verify:
            header_presence_flag = True
            header_value = ''.join([header_value, f'\t{key}: {sip_headers_from_file[key]}\n'])

    if header_presence_flag:
        print(f'\"{header_name_to_verify}\" header is present in SIP request as below:\n{header_value}')
    else:
        print(f'\"{header_name_to_verify}\" header is not present in SIP Request.')

def validate_sip_message(file_path):
    mandatory_headers = {'To', 'From', 'CSeq', 'Call-Id', 'Via', 'Max-Forwards'}
    sip_message_details = fetch_sip_message_details(file_path)
    sip_headers = sip_message_details.get('headers').keys()
    sip_headers_lower = [item.lower() for item in sip_headers]
    missing_headers_list= []
    missing_headers = ''
    validation_flag = False
    for i in mandatory_headers:
        miss_flag = False
        for j in sip_headers_lower:
            if i.lower() == j.lower():
                miss_flag = True
                continue
        if not miss_flag:
            missing_headers_list.append(i)
            missing_headers = ','.join(missing_headers_list)
    if not missing_headers_list:
        validation_flag = True
    else:
        print(f'\"""\nThe verification of the request failed due to the following reason(s):\n'
              f'Error: The \"{missing_headers}\" header is missing, as required by "RFC3261 Section 8.1.1"\n'
              f'\""".')

    if validation_flag:
        print(f'\"""\nThe request has been verified and no issues were found.\n'
              f'\"""')


def main():
    # Defining command line option to parse sip test file and perform various function
    arg_parsor = argparse.ArgumentParser(description="SIP Request Parser Command Line Interface", argument_default=argparse.SUPPRESS)

    arg_parsor.add_argument('-p', action='store_true', help="flag p to print details in sip message")
    arg_parsor.add_argument('--print', action='store_true', help="flag print to print details in sip message")

    #arg_parsor.add_argument('-e', action='store_true', help="flag p to verify given header details in sip message")
    #arg_parsor.add_argument('--exists', action='store_true', help="flag print to verify given header details in sip message")
    #arg_parsor.add_argument('header', type=str, help="header to search in sip message")

    arg_parsor.add_argument('file', type=str, help="Path to the text file containing SIP request")

    execute_args = arg_parsor.parse_args()

    # Execute command line
    if execute_args.p and execute_args.print:
        print_sip_message_details(execute_args.file)
    #if execute_args.e and execute_args.exists and execute_args.header:
        #verify_and_fetch_header_data(execute_args.header, execute_args.file)



if __name__ == "__main__":
    main()
