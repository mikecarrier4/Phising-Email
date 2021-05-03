from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def A_tag (url, domain_name):

    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        web_byte = urlopen(req).read()

        webpage = web_byte.decode('utf-8', errors = 'ignore')
        soup = BeautifulSoup(webpage, 'html.parser')

        anchor_txt = ''
        anchor_list = []
        for link in soup.findAll('a', href = True):
                anchor_txt = link['href']
                anchor_list.append(anchor_txt)
                
        
        number_of_links = len(anchor_list)
        count_domain = 0
        for line in anchor_list:
            if domain_name in line:
                count_domain = count_domain +1
                print(line)
        
                

        Domain_listed_anchors = (count_domain / number_of_links)
        print(Domain_listed_anchors)
        if Domain_listed_anchors == 0:
            rule1_2_2 = -1
        elif Domain_listed_anchors < .31:
            rule1_2_2 = 1
        elif Domain_listed_anchors >= .31 and Domain_listed_anchors < .67:
            rule1_2_2 = 0
        else:
            rule1_2_2 = -1
    except:
        rule1_2_2 = -10
        
    
    

    return rule1_2_2



