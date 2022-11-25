from queue import Queue
import time, json, requests

from adapter.library.logger import CloudWatch

cloudwatch = CloudWatch('Request', level='INFO')

class Request:

    @cloudwatch.debug
    def __init__(self, base_url, headers={}):
        """ constructs new 'Request' object.

            :param base_url: base url for all requests made
            :param request_per_min: limit number of requests per min (default: None)
            :param headers: set headers for all requests made (default: {})

            :return: none
        """
        self.base_url = base_url
        self.headers = headers

    @cloudwatch.debug
    def get(self, route):
        """ make get request.
        """
        request = requests.get(f"{self.base_url}/{route}", headers=self.headers)
        
        try: request = request.json()
        except: 
            raise json.JSONDecodeError

        return request