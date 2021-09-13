from utils.api_errors import APIConnectException
import requests
import config

allApiData = config.apisToCall

# This service calls the APIs using the requests module

def callApi(url, id_ML):
    try:
        url = url + id_ML
        result = requests.get(url.rstrip(), timeout=5)
        return result.json()
    except Exception as e:
        raise APIConnectException(url, str(e))

        

    
