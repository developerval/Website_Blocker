import time
from datetime import datetime as dt

hosts_path = '/etc/hosts'
redirect = '127.0.0.1'
blocked_websites = {'www.facebook.com',
                    'facebook.com', 'www.youtube.com', 'youtube.com'}

while True:
    if 9 < dt.now().hour < 17:
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in blocked_websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        print("Fun hours!!!")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocked_websites):
                    file.write(line)
                file.truncate()
    time.sleep(10)
