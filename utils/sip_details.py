import re
from utils import constants

class FetchSIPMessageDetails:
    def __init__(self, file_path):
        self._file_path = file_path
        self._lines = None
        self._request_uri = None
        self._sip_body = []
        self._sip_headers = {}
        self._method_name = None
        self.parse_sip_file()
        self.set_request_uri()
        self.set_method_name()
        self.set_sip_header_and_body()

    def parse_sip_file(self):
        with open(self._file_path, 'r') as sip_file:
            self._lines = sip_file.readlines()

    def set_request_uri(self):
        self._request_uri = self._lines[0].strip()

    def set_sip_header_and_body(self):
        for line in self._lines[1:]:
            line = line.strip()
            if re.search(constants.HEADER_SEARCH_PATTERN, line):
                [header, value] = re.split(r':\s', line)
                self._sip_headers[header] = value
            if not line or not re.search(constants.HEADER_SEARCH_PATTERN, line):
                self._sip_body.append(line)

    def set_method_name(self):
        self._method_name = re.split(constants.METHOD_SPLIT_PATTERN, self._request_uri)[0]

    def get_request_uri(self):
        return self._request_uri

    def get_sip_header(self):
        return self._sip_headers

    def get_sip_body(self):
        return self._sip_body

    def get_method_name(self):
        return self._method_name


