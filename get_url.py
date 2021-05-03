

from urllib.parse import urlparse


def get_url(url):
    domain_name = ''
    

    count = 0

    if '//' in url:

        split_url = url.split('//')
        double_split_url = split_url[1].split('/')

        

        for i in double_split_url[0]:

            if i == '.':
                count = count + 1
            
        if count == 1:
            domain_name = urlparse(url).netloc

        elif count == 2:
            t = urlparse(url).netloc
            domain_name = ('.'.join(t.split('.')[1:]))
        else:
            print('Suspicious URL, can you identify an IP adress in the url? If so, its phising. If multiple sub domain names are in the url, please remove 1 sub domain.  This script can only have at the most 1 sub domain name in the url')        
       
    return domain_name 

