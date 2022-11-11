import requests
import json
from Config_Manager import Config_Manager

class Helio_Controller:
    def __init__(self, helio_endpoint, identifier, mapping):
        self.helio_endpoint = helio_endpoint
        self.task = "/api/" + identifier
        self.mappings = mapping
        self.ttl = None
    
    def create_task(self):
        
        url = self.helio_endpoint + self.task
        payload = self.mappings
        headers = {
            'Content-Type': 'text/plain'
        }
        try:
            print("Creating Helio Task")
            response = requests.request("POST", url, headers=headers, data=payload)
            print("Helio Task Created")
        except:
            print("Error creating task")

    def retrieve_file(self):

        url = self.helio_endpoint + self.task + "/data"

        payload={}
        headers = {}

        try:
            print("Retrieving Helio Graph File")
            response = requests.request("GET", url, headers=headers, data=payload)
            print("Helio Graph File Retrieved")
            self.ttl = response.text
        except:
            print("Error retrieving file from helio")