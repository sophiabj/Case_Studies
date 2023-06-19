import requests

class XecdClient(object):
    """XECD REST API Client"""

    def __init__(self, account_id, api_key, options = {}):
        self.options = {
            'auth': {
                'user': account_id,
                'password': api_key
            },
            'baseUrl': 'https://xecdapi.xe.com/v1/',
            'params': {}
        }
        self.options.update(options)

        self.convertFromRequestUri = 'convert_from.json'
        self.convertToRequestUri = 'convert_to.json'
        
    

    def __send(self, ops):
        self.options.update(ops)
        #cached for debugging purposes
        url = self.options["url"]
        username = self.options['auth']['user']
        password = self.options['auth']['password']
        params = self.options['params']
        temp = requests.get(url, auth=(username, password), params=params)
        data = temp.json()
        return data

    

    
    def convert_from(self, from_currency ="USD", to_currency ="*", amount = 1, obsolete = False, inverse = False, options = {}):
        ops = {
            'url': self.options['baseUrl'] + self.convertFromRequestUri,
            'params': {
                'from': from_currency,
                'to': to_currency,
                'amount': amount,
                'obsolete': True if obsolete else False,
                'inverse': True if inverse else False
            }
        }
        ops.update(options)
        return self.__send(ops)

    def convert_to(self, to_currency ="USD", from_currency ="*", amount = 1, obsolete = False, inverse = False, options = {}):
        ops = {
            'url': self.options['baseUrl'] + self.convertToRequestUri,
            'params': {
                'to': to_currency,
                'from': from_currency,
                'amount': amount,
                'obsolete': True if obsolete else False,
                'inverse': True if inverse else False
            }
        }
        ops.update(options)
        return self.__send(ops)

   
    
       
    