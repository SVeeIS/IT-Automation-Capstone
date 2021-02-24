#! /usr/bin/env python3

import os
import requests

dir = "/data/feedback/"
fb = {}

#List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
for data in os.listdir(dir):
  #membuka data
  with open('{}{}'.format(dir,data)) as file:
    #You should now have a list that contains all of the feedback files from the path /data/feedback. Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
    #Now, you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.
    fb["title"] = file.readline().strip()
    fb["name"] = file.readline().strip()
    fb["date"] = file.readline().strip()
    fb["feedback"] = file.readline().strip()
	
  #Use the Python requests module to post the dictionary to the company's website. Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. Replace <corpweb-external-IP> with corpweb's external IP address.
  response = requests.post("http://<corpweb-external-IP>/feedback/", json=fb)
  
if not response.ok:
   raise Exception("POST failed, Status code: {}, File: {}".format(response.status_code, data))
print("Successfully added!")
	