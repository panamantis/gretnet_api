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

#/search
def handle_search_request(): #*args,**kwargs):
    """Do standard search for Creator and request report
    This endpoint is equivalent to clicking the 'Analyze this' button
    in the search interface
    ---
        post:
          summary: Handle search requests
          consumes:
            - application/json
          parameters:
            - in: body
              name: meta
              description: The keyword to search for.
              schema:
                type: object
                properties:
                  keyword:
                    type: string
          responses:
            200:
              description: Post accepted and processed.
    """
    
    try:
        the_json=request.json
    except: the_json={}
    
    if the_json:
        Helper.cache_request('search',the_json, id='')
        
    keyword=the_json.get('keyword','')

    try: print (str(request.json))
    except: pass

    result={}
    result['status_code']=200

    return jsonify(result)

#/status
def handle_status_request(): #*args,**kwargs):
    """Do a status request for the requested report (kanban id)
    ---
        post:
          summary: Handle status requests
          consumes:
            - application/json
          parameters:
            - in: body
              name: meta
              description: Kanban ID to get the status for
              schema:
                type: object
                properties:
                  kanban_id:
                    type: string
          responses:
            200:
              description: Post accepted and processed.
    """
    
    try:
        the_json=request.json
    except: the_json={}
    
    if the_json:
        Helper.cache_request('kanban',the_json, id='')
        
    keyword=the_json.get('kanban_id','')

    try: print (str(request.json))
    except: pass

    result={}
    result['status_code']=200

    return jsonify(result)

#/training
def handle_training_request(): #*args,**kwargs):
    """Returns raw data structure of the training manual
    ---
        post:
          summary: Handle training manual requests
          consumes:
            - application/json
          parameters:
            - in: body
              name: meta
              description: Kanban ID to get the status for
              schema:
                type: object
                properties:
                  kanban_id:
                    type: string
          responses:
            200:
              description: Post accepted and processed.
    """
    
    try:
        the_json=request.json
    except: the_json={}
    
    if the_json:
        Helper.cache_request('training',the_json, id='')
        
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
