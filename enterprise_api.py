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


LOCAL_PATH = os.path.abspath(os.path.dirname(__file__))+"/"

sys.path.insert(0,LOCAL_PATH)
sys.path.insert(0,LOCAL_PATH+"../")

import configparser as ConfigParser #py3 pip install configparser


from api_helper import GretNet_API_Helper
import e_views
import e_monetization
import e_std_usage
import e_api_methods
import e_fun_calls
import e_test_calls


#0v1# JC  Apr  8, 2021  Base setup


##NOTES:
#- OpenAPI spec with minimal flask - swagger config
#- ref: https://github.com/flasgger/flasgger
#- if behind reverse proxy must adjust:  template = dict(swaggerUiPrefix=LazyString(lambda : request.environ.get('HTTP_X_SCRIPT_NAME', '')))


Config = ConfigParser.ConfigParser()
Config.read(LOCAL_PATH+"../settings.ini")

#gretapi_http=Config.get('gretapi','gretapi_protocol')



app = Flask(__name__)


swagger = Swagger(app)



## Simple external routing
    
#demo# app.add_url_rule('/colors/<palette>/','home',view_func=e_views.colors)
app.add_url_rule('/monetization','monetization',view_func=e_monetization.handle_web_monetization, methods=["POST"])
app.add_url_rule('/interledger','interledger',view_func=e_monetization.handle_interledger, methods=["POST"])

app.add_url_rule('/search','search',view_func=e_std_usage.handle_search_request, methods=["POST"])
app.add_url_rule('/status','status',view_func=e_std_usage.handle_status_request, methods=["POST"])
app.add_url_rule('/training','training',view_func=e_std_usage.handle_training_request, methods=["GET"])

app.add_url_rule('/creator','creator',view_func=e_api_methods.handle_submit_request, methods=["POST"])
app.add_url_rule('/creation','creation',view_func=e_api_methods.handle_creation_request, methods=["POST"])
app.add_url_rule('/target','target',view_func=e_api_methods.handle_target_request, methods=["POST"])

app.add_url_rule('/crawl_domain','crawl_domain',view_func=e_fun_calls.handle_crawl_domain_request, methods=["POST"])

app.add_url_rule('/test','test',view_func=e_test_calls.handle_test_request, methods=["GET"])
app.add_url_rule('/capability','capability',view_func=e_test_calls.handle_capability_request, methods=["GET"])



def dev1():
    print ("DRAFT SPEC FOR API:")
    print ("[A] web monetization")
    print ("[B] interledger")

    ## Usage
    print ("[C] keyword search get kanban id")
    print ("[D] kanban status")
    print ("[E] dump training manual")

    ## API friendly
    print ("[K] submit a new creator")
    print ("[L] submit a creators' creation (urls)")
    print ("[M] submit a target to audit!")
    
    ## Fun
    print ("[F] custom add node, relation")
    print ("[G] crawl domain")
    print ("[H] standard search")

    ## System
    print ("[I] list complete system capability")
    print ("[J] test check setup")

    return


if __name__=='__main__':
    branches=['dev1']

    for b in branches:
        globals()[b]()

    app.run(port=5000,debug=True)
        
        
        
        
        




"""

## Manually wrap
#  def wrap_api(cls, rt):
#D1#    return application.route(rt)(cls)
#D1#  import api
#D1#  galleries = wrap_api(api.get_galleries(), '/api/galleries')

POST SAMPLE

swagger: '2.0'
info:
  title: Demo App
  version: "1"
paths:
  /api/v1/list:
    post:
      description: testpost
      operationId: PostNewName
      consumes:
        - application/json
      parameters:
        - name: body
          in: body
          required: true
          schema:
            id : toto
            required:
              - first
              - last
            properties:
              first:
                type: string
                description: Unique identifier representing a First Name
              last:
                type: string
                description: Unique identifier representing a Last Name
      responses:
        200:
          description: creation OK
          
"""

    
    





























        
"""

"""        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
