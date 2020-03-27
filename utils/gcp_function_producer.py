
#!/usr/bin/python3
# -*- coding: utf-8 -*- 
""" 
Created on Wed Mar 09 10:54:20 2020 
 
@author: guilherme passos |twiiter: @gpass0s

This module insert data Hubspot webhook coming in from into Redis 
""" 

import os
import random
import redis

_redis_host = os.environ["REDIS_HOST"]
_redis_port = os.environ["REDIS_PORT"]
_redis_queues = ["QUEUE_A", "QUEUE_B"]
redis_client = redis.Redis(host=redis_host, port=redis_port)


def insert_data_into_redis(request):

    # Set CORS headers for preflight requests
    if request.method == 'OPTIONS':
        # Allows GET requests from origin https://mydomain.com with
        # Authorization header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-:Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }

    payload = request.get_json()
    queue_to_insert = round(random.uniform(0,1))
    redis_client.rpush(_redis_queues[queue_to_insert], str(payload))
    return "Data successfully inserted to Redis"
