from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
from datetime import datetime
from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json


def Whois(whois_url, domain_name):
    page = urlopen(whois_url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    stringtxt = soup.get_text()
    list = stringtxt.splitlines()
    za = list
    
    now = datetime.now()
    try:
        for index, value in enumerate(za):
            if 'Expires On' in value:
                search_index = index + 1
                print(za[index])
                date_time_str = za[search_index]
                date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
                print(date_time_obj)
                if date_time_obj > now:
                    rule1_1_8 = 1
                    print('Found it')
                    break
                else:
                    rule1_1_8 = -1
                    break
   
        


#some site without http/https in the path

        if rule1_1_8 == 1:

            base_url = domain_name
            port = '443'

            hostname = base_url
            context = ssl.create_default_context()

            with socket.create_connection((hostname, port)) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    print(ssock.version())
                    data = json.dumps(ssock.getpeercert())
                    # print(ssock.getpeercert())
            print(data)

            if len(data) > 1:
                rule1_1_8 = 1
            else:
                rule1_1_8 = 0

            
            #Rule 1.1.9
        one_year_out = now.replace(year = now.year +1)
        if date_time_obj < one_year_out:
            rule1_1_9 = 1
        else:
            rule1_1_9 = -1

    except:
        rule1_1_8 = -1
        rule1_1_9 = -1

    

        



    return [rule1_1_8, rule1_1_9]





