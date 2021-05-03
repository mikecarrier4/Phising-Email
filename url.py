import numpy as np
from re import search
from query import Whois
from urllib.parse import urlparse
from get_url import get_url
from A_tag import A_tag
from Favcon import Favicon_pull

#Enter URL in <str>
url = input('Enter a Url Here, use fully qualified with https or http')
print('Website url is', (url))
url = url.lower()
domain_name = 0

#splitting domain name from url
if  type(url) != str or len(url) < 4:
    raise TypeError ('This is not a URL , please re enter a url')

#get_url Function
domain_name = get_url(url)
print('Domain name is ' ,domain_name)

#To acess whois db we need whois url + site domain for domain searching
whois_url = ("https://who.is/whois/" + str(domain_name))
print(whois_url)


#Rule1.1.8 using Whois Function & Rule 1.1.9
combined = Whois(whois_url, domain_name)
rule_1_1_8 = combined[0]
rule_1_1_9 = combined[1] 
#Rule1.1.1
if rule_1_1_8 == 1:
    rule1_1_1 = 1
else:
    rule1_1_1 = -1

#1.1.2 Rule
if len(url) < 54:
    rule_2 = 1
elif len(url) >= 54 and len(url) <= 75:
    rule_2 = 0
else:
    rule_2 = -1

#1.1.3 Rule
https_string = 'https'
http_string = 'http'
if search (https_string, url):
    rule_3 = 1
elif search (http_string, url):
    rule_3 = 1
else:
    rule_3 = -1
#1.1.4

rule_4 = []

if '@' in url:
    rule_4 = -1
else:
    rule_4 = 1

#1.1.5

rule_5 = []
if '///' in url:
    rule_5 = -1
elif '//' in url:
    if '//' in url[0:6]:
        rule_5 = -1
    elif '//' in url[8:]:
        rule_5 = -1
    else:
        rule_5 = 1
else:
    rule_5 = 1

#Rule 1.1.6

rule_6 = []
if '-' in domain_name:
    rule_6 = -1
else:
    rule_6 = 1

#Rule1.1.7
if rule_1_1_8 == 1:
    rule1_1_7 = 1
else:
    rule1_1_7 = -1

#Rule1.1.10
#Needs a Kill command commenting out for presentation
rule1_1_10 = 1
#rule1_1_10 = Favicon_pull(domain_name)
#print('Rule 10 is', rule1_1_10)
#Domain Name

#1.1.12
if 'http' in url:
    split_url12 = url.split('http')
    print('Rule 12', split_url12)
    if 'http' in split_url12[1]:
        rule1_1_12 = -1
    else:
        rule1_1_12 = 1


#1.2.2 URL Anchor
rule1_2_2 = A_tag(url, domain_name)


array = np.array((rule1_1_1, rule_2, rule_3, rule_4, rule_5, rule_6, rule1_1_7, rule_1_1_8, rule_1_1_9, rule1_1_10, rule1_1_12, rule1_2_2))
prediction_array = [array]
print(array)
print(type(prediction_array))