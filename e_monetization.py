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


import configparser as ConfigParser #py3 pip install configparser


#0v1# JC  Apr  8, 2021  Base setup


Config = ConfigParser.ConfigParser()
Config.read(LOCAL_PATH+"../settings.ini")

#gretapi_http=Config.get('gretapi','gretapi_protocol')


Helper=GretNet_API_Helper()


## OpenAPI
#

#/monetization
def handle_web_monetization(): #*args,**kwargs):
    """Endpoint accepts POST requests of monetization meta data
    This endpoint is strictly for meta data, use the interledger/ endpoint to push transaction specific details
    ---
        post:
          summary: Handle monetization post
          consumes:
            - application/json
          parameters:
            - in: body
              name: meta
              description: The Meta to push.
              schema:
                type: object
                properties:
                  generic_key1:
                    type: string
                  generic_key2:
                    type: string
          responses:
            200:
              description: Post accepted and processed.
    """
    
    try:
        the_json=request.json
    except: the_json={}
    
    if the_json:
        Helper.cache_request('monetization',the_json, id='')

    try: print (str(request.json))
    except: pass

    result={}
    result['status_code']=200

    return jsonify(result)


#/interledger
def handle_interledger(): 
    """Endpoint accepts POST requests of Interledger transaction
    This endpoint captures Interledger formatted json posts and stores it within GretNet.
    ---
        post:
          summary: Handles Interleger post
          consumes:
            - application/json
          parameters:
            - in: body
              name: meta
              description: The Meta to push.
              schema:
                type: object
                properties:
                  generic_key1:
                    type: string
                  generic_key2:
                    type: string
          responses:
            200:
              description: Post accepted and processed.
    """
    
    try:
        the_json=request.json
    except: the_json={}
    
    if the_json:
        Helper.cache_request('interledger',the_json, id='')

    try: print (str(request.json))
    except: pass

    result={}
    result['status_code']=200

    return jsonify(result)





def dev1():

    return

if __name__=='__main__':
    branches=['dev1']

    for b in branches:
        globals()[b]()

        

"""
          parameters:
            - in: body
              name: meta
              description: The Meta to push.
              schema:
                type: object
                required:
                  - userName
"""

































        
"""

"""        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
