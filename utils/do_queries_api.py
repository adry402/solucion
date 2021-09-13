from services.call_api import callApi
from utils.api_errors import APIBadRequestError

import config
import json

#List of APIs
allApiData = config.apisToCall
# Atributos a consultar en cada API
reqs = json.loads(config.to_query)


def get_tags(num_api, id_search, serch_new_var):
    lst_tags = []
    srch_id = str(num_api)
    if serch_new_var:
        srch_id = "new_vars"
    url = allApiData[num_api]
    response = callApi(url,str(id_search))
    for attr in reqs[srch_id]:
        if attr in response:
            lst_tags.append(str(response[attr]))
            print("Key exist in JSON data")
        else:
            lst_tags.append("NA")
            print("Key doesn't exist in JSON data")
    return lst_tags


def ret_response(id_ML):
    #Consulto los id requeridos adicionales
    lst_id_required = get_tags(0, id_ML,True)
    # Se consulta a la primera API donde tambien estan los 
    # id requeridos para las apis siguientes
    lst_first_API = get_tags(0,id_ML,False)
    lst_others_API = []
    # Este contador nos ayuda a avanzar entre APIs
    aux = 0
    for req in lst_id_required:
        aux = aux + 1
        if req != "":
            lst_temp = get_tags(aux,req,False)
        else:
            lst_temp = ["NA"]
        lst_others_API = lst_others_API + lst_temp
    lst_others_API.append(id_ML)
    return lst_first_API + lst_others_API