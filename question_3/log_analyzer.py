"""
Log File Analyzer Script
"""

import re
from tabulate import tabulate
import yaml
import traceback

# Path of the Log file to be analyzed
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

def log_analyzer(log_file):
    """
    This function analyzes the log file and extracts useful information related to pods. It parses the log files, extracts key data, and outputs metrics such as the total requests per pod, HTTP response code summary,
    total bytes sent per pod, and a list of unique request paths.

    Parameters:
        log_file: Path of the Log file to be analyzed

    Output: 
        - Total requests per pod: Count the number of requests coming from each ingress pod.
        - Response code summary: Count how many times each HTTP response code appears in the logs.
        - Total bytes sent per pod: Sum the total number of bytes sent for requests coming from each pod.
        - Unique request paths: List all unique request paths that were logged.
    
    """
    try:
        # Regex pattern to match the log file format
        log_pattern = r'(?P<Pod_Name>\S+) (?P<Container>\S+) (?P<IP_Address>\S+) (\S+) (\S+) (?P<Timestamp>\[([\w:/]+\s[+\-]\d{4})\]) (?P<Request_Path>"(\S+) (\S+)\s*(\S*)") (?P<HTTP_ResponseCode>\d{3}) (?P<Bytes_Sent>\d+)'

        # Initialization of data structures to store the values
        pod_count = {}                  # Dictionary to store the count of requests coming from each ingress pod
        http_response_codes = {}        # Dictionary to store the count of each http response code
        total_bytes_sent_per_pod = {}   # Dictionary to store the sum of total number of bytes sent for each pod
        unique_request_paths = set()    # Set to store unique request paths

        # Open the log file and read line by line
        with open(log_file, 'r') as file:
            for line in file:
                # Match the log line using the regex pattern of log
                match = re.match(log_pattern, line)
                if match:
                    # Store the unique pod names and update the pod request count
                    pod_count[match.group('Pod_Name')] = pod_count.get(match.group('Pod_Name'), 0)+ 1

                    # Store the HTTP response codes and update the response code count
                    http_response_codes[match.group('HTTP_ResponseCode')] = http_response_codes.get(match.group('HTTP_ResponseCode'), 0)+ 1

                    # Store the unique pod names and update the sum of total bytes sent per pod
                    total_bytes_sent_per_pod[match.group('Pod_Name')] = total_bytes_sent_per_pod.get(match.group('Pod_Name'), 0) + int(match.group('Bytes_Sent'))
                    
                    # Add the request paths to the set of unique request paths
                    unique_request_paths.add(match.group('Request_Path'))

        # Output the analysis of logs
        print("Total requests per pod: \n" + tabulate([[pod, count] for pod, count in pod_count.items()], headers = ['Pod', 'Count']))

        print("\nResponse code summary: \n" + tabulate([[code, count] for code, count in http_response_codes.items()], headers = ['http_response_codes', 'Count']))

        print("\nTotal bytes sent per pod: \n" + tabulate([[pod, bytes] for pod, bytes in total_bytes_sent_per_pod.items()], headers = ['Pod', 'Total Bytes']))

        print(tabulate([[item] for item in unique_request_paths], headers=['\nUnique request paths:']))
        
    except Exception as e:
        traceback.print_exc()
        raise e

if __name__=="__main__":
    log_analyzer(config['log_file_path'])