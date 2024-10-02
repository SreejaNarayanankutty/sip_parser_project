import re


def parse_sip_file(file_path):
    # print("inside parse file")
    with open(file_path, 'r') as sip_file:
        lines = sip_file.readlines()
        # print(lines)
        return lines


def separate_details(file_path):
    lines = parse_sip_file(file_path)
    sipheaders = {}
    sipbody = []
    requesturi = lines[0].strip()
    # print(requesturi)
    for line in lines[1:]:
        line = line.strip()
        if re.search(r'.*:\s.*', line):
            print(re.split(r'.*:\s.*', line))
            [header, value] = re.split(r':\s', line)
            # print(header+":"+value)
            sipheaders[header] = value
        if not line or not re.search(r'.*:\s.*', line):
            sipbody.append(line)
    # print(sipheaders)
    # print(sipbody)
    return requesturi, sipheaders, sipbody


def print_message_details(file_path):
    requesturi, sipheaders, sipbody = separate_details(file_path)
    methodname = re.split(r'\ssip:', requesturi)[0]
    headerData = ""
    bodyData = ""
    for key in sipheaders.keys():
        print("inside join headers")
        headerData = ''.join([headerData, f'\t{key}: {sipheaders[key]}\n'])
    for data in sipbody:
        bodyData = ''.join([bodyData, data])
    print(headerData)

    print(f'\"""\nThe given SIP message is a request with:\n'
          f'request-uri: {requesturi}\n'
          f'method: {methodname}\n'
          f'headers:\n{headerData}'
          f'and body:\n\t{bodyData}\n\"""')


def main():
    # print("hello inside main")
    print_message_details("./data/sip_request.txt")


if __name__ == "__main__":
    main()
