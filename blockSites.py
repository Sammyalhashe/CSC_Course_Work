import time
from datetime import datetime as dt

temp_host = r".\host"
host = r"C:\Windows\System32\drivers\etc"
localhost = '127.0.0.1'

sites = ['www.facebook.com', 'facebook.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 22) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("Work Time...")
        with open(host, 'r+') as fh:
            content = fh.read()
            for site in sites:
                if site in content:
                    pass
                else:
                    fh.write(localhost + ' ' + site + '\n')
    else:
        print("Free Time...")
        with open(host, 'r+') as fh:
            lines = fh.readlines()
            fh.seek(0)
            for line in lines:
                print(line, any([site in line for site in sites]))
                if not any([site in line for site in sites]):
                    fh.write(line)
            fh.truncate()
    time.sleep(500)
