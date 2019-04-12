'''
Created on 9. apr. 2019

@author: Lars Jespersen

@contains: functions for getting data from Unisport json sample data or other sources of data
'''

import json
import urllib.request
from urllib.error import HTTPError

class GetData(object):


    def __init__(self):
        '''
        Constructor
        '''
    
    def GetUnisportData(self):   
        try:
            url_address ='https://www.unisport.dk/api/sample'
            with urllib.request.urlopen(url_address) as url:
                unisportData = json.loads(url.read())
                return unisportData
        except HTTPError as ex:
            print(ex.read())