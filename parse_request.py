import argparse

from utils.fetch_header_data import verify_and_fetch_header_data
from utils.print_details import print_sip_message_details
from utils.validate_compliance import validate_sip_message


def main():
    # Defining command line option to parse sip test file to perform various function
    arg_parser = argparse.ArgumentParser(description="SIP Request Parser Command Line Interface")
    group = arg_parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-p', '--print', action='store_true', help="To print details in sip message")
    group.add_argument('-e','--exists', action='store_true', help="To verify given header in sip message")
    group.add_argument('-v','--validate', action='store_true', help="To validate sip message based on RFC3261")

    arg_parser.add_argument('header_name', nargs='?', type=str, help="To pass header name to verify in sip message")
    arg_parser.add_argument('file', type=str, help="Path to the text file containing SIP request")

    execute_args = arg_parser.parse_args()

    # Execute various function based on command line
    try:
        if execute_args.print:
            print_sip_message_details(execute_args.file)
        elif execute_args.exists and execute_args.header_name:
            verify_and_fetch_header_data(execute_args.header_name, execute_args.file)
        elif execute_args.validate:
            validate_sip_message(execute_args.file)
        else:
            print('Please provide valid command line options. Use --help for more information.')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()
