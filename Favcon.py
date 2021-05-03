# importing the libraries
from bs4 import BeautifulSoup
import requests
import time

domain_name = 'youtufdsabe.com'
rule1_1_10 = 0
def Favicon_pull(domain_name):

   
    url= ("https://www." + domain_name + "/favicon.ico")
    try:

# Make a GET request to fetch the raw HTML content
        html_content = requests.get(url).text

# Parse the html content
        soup = BeautifulSoup(html_content)
        print(soup.prettify()) # print the parsed data of html
        if len(soup.prettify()) > 10:
            rule1_1_10 = 1
    except:
        rule1_1_10 = 0

    return rule1_1_10

rule1_1_10 = Favicon_pull(domain_name)
print(rule1_1_10)