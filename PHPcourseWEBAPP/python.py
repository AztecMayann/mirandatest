
#!/usr/bin/env python3
import requests
import socket


def check_localhost():
        localhost = socket.gethostbyname('localhost')
        host = '127.0.0.1'
        if host == localhost:
                return True



def check_connectivity():
        request = requests.get("https://www.google.com")
        if request.status_code == 200:
            return True
