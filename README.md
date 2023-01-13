# Network Vulnerability Scanner
> A Network Programming course project

A Python script that scans a target system for open ports and known vulnerabilities.

## Requirements
- Python 3.x
- requests library
- json library
- smtplib library

## Usage
1. Replace the `ip` variable with the target IP address or hostname.
2. Replace the `ports` variable with the ports you want to scan.
3. Replace the credentials and the recipient email for the email alerts.
4. Run the script: ```python scanner.py```

## Features

* Scans for open ports on the target system
* Identifies the software running on each open port
* Checks for known vulnerabilities of the software
* Send email alerts when vulnerabilities are detected

### Note

* The NVD API has a usage limit, so you might need to get an API key to be able to use it.
* Make sure that the usage of the IP address you provided is allowed by the internet service provider.
* This is a simple example, to get more information about the vulnerabilities, you might need to explore other data sources and APIs like the Common Vulnerabilities and Exposures (CVE) database or the Open Vulnerability and Assessment Language (OVAL).
