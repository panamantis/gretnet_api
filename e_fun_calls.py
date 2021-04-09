import sys,os
import time
import datetime
import random
import re
import json

import requests

from flask import Flask, jsonify
from flasgger import Swagger      # pip install flasgger
from flasgger import swag_from
from flask import request

from api_helper import GretNet_API_Helper


LOCAL_PATH = os.path.abspath(os.path.dirname(__file__))+"/"

sys.path.insert(0,LOCAL_PATH)
sys.path.insert(0,LOCAL_PATH+"../")



#0v1# JC  Apr  8, 2021  Base setup


#Helper=GretNet_API_Helper()


## OpenAPI
#

#/crawl_domain
def handle_crawl_domain_request(): #*args,**kwargs):
    """Submit a domain to crawl
    ---
        post:
          summary: Handle submit domain to crawl requests
          consumes:
            - application/json
          parameters:
            - in: body
              name: meta
              description: Domain to crawl
              schema:
                type: object
                properties:
                  url:
                    type: string
          responses:
            200:
              description: Post accepted and processed.
    """
    
    try:
        the_json=request.json
    except: the_json={}
    
    if the_json:
        Helper.cache_request('crawl_domain',the_json, id='')
        
    try: print (str(request.json))
    except: pass

    result={}
    result['status_code']=200

    return jsonify(result)


#TBD:  add node or relation, standard search



def dev1():

    return

if __name__=='__main__':
    branches=['dev1']

    for b in branches:
        globals()[b]()

        

"""
"""

































        
"""

"""        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
