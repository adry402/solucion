from utils.api_errors import APIConnectException
import requests
import config

allApiData = config.apisToCall

# Este servicio llama a la API usando el metodo request

def callApi(url, id_ML):
    try:
        url = url + id_ML
        result = requests.get(url.rstrip(), timeout=5)
        return result.json()
    except Exception as e:
        raise APIConnectException(url, str(e))

        

    
