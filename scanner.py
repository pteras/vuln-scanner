import socket
import requests
import json
import smtplib

# target IP address
ip = "127.0.0.1"

# ports to scan (top ports)
ports = [21, 22, 23, 25, 53, 80, 110, 111,135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]

# email credentials to send alerts
username = "your_email@example.com"
password = "your_password"

# email recipient
recipient = "alerts@example.com"

# service detection function


def service_detection(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, port))
        sock.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
        banner = sock.recv(1024)
        if b"Apache" in banner:
            return "Apache"
        elif b"nginx" in banner:
            return "nginx"
        else:
            return "Unknown"
    except:
        return "Unknown"
    finally:
        sock.close()

# function to check for known vulnerabilities


def check_vulnerabilities(software):
    # NVD API endpoint
    url = "https://services.nvd.nist.gov/rest/json/cve/1.1?product={}".format(
        software)
    # send GET request to NVD API
    response = requests.get(url)
    # parse response as JSON
    data = json.loads(response.text)
    # check if there are any vulnerabilities
    if data["totalResults"] == 0:
        return "No known vulnerabilities"
    else:
        return "Known vulnerabilities found"

# function to send email alert


def send_alert(vulnerability):
    subject = "Vulnerability Alert"
    body = "A vulnerability was detected: {}".format(vulnerability)

    msg = "Subject: {}\n\n{}".format(subject, body)

    server = smtplib.SMTP("smtp.example.com")
    server.starttls()
    server.login(username, password)
    server.sendmail(username, recipient, msg)
    server.quit()


# iterate through the ports
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((ip, port))
    if result == 0:
        software = service_detection(ip, port)
        if software != "Unknown":
            vulnerability = check_vulnerabilities(software)
            print("Port {}: {} - {}".format(port, software, vulnerability))
            if vulnerability != "No known vulnerabilities":
                send_alert(vulnerability)
        else:
            print("Port {}: {}".format(port, software))
    else:
        print("Port {}: Closed".format(port))
    sock.close()
