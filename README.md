# SIP Parser Project

This project is a Python CLI program which will take SIP request file as input and do following functions based on different command line parameters;

# Table of Contents
- [Installation](#Installation)
- [Usage](#Usage)

## Installation
1. Clone repository and install required dependencies

## Usage
This program support below Command line arguments.
1. -p --print: The .txt file is parsed and the following message is printed:
      ```
      """
       The given SIP message is a request with:
       request-uri: <request-uri>
       method: <method>
       headers:
          <header-1>: <header-1-content>
          <header-1>: <header-1-content>
          <...>: <...>
       and body:
          <raw-body>
       """ 
     ```

2. -e --exists <header-name>': The .txt file is parsed and the program prints whether the given header exists and what its contents are.
3. -v --validate': The .txt file is parsed and the request should be checked for compliance with the RFC3261 Sections 8.1.1, 8.1.1.1, 
   8.1.1.2 and 8.1.1.3. 
   - In case no issues are found, such as with the attached example file 'sip_request.txt', the following 
      message should be printed:
        ```
         """
         The request has been verified and no issues were found. 
         """
       ```
   - If an issue is found, such as the Call-ID missing in violation of RFC3261 Section 8.1.1 in the attached example file
     'sip_request_without_call_id.txt', an error similar to the one shown below should be printed:
      ```
         """
         The verification of the request failed due to the following reason(s):
         Error: The "Call ID" header is missing, as required by "RFC3261 Section 8.1.1"  
         """
      ```  

Reference: https://rfc-editor.org/rfc/rfc3261#section-8.1.1
