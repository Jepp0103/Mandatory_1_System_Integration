from bottle import request, run, get, post, view, response
import json
##import csv
##import requests

hostname = "192.168.111.148"

@post("/receive-json")
def do():
    jsondata= json.load(request.body)
    number = int(jsondata["data"])
    number = number * 3
    response.content_type="text/csv"
    return "data\n"+str(number)

################################
run(host=hostname, port=3333, debug=True, reloader=True, server="paste")