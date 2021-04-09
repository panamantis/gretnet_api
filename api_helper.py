import sys,os
import time
import datetime
import random
import re
import json

import requests

LOCAL_PATH = os.path.abspath(os.path.dirname(__file__))+"/"

sys.path.insert(0,LOCAL_PATH)
sys.path.insert(0,LOCAL_PATH+"../")


from istorage.ystorage_handler import Storage_Helper

import configparser as ConfigParser #py3 pip install configparser



#0v1# JC  Apr  8, 2021  Base setup


Config = ConfigParser.ConfigParser()
Config.read(LOCAL_PATH+"../settings.ini")


class GretNet_API_Helper(object):
    #
    def __init__(self):
        self.Storage=Storage_Helper(storage_dir=LOCAL_PATH+"api_cache")
        self.Storage.init_db('posts')
        return
    
    def cache_request(self,the_type,the_data,id=''):
        ## Use local sqlite
        if the_data:
            the_data['kind']=the_type
            if not id:
                id=str(datetime.datetime.now())
            self.Storage.db_put(id,'record',the_data,name='posts')
        return



def dev1():
    return


if __name__=='__main__':
    branches=['dev1']

    for b in branches:
        globals()[b]()

    app.run(port=5000,debug=True)
        
        

































        
"""

"""        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
