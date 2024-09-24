### Overview
A Python program to analyze a log file and summarize the results.

### Requirements:
    - Python 3.x
    - External modules: `tabulate` for output formatting, 'PyYAML' to load, parse, and write YAML
    
To install modules:
```
pip install -r requirements.txt
```
### Assumptions:
- Log file has been downloaded.
- A config file has been created to store the path of the log file.

### Usage:

```
python log_analyzer.py

or

python3 log_analyzer.py
```

Sample Output:
```
Total requests per pod:
Pod                                          Count
-----------------------------------------  -------
ingress-nginx-controller-7b5855865f-7c8b4       75

Response code summary:
  http_response_codes    Count
---------------------  -------
                  404       42
                  200       33

Total bytes sent per pod:
Pod                                          Total Bytes
-----------------------------------------  -------------
ingress-nginx-controller-7b5855865f-7c8b4        5968259

Unique request paths:
----------------------------------------------------------
"GET /data/wasser/still/34 HTTP/2.0"
"GET /data/spirituosen/eiswuerfel-spirituosen/33 HTTP/2.0"
"GET /data/spirituosen/gin-wacholder/33 HTTP/2.0"
"GET /data/spirituosen/weitere-spirituosen/31 HTTP/2.0"
```
