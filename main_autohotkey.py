"""
Main file of the project everthing is routing form here
"""

import requests
import json
import sys
import pyperclip

# import all the const to work
from const import *


def api_call(code='CYUL'):
    """
    :param code: code that will be sent to the API
    :return: name of the airport
    """
    payload = {"api_key": API_KEY, "airports": code}

    responce = requests.get(URL_API_ICAO, params=payload).content
    airport_info = json.loads(responce)

    if len(airport_info) == 1:
        return airport_info[0]["Location_Name"]

    else:
        return WRONG_AIRPORT

def get_args():
    """

    :return: arguments form the comannd line and transfer theme to scripts
    """
    return sys.argv[1]


if __name__ == "__main__":
    code_icao = get_args()
    airport_name = api_call(code_icao)
    pyperclip.copy(airport_name)
