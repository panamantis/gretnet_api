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

#/creator
def handle_submit_request(): #*args,**kwargs):
    """Submit a new Creator or update their details
    ---
        post:
          summary: Handle submit creator requests
          consumes:
            - application/json
          parameters:
            - in: body
              name: meta
              description: Creator meta data
              schema:
                type: object
                properties:
                  meta_string:
                    type: string
          responses:
            200:
              description: Post accepted and processed.
    """
    
    try:
        the_json=request.json
    except: the_json={}
    
    if the_json:
        Helper.cache_request('submit_creator',the_json, id='')
        
    try: print (str(request.json))
    except: pass

    result={}
    result['status_code']=200

    return jsonify(result)

#/creation
def handle_creation_request(): #*args,**kwargs):
    """Submit a new Creation or update the details
    ---
        post:
          summary: Handle submit creation requests
          consumes:
            - application/json
          parameters:
            - in: body
              name: meta
              description: Creation meta data
              schema:
                type: object
                properties:
                  meta_string:
                    type: string
          responses:
            200:
              description: Post accepted and processed.
    """
    
    try:
        the_json=request.json
    except: the_json={}
    
    if the_json:
        Helper.cache_request('submit_creation',the_json, id='')
        
    try: print (str(request.json))
    except: pass

    result={}
    result['status_code']=200

    return jsonify(result)

#/target
def handle_target_request(): #*args,**kwargs):
    """Submit a target entity to audit or crawl
    ---
        post:
          summary: Handle submit target requests
          consumes:
            - application/json
          parameters:
            - in: body
              name: meta
              description: Target meta data
              schema:
                type: object
                properties:
                  meta_string:
                    type: string
          responses:
            200:
              description: Post accepted and processed.
    """
    
    try:
        the_json=request.json
    except: the_json={}
    
    if the_json:
        Helper.cache_request('submit_target',the_json, id='')
        
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
"""

































        
"""

"""        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
