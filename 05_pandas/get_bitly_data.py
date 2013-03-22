import os
from urllib2 import urlopen
from lxml.html import parse
import json
import glob

import pandas as pd

bitly_dir = 'bitly'

def get_bitly_data(num):
    url_path = 'http://bitly.measuredvoice.com/bitly_archive'
    data = urlopen(os.path.join(url_path,'?C=M;O=D'))

    parsed = parse(data)
    doc = parsed.getroot()

    links = doc.findall('.//a')
    for i in range(10):
        print links[i].get('href')
    print ''
    
    os.mkdir(bitly_dir)
    
    urls = [ link.get('href') for link in doc.findall('.//a') ]
    for u in urls[:num]:
        if u.startswith('usagov_bitly_data'):
            print "downloading ",  u
            data = urlopen(os.path.join(url_path,u)).read()
            with open(os.path.join('bitly', u+'.json'),'w') as out_file:
                out_file.write(data)

            
get_bitly_data(10)        









