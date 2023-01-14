import requests
# dag #1 - extract rates dictionary
def extract_rates(apikey:str, start_date:str, end_date:str) -> str:

    from typing import Dict

    '''
    Extract Forex rates from Fixer.io. 
    Args:
        -> api_key:str, start_date:str, end_date:str
    Returns
        -> result:dict
    '''

    url = f"https://api.apilayer.com/fixer/timeseries?start_date={start_date}&end_date={end_date}"

    payload: Dict[str, str] = {}
    headers = {
        "apikey": api_key
    }


    response = requests.request("GET", url, headers=headers, data=payload)
    results = response.text

    return results